# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T08:07:26.326386+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8486`

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

- `news_risk_high->crypto_major_24h` score `56.2827` n `69` status `ready` deltaP `35.5223` edge `4.5426` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `49.352` n `69` status `ready` deltaP `39.2814` edge `3.9887` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `34.9966` n `148` status `ready` deltaP `-1.9034` edge `2.9524` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `11.991` n `69` status `ready` deltaP `45.2521` edge `0.7018` maxDD `-0.0053`
- `risk_on_high->unknown_4h` score `8.3719` n `52` status `ready` deltaP `-9.076` edge `0.7807` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `8.3719` n `52` status `ready` deltaP `-9.076` edge `0.7807` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.2424` n `52` status `ready` deltaP `44.9653` edge `0.3871` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.2424` n `52` status `ready` deltaP `44.9653` edge `0.3871` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.9577` n `148` status `ready` deltaP `38.2085` edge `0.3776` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `6.7239` n `81` status `ready` deltaP `22.9449` edge `0.5283` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.5907` n `81` status `ready` deltaP `19.8359` edge `0.3761` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `3.3945` n `81` status `ready` deltaP `17.7497` edge `0.2111` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.7276` n `81` status `ready` deltaP `20.9673` edge `0.1398` maxDD `-2.8494`
- `risk_on_high->commodity_4h` score `2.6161` n `52` status `ready` deltaP `31.1679` edge `0.0452` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.6161` n `52` status `ready` deltaP `31.1679` edge `0.0452` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.5058` n `148` status `ready` deltaP `27.5297` edge `0.0671` maxDD `-0.345`
- `news_risk_high->metal_24h` score `2.4964` n `69` status `ready` deltaP `26.872` edge `0.0922` maxDD `-1.7316`
- `news_risk_high->fx_4h` score `1.2838` n `81` status `ready` deltaP `14.4554` edge `0.0325` maxDD `-0.084`
- `market_context_high->commodity_1h` score `1.022` n `148` status `ready` deltaP `15.2492` edge `0.0212` maxDD `-0.3491`
- `news_risk_high->fx_24h` score `0.8268` n `69` status `ready` deltaP `4.2195` edge `0.0451` maxDD `-0.0128`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
