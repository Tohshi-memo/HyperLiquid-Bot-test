# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T10:07:32.058075+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `6933`

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

- `market_context_high->unknown_4h` score `42.663` n `85` status `ready` deltaP `-11.9243` edge `3.6928` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.3326` n `61` status `ready` deltaP `35.9403` edge `0.581` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `6.2204` n `61` status `ready` deltaP `6.2415` edge `1.0707` maxDD `-17.8526`
- `market_context_high->fx_4h` score `1.3603` n `85` status `ready` deltaP `19.6539` edge `0.0107` maxDD `-0.2692`
- `market_context_high->index_24h` score `1.1733` n `61` status `ready` deltaP `20.0877` edge `0.1185` maxDD `-1.1592`
- `market_context_high->commodity_1h` score `0.3255` n `93` status `ready` deltaP `6.4999` edge `0.0089` maxDD `-0.3417`
- `market_context_high->commodity_4h` score `0.2904` n `85` status `ready` deltaP `10.2655` edge `0.0091` maxDD `-1.6002`
- `market_context_high->fx_1h` score `-0.0101` n `93` status `ready` deltaP `3.1244` edge `0.0021` maxDD `-0.271`
- `market_context_high->fx_24h` score `-0.125` n `61` status `ready` deltaP `10.4821` edge `0.0142` maxDD `-1.0082`
- `market_context_high->crypto_major_1h` score `-0.4487` n `93` status `ready` deltaP `0.7147` edge `0.0266` maxDD `-3.7778`
- `market_context_high->metal_1h` score `-0.6477` n `93` status `ready` deltaP `-3.7361` edge `0.0014` maxDD `-0.7626`
- `market_context_high->metal_4h` score `-0.6801` n `85` status `ready` deltaP `-4.5319` edge `0.0153` maxDD `-1.1153`
- `market_context_high->crypto_major_4h` score `-1.0171` n `85` status `ready` deltaP `-2.6596` edge `0.0916` maxDD `-10.6751`
- `market_context_high->crypto_alt_1h` score `-1.0887` n `93` status `ready` deltaP `-6.1586` edge `0.0174` maxDD `-4.9401`
- `market_context_high->metal_24h` score `-1.285` n `61` status `ready` deltaP `-8.0915` edge `0.0377` maxDD `-3.5466`
- `market_context_high->index_4h` score `-1.3147` n `85` status `ready` deltaP `-11.3289` edge `0.0002` maxDD `-1.1242`
- `market_context_high->index_1h` score `-1.3908` n `93` status `ready` deltaP `-4.0355` edge `-0.0028` maxDD `-0.5627`
- `market_context_high->equity_1h` score `-1.4944` n `93` status `ready` deltaP `-4.6471` edge `-0.0066` maxDD `-2.2898`
- `market_context_high->crypto_alt_4h` score `-2.1035` n `85` status `ready` deltaP `-9.41` edge `0.0489` maxDD `-13.8008`
- `market_context_high->equity_4h` score `-2.7086` n `85` status `ready` deltaP `-9.1912` edge `-0.0052` maxDD `-6.4057`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
