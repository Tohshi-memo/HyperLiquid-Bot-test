# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T19:52:26.459568+00:00`
- Price records: `672`
- Market context records: `4966`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9536`

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

- `market_context_high->unknown_1h` score `17.5857` n `100` status `ready` deltaP `8.4551` edge `1.4592` maxDD `-1.674`
- `market_context_high->unknown_4h` score `12.0597` n `94` status `ready` deltaP `28.4088` edge `0.867` maxDD `-1.7801`
- `market_context_high->crypto_major_4h` score `7.4876` n `94` status `ready` deltaP `22.1977` edge `0.5984` maxDD `-7.1265`
- `market_context_high->crypto_alt_4h` score `7.1972` n `94` status `ready` deltaP `22.6486` edge `0.584` maxDD `-7.8181`
- `market_context_high->unknown_24h` score `5.8365` n `91` status `ready` deltaP `27.3199` edge `0.3385` maxDD `-1.4072`
- `market_context_high->equity_4h` score `1.7833` n `94` status `ready` deltaP `14.5887` edge `0.1895` maxDD `-6.3852`
- `market_context_high->metal_4h` score `1.5667` n `94` status `ready` deltaP `12.633` edge `0.1209` maxDD `-1.9651`
- `market_context_high->crypto_major_1h` score `1.0416` n `100` status `ready` deltaP `7.3413` edge `0.1417` maxDD `-5.6406`
- `market_context_high->equity_1h` score `1.0059` n `100` status `ready` deltaP `9.8503` edge `0.0755` maxDD `-2.5875`
- `market_context_high->index_4h` score `0.9788` n `94` status `ready` deltaP `12.4708` edge `0.0446` maxDD `-0.6938`
- `market_context_high->crypto_alt_1h` score `0.4968` n `100` status `ready` deltaP `8.4491` edge `0.1096` maxDD `-5.5126`
- `market_context_high->metal_1h` score `0.0978` n `100` status `ready` deltaP `4.6407` edge `0.0352` maxDD `-1.3057`
- `market_context_high->commodity_1h` score `-0.4052` n `100` status `ready` deltaP `0.994` edge `0.0074` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.4278` n `100` status `ready` deltaP `1.2515` edge `0.0123` maxDD `-0.7054`
- `market_context_high->commodity_4h` score `-0.9795` n `94` status `ready` deltaP `7.1711` edge `-0.0049` maxDD `-4.9624`
- `market_context_high->fx_4h` score `-1.1057` n `94` status `ready` deltaP `-6.0781` edge `-0.0042` maxDD `-1.0967`
- `market_context_high->fx_24h` score `-1.5583` n `91` status `ready` deltaP `-2.3447` edge `-0.0132` maxDD `-2.749`
- `market_context_high->fx_1h` score `-1.5655` n `100` status `ready` deltaP `-9.9581` edge `-0.0041` maxDD `-0.4646`
- `market_context_high->commodity_24h` score `-3.9923` n `91` status `ready` deltaP `19.6485` edge `0.0472` maxDD `-27.5371`
- `market_context_high->metal_24h` score `-7.0133` n `91` status `ready` deltaP `-10.2088` edge `0.0291` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
