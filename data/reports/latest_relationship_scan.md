# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-10T09:22:27.814022+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7647`

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

- `market_context_high->unknown_4h` score `40.9447` n `91` status `ready` deltaP `-6.188` edge `3.5072` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.7014` n `91` status `ready` deltaP `35.6905` edge `0.6134` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `8.9385` n `91` status `ready` deltaP `19.4832` edge `1.3309` maxDD `-17.8526`
- `market_context_high->crypto_alt_24h` score `1.6436` n `91` status `ready` deltaP `10.0578` edge `0.7549` maxDD `-35.5652`
- `market_context_high->crypto_major_4h` score `1.2863` n `91` status `ready` deltaP `14.9625` edge `0.1982` maxDD `-6.9761`
- `market_context_high->fx_1h` score `0.2487` n `91` status `ready` deltaP `6.5474` edge `0.0013` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.14` n `91` status `ready` deltaP `8.9459` edge `0.0472` maxDD `-3.7778`
- `market_context_high->fx_4h` score `-0.1062` n `91` status `ready` deltaP `8.674` edge `0.008` maxDD `-0.3077`
- `market_context_high->index_24h` score `-0.2708` n `91` status `ready` deltaP `9.7702` edge `0.0911` maxDD `-1.9432`
- `market_context_high->metal_1h` score `-0.2966` n `91` status `ready` deltaP `3.7475` edge `0.0015` maxDD `-0.7626`
- `market_context_high->metal_24h` score `-0.3574` n `91` status `ready` deltaP `6.7172` edge `0.0579` maxDD `-3.5466`
- `market_context_high->commodity_1h` score `-0.3627` n `91` status `ready` deltaP `0.7025` edge `0.0027` maxDD `-0.3417`
- `market_context_high->commodity_4h` score `-0.7615` n `91` status `ready` deltaP `-2.4038` edge `-0.0116` maxDD `-1.6002`
- `market_context_high->equity_1h` score `-0.9134` n `91` status `ready` deltaP `-4.2886` edge `-0.0045` maxDD `-2.0542`
- `market_context_high->metal_4h` score `-0.9403` n `91` status `ready` deltaP `-5.0088` edge `0.0136` maxDD `-1.0609`
- `market_context_high->unknown_1h` score `-0.9713` n `91` status `ready` deltaP `-4.0682` edge `-0.0123` maxDD `-0.9885`
- `market_context_high->crypto_alt_4h` score `-1.1637` n `91` status `ready` deltaP `-8.1715` edge `0.0986` maxDD `-8.7986`
- `market_context_high->crypto_alt_1h` score `-1.1676` n `91` status `ready` deltaP `-2.0941` edge `0.0305` maxDD `-4.7735`
- `market_context_high->index_1h` score `-1.2325` n `91` status `ready` deltaP `-10.3376` edge `-0.0029` maxDD `-0.5627`
- `market_context_high->index_4h` score `-1.2866` n `91` status `ready` deltaP `-10.8651` edge `0.0007` maxDD `-1.1242`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
