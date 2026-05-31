# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T10:07:21.564907+00:00`
- Price records: `672`
- Market context records: `2446`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9222`

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

- `news_risk_high->crypto_alt_24h` score `19.2345` n `43` status `ready` deltaP `43.2655` edge `1.3733` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `19.0696` n `43` status `ready` deltaP `53.9244` edge `1.2736` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.7499` n `43` status `ready` deltaP `29.7925` edge `1.062` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `9.4162` n `43` status `ready` deltaP `16.6424` edge `0.7318` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `6.9449` n `43` status `ready` deltaP `23.3002` edge `0.446` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `5.9914` n `108` status `ready` deltaP `22.3958` edge `0.3828` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `5.0674` n `124` status `ready` deltaP `23.3675` edge `0.4475` maxDD `-10.1468`
- `news_risk_high->index_24h` score `4.9615` n `43` status `ready` deltaP `8.9309` edge `0.3958` maxDD `-1.3507`
- `market_context_high->crypto_alt_4h` score `4.8494` n `124` status `ready` deltaP `23.3428` edge `0.5164` maxDD `-15.4319`
- `news_risk_high->commodity_4h` score `3.1815` n `43` status `ready` deltaP `28.6514` edge `0.284` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.1547` n `43` status `ready` deltaP `32.8892` edge `0.0621` maxDD `-0.1442`
- `market_context_high->unknown_4h` score `2.6076` n `124` status `ready` deltaP `13.0754` edge `0.1911` maxDD `-1.8773`
- `market_context_high->crypto_major_24h` score `2.5363` n `108` status `ready` deltaP `11.6898` edge `0.6365` maxDD `-25.1408`
- `news_risk_high->fx_4h` score `2.122` n `43` status `ready` deltaP `26.9746` edge `0.0154` maxDD `-0.1382`
- `news_risk_high->unknown_4h` score `1.6779` n `43` status `ready` deltaP `15.3822` edge `0.1096` maxDD `-2.7857`
- `market_context_high->index_24h` score `1.5692` n `108` status `ready` deltaP `7.6389` edge `0.1154` maxDD `-0.5117`
- `news_risk_high->unknown_1h` score `1.1133` n `43` status `ready` deltaP `20.4463` edge `0.0034` maxDD `-1.7548`
- `market_context_high->crypto_major_1h` score `0.8563` n `135` status `ready` deltaP `9.236` edge `0.1292` maxDD `-4.2199`
- `market_context_high->crypto_alt_1h` score `0.7645` n `135` status `ready` deltaP `7.912` edge `0.1297` maxDD `-6.1656`
- `market_context_high->index_4h` score `0.5927` n `124` status `ready` deltaP `13.0606` edge `0.0449` maxDD `-2.2732`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
