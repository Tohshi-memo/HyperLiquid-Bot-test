# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T09:52:30.803554+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8300`

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

- `market_context_high->unknown_1h` score `68.6478` n `124` status `ready` deltaP `-0.6422` edge `5.7664` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `35.4117` n `112` status `ready` deltaP `-2.1124` edge `3.0188` maxDD `-2.2991`
- `market_context_high->crypto_major_24h` score `10.8992` n `81` status `ready` deltaP `29.8032` edge `0.7232` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.3575` n `65` status `ready` deltaP `32.5516` edge `0.5831` maxDD `-0.6258`
- `market_context_high->crypto_alt_24h` score `6.9822` n `81` status `ready` deltaP `25.3666` edge `0.4747` maxDD `-2.9571`
- `news_risk_high->crypto_alt_4h` score `5.8488` n `65` status `ready` deltaP `19.7866` edge `0.4899` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `3.4605` n `112` status `ready` deltaP `15.2439` edge `0.2665` maxDD `-4.047`
- `news_risk_high->index_24h` score `3.3608` n `65` status `ready` deltaP `23.7847` edge `0.1215` maxDD `0.0`
- `news_risk_high->equity_24h` score `3.1577` n `65` status `ready` deltaP `11.0337` edge `0.1996` maxDD `-0.1344`
- `news_risk_high->index_4h` score `2.9424` n `65` status `ready` deltaP `32.371` edge `0.0556` maxDD `-0.4296`
- `news_risk_high->equity_4h` score `2.5628` n `65` status `ready` deltaP `20.5769` edge `0.1374` maxDD `-2.881`
- `news_risk_high->crypto_major_1h` score `2.4317` n `65` status `ready` deltaP `9.7167` edge `0.1734` maxDD `-1.5096`
- `news_risk_high->index_1h` score `2.0471` n `65` status `ready` deltaP `25.3178` edge `0.0168` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.8824` n `65` status `ready` deltaP `17.7064` edge `0.0804` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.4916` n `112` status `ready` deltaP `26.1106` edge `0.0259` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.0701` n `65` status `ready` deltaP `3.222` edge `0.1196` maxDD `-2.4854`
- `market_context_high->fx_1h` score `0.8647` n `124` status `ready` deltaP `14.2264` edge `0.0056` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.7167` n `124` status `ready` deltaP `9.6919` edge `0.084` maxDD `-3.7778`
- `news_risk_high->commodity_24h` score `0.537` n `65` status `ready` deltaP `24.9119` edge `0.1059` maxDD `-10.9169`
- `market_context_high->crypto_alt_4h` score `0.508` n `112` status `ready` deltaP `2.2866` edge `0.206` maxDD `-7.6465`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
