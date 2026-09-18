# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T00:52:27.502723+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8686`

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

- `market_context_high->unknown_4h` score `35.658` n `149` status `ready` deltaP `-0.311` edge `2.9969` maxDD `-0.5326`
- `news_risk_high->unknown_4h` score `22.4104` n `69` status `ready` deltaP `-6.1859` edge `1.954` maxDD `-1.9518`
- `risk_on_high->unknown_4h` score `9.5367` n `52` status `ready` deltaP `-7.5516` edge `0.8676` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `9.5367` n `52` status `ready` deltaP `-7.5516` edge `0.8676` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `9.0784` n `52` status `ready` deltaP `50.0` edge `0.4232` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.0784` n `52` status `ready` deltaP `50.0` edge `0.4232` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `8.6378` n `47` status `ready` deltaP `31.069` edge `0.6506` maxDD `-9.3661`
- `market_context_high->commodity_24h` score `7.7793` n `149` status `ready` deltaP `43.2886` edge `0.4122` maxDD `-0.8682`
- `news_risk_high->equity_24h` score `4.1495` n `47` status `ready` deltaP `10.786` edge `0.4513` maxDD `-6.5262`
- `news_risk_high->index_24h` score `4.0094` n `47` status `ready` deltaP `28.1582` edge `0.164` maxDD `-0.075`
- `risk_on_high->commodity_4h` score `3.0305` n `52` status `ready` deltaP `33.3021` edge `0.0655` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `3.0305` n `52` status `ready` deltaP `33.3021` edge `0.0655` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.9302` n `149` status `ready` deltaP `29.8044` edge `0.0873` maxDD `-0.345`
- `news_risk_high->crypto_major_24h` score `2.0607` n `47` status `ready` deltaP `4.8426` edge `0.4314` maxDD `-13.2931`
- `risk_on_high->fx_24h` score `1.6992` n `52` status `ready` deltaP `25.1602` edge `-0.0219` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `1.6992` n `52` status `ready` deltaP `25.1602` edge `-0.0219` maxDD `-0.0054`
- `market_context_high->fx_24h` score `1.5643` n `149` status `ready` deltaP `22.3853` edge `0.0027` maxDD `-0.0593`
- `news_risk_high->metal_24h` score `1.5077` n `47` status `ready` deltaP `11.0483` edge `0.0974` maxDD `-0.6334`
- `market_context_high->commodity_1h` score `1.2739` n `149` status `ready` deltaP `17.5582` edge `0.0268` maxDD `-0.3491`
- `news_risk_high->equity_4h` score `0.7849` n `69` status `ready` deltaP `10.1096` edge `0.0817` maxDD `-3.3619`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
