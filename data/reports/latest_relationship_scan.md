# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T05:52:27.127259+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `5933`

## Conditions

- `news_risk_high`: News Risk is elevated.
- `macro_risk_high`: Macro Risk is elevated.
- `risk_on_high`: Risk-On score is elevated.
- `market_context_high`: Market Context is supportive.
- `polymarket_volume_spike`: Polymarket 24h volume z-score is elevated.
- `flow_alert_high`: Flow Alert score is elevated.
- `news_and_polymarket`: News Risk and Polymarket volume spike happen together.
- `risk_on_and_context`: Risk-On and Market Context are both supportive.
- `macro_and_flow`: Macro Risk and Flow Alert are elevated together.

## Top Patterns

- `market_context_high->unknown_4h` score `42.7995` n `85` status `ready` deltaP `-12.9484` edge `3.711` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.6898` n `78` status `ready` deltaP `38.6351` edge `0.5928` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `8.0692` n `78` status `ready` deltaP `15.7853` edge `1.2441` maxDD `-17.8526`
- `market_context_high->fx_4h` score `1.0917` n `85` status `ready` deltaP `17.6058` edge `0.0103` maxDD `-0.2692`
- `market_context_high->crypto_major_4h` score `0.7466` n `85` status `ready` deltaP `10.6528` edge `0.177` maxDD `-8.5176`
- `market_context_high->fx_1h` score `0.1124` n `97` status `ready` deltaP `5.5852` edge `0.0014` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `-0.0183` n `97` status `ready` deltaP `6.6671` edge `0.0421` maxDD `-3.7778`
- `market_context_high->commodity_1h` score `-0.0484` n `97` status `ready` deltaP `3.3907` edge `0.0068` maxDD `-0.3417`
- `market_context_high->commodity_4h` score `-0.1368` n `85` status `ready` deltaP `5.1453` edge `0.0015` maxDD `-1.6002`
- `market_context_high->index_24h` score `-0.3274` n `78` status `ready` deltaP `6.8377` edge `0.0946` maxDD `-1.9056`
- `market_context_high->metal_24h` score `-0.6107` n `78` status `ready` deltaP `3.5256` edge `0.0467` maxDD `-3.5466`
- `market_context_high->metal_1h` score `-0.6763` n `97` status `ready` deltaP `-4.8058` edge `0.0007` maxDD `-0.7626`
- `market_context_high->crypto_alt_1h` score `-0.8008` n `97` status `ready` deltaP `-1.747` edge `0.0249` maxDD `-4.9401`
- `market_context_high->crypto_alt_24h` score `-0.8966` n `78` status `ready` deltaP `2.8178` edge `0.4775` maxDD `-35.5652`
- `market_context_high->metal_4h` score `-1.3451` n `85` status `ready` deltaP `-12.7242` edge `0.0135` maxDD `-1.0898`
- `market_context_high->fx_24h` score `-1.6161` n `78` status `ready` deltaP `-2.2169` edge `-0.0035` maxDD `-2.446`
- `market_context_high->equity_1h` score `-1.6179` n `97` status `ready` deltaP `-6.221` edge `-0.0064` maxDD `-2.2898`
- `market_context_high->index_1h` score `-1.7834` n `97` status `ready` deltaP `-8.9126` edge `-0.003` maxDD `-0.5627`
- `market_context_high->index_4h` score `-2.2671` n `85` status `ready` deltaP `-14.401` edge `0.0003` maxDD `-1.1242`
- `market_context_high->equity_4h` score `-2.7882` n `85` status `ready` deltaP `-11.2392` edge `-0.0041` maxDD `-5.9321`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
