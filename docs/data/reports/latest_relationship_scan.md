# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T06:52:27.507828+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8452`

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

- `news_risk_high->crypto_major_24h` score `58.0629` n `64` status `ready` deltaP `35.5903` edge `4.6905` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `51.4259` n `64` status `ready` deltaP `38.7153` edge `4.1653` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `36.0281` n `149` status `ready` deltaP `-1.8354` edge `3.0379` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `13.0665` n `64` status `ready` deltaP `47.3958` edge `0.7729` maxDD `0.0`
- `risk_on_high->unknown_4h` score `9.9067` n `52` status `ready` deltaP `-9.076` edge `0.9086` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `9.9067` n `52` status `ready` deltaP `-9.076` edge `0.9086` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.2568` n `52` status `ready` deltaP `44.9653` edge `0.3883` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.2568` n `52` status `ready` deltaP `44.9653` edge `0.3883` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.9577` n `149` status `ready` deltaP `38.2539` edge `0.3773` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `6.9444` n `80` status `ready` deltaP `23.2012` edge `0.5408` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.7271` n `80` status `ready` deltaP `20.0305` edge `0.382` maxDD `-8.0625`
- `news_risk_high->metal_24h` score `3.6811` n `64` status `ready` deltaP `32.1181` edge `0.1204` maxDD `-0.5541`
- `news_risk_high->crypto_alt_1h` score `3.3513` n `81` status `ready` deltaP `17.4503` edge `0.2095` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.6581` n `81` status `ready` deltaP `20.3685` edge `0.138` maxDD `-2.8494`
- `risk_on_high->commodity_4h` score `2.548` n `52` status `ready` deltaP `30.4057` edge `0.0446` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.548` n `52` status `ready` deltaP `30.4057` edge `0.0446` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.4477` n `149` status `ready` deltaP `26.908` edge `0.0664` maxDD `-0.345`
- `news_risk_high->fx_4h` score `1.2615` n `80` status `ready` deltaP `14.1159` edge `0.0329` maxDD `-0.084`
- `news_risk_high->fx_24h` score `1.0916` n `64` status `ready` deltaP `6.25` edge `0.0535` maxDD `-0.0029`
- `market_context_high->commodity_1h` score `1.039` n `149` status `ready` deltaP `15.4624` edge `0.0212` maxDD `-0.3491`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
