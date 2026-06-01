# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T00:22:15.553993+00:00`
- Price records: `672`
- Market context records: `2511`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9280`

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

- `market_context_high->unknown_24h` score `5.1927` n `121` status `ready` deltaP `19.6869` edge `0.3343` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `4.6925` n `151` status `ready` deltaP `21.5756` edge `0.5151` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.8923` n `151` status `ready` deltaP `17.8596` edge `0.3863` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `2.1776` n `121` status `ready` deltaP `11.9003` edge `0.5891` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `2.0455` n `151` status `ready` deltaP `11.5843` edge `0.1982` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `0.7941` n `161` status `ready` deltaP `7.4265` edge `0.1354` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `0.5069` n `161` status `ready` deltaP `7.4041` edge `0.1123` maxDD `-4.2199`
- `market_context_high->crypto_alt_24h` score `0.1907` n `121` status `ready` deltaP `1.7533` edge `0.7085` maxDD `-43.6595`
- `market_context_high->index_24h` score `0.0528` n `121` status `ready` deltaP `3.6716` edge `0.078` maxDD `-2.5127`
- `market_context_high->equity_24h` score `-0.1337` n `121` status `ready` deltaP `18.0685` edge `0.0211` maxDD `-6.8828`
- `market_context_high->index_4h` score `-0.1349` n `151` status `ready` deltaP `6.7214` edge `0.0281` maxDD `-2.3986`
- `market_context_high->fx_1h` score `-0.2946` n `161` status `ready` deltaP `1.6802` edge `0.0045` maxDD `-0.278`
- `market_context_high->metal_1h` score `-0.3892` n `161` status `ready` deltaP `1.5082` edge `0.016` maxDD `-3.0759`
- `market_context_high->unknown_1h` score `-0.452` n `161` status `ready` deltaP `1.9191` edge `0.0215` maxDD `-3.0902`
- `market_context_high->commodity_1h` score `-0.4696` n `161` status `ready` deltaP `2.8397` edge `0.0087` maxDD `-4.3601`
- `market_context_high->index_1h` score `-0.5716` n `161` status `ready` deltaP `-0.2594` edge `0.0035` maxDD `-1.2855`
- `market_context_high->fx_4h` score `-0.6575` n `151` status `ready` deltaP `-1.0984` edge `0.009` maxDD `-0.8774`
- `market_context_high->fx_24h` score `-0.8158` n `121` status `ready` deltaP `4.0103` edge `0.0051` maxDD `-2.5804`
- `market_context_high->equity_1h` score `-0.9059` n `161` status `ready` deltaP `-0.4853` edge `0.0116` maxDD `-2.7085`
- `market_context_high->metal_4h` score `-1.1043` n `151` status `ready` deltaP `1.8929` edge `0.0341` maxDD `-4.7664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
