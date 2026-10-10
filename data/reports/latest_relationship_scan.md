# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-10T02:22:27.464559+00:00`
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

- `market_context_high->unknown_4h` score `40.9599` n `91` status `ready` deltaP `-5.5782` edge `3.5044` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.4485` n `91` status `ready` deltaP `33.2641` edge `0.6085` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `8.691` n `91` status `ready` deltaP `18.4433` edge `1.3061` maxDD `-17.8526`
- `market_context_high->crypto_alt_24h` score `1.7232` n `91` status `ready` deltaP `10.0578` edge `0.7651` maxDD `-35.5652`
- `market_context_high->crypto_major_4h` score `1.5889` n `91` status `ready` deltaP `18.621` edge `0.2126` maxDD `-6.9761`
- `market_context_high->fx_1h` score `0.2128` n `91` status `ready` deltaP `6.0983` edge `0.0013` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.2109` n `91` status `ready` deltaP `9.9938` edge `0.0493` maxDD `-3.7778`
- `market_context_high->fx_4h` score `0.1059` n `91` status `ready` deltaP `11.2654` edge `0.0084` maxDD `-0.3077`
- `market_context_high->commodity_1h` score `-0.2476` n `91` status `ready` deltaP `1.9001` edge `0.0043` maxDD `-0.3417`
- `market_context_high->metal_24h` score `-0.2842` n `91` status `ready` deltaP `7.5838` edge `0.0615` maxDD `-3.5466`
- `market_context_high->metal_1h` score `-0.2966` n `91` status `ready` deltaP `3.7475` edge `0.0015` maxDD `-0.7626`
- `market_context_high->index_24h` score `-0.37` n `91` status `ready` deltaP `7.8638` edge `0.0911` maxDD `-1.9432`
- `market_context_high->commodity_4h` score `-0.6145` n `91` status `ready` deltaP `-0.1172` edge `-0.008` maxDD `-1.6002`
- `market_context_high->equity_1h` score `-0.8815` n `91` status `ready` deltaP `-3.6898` edge `-0.0044` maxDD `-2.0542`
- `market_context_high->crypto_alt_4h` score `-0.9499` n `91` status `ready` deltaP `-7.1044` edge `0.1189` maxDD `-8.7986`
- `market_context_high->metal_4h` score `-0.9807` n `91` status `ready` deltaP `-5.7709` edge `0.0135` maxDD `-1.0609`
- `market_context_high->unknown_1h` score `-0.9846` n `91` status `ready` deltaP `-3.9185` edge `-0.0144` maxDD `-0.9885`
- `market_context_high->crypto_alt_1h` score `-1.1711` n `91` status `ready` deltaP `-2.2438` edge `0.0312` maxDD `-4.7735`
- `market_context_high->index_4h` score `-1.2288` n `91` status `ready` deltaP `-9.798` edge `0.001` maxDD `-1.1242`
- `market_context_high->index_1h` score `-1.2419` n `91` status `ready` deltaP `-10.4873` edge `-0.0031` maxDD `-0.5627`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
