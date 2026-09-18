# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T00:37:27.702126+00:00`
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

- `market_context_high->unknown_4h` score `35.6664` n `149` status `ready` deltaP `-0.311` edge `2.9976` maxDD `-0.5326`
- `news_risk_high->unknown_4h` score `21.0734` n `70` status `ready` deltaP `-7.3868` edge `1.8611` maxDD `-2.4592`
- `risk_on_high->unknown_4h` score `9.5451` n `52` status `ready` deltaP `-7.5516` edge `0.8683` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `9.5451` n `52` status `ready` deltaP `-7.5516` edge `0.8683` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `9.0964` n `52` status `ready` deltaP `50.0` edge `0.4247` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.0964` n `52` status `ready` deltaP `50.0` edge `0.4247` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `8.8066` n `48` status `ready` deltaP `31.4236` edge `0.6623` maxDD `-9.3661`
- `market_context_high->commodity_24h` score `7.7973` n `149` status `ready` deltaP `43.2886` edge `0.4137` maxDD `-0.8682`
- `news_risk_high->equity_24h` score `4.3991` n `48` status `ready` deltaP `11.8055` edge `0.4653` maxDD `-6.5262`
- `news_risk_high->index_24h` score `4.0964` n `48` status `ready` deltaP `28.6458` edge `0.168` maxDD `-0.075`
- `risk_on_high->commodity_4h` score `3.0329` n `52` status `ready` deltaP `33.3021` edge `0.0657` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `3.0329` n `52` status `ready` deltaP `33.3021` edge `0.0657` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.9326` n `149` status `ready` deltaP `29.8044` edge `0.0875` maxDD `-0.345`
- `news_risk_high->crypto_major_24h` score `2.3322` n `48` status `ready` deltaP `5.7291` edge `0.4603` maxDD `-13.2931`
- `risk_on_high->fx_24h` score `1.7191` n `52` status `ready` deltaP `25.3338` edge `-0.0214` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `1.7191` n `52` status `ready` deltaP `25.3338` edge `-0.0214` maxDD `-0.0054`
- `news_risk_high->metal_24h` score `1.6409` n `48` status `ready` deltaP `11.9792` edge `0.1023` maxDD `-0.6334`
- `market_context_high->fx_24h` score `1.5842` n `149` status `ready` deltaP `22.5589` edge `0.0032` maxDD `-0.0593`
- `market_context_high->commodity_1h` score `1.2763` n `149` status `ready` deltaP `17.5582` edge `0.027` maxDD `-0.3491`
- `news_risk_high->equity_4h` score `0.6676` n `70` status `ready` deltaP `9.1986` edge `0.078` maxDD `-3.3619`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
