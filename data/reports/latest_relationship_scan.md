# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T22:07:31.791182+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8098`

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

- `news_risk_high->crypto_major_24h` score `46.2215` n `39` status `ready` deltaP `25.1069` edge `3.7736` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `43.9753` n `39` status `ready` deltaP `33.7073` edge `3.5778` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `37.7032` n `149` status `ready` deltaP `-0.9208` edge `3.1714` maxDD `-0.5326`
- `risk_on_high->unknown_4h` score `11.5819` n `52` status `ready` deltaP `-8.1614` edge `1.0421` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `11.5819` n `52` status `ready` deltaP `-8.1614` edge `1.0421` maxDD `-0.4694`
- `news_risk_high->equity_24h` score `9.0168` n `39` status `ready` deltaP `32.9594` edge `0.5914` maxDD `-2.1119`
- `news_risk_high->crypto_alt_4h` score `8.9429` n `80` status `ready` deltaP `29.4817` edge `0.6613` maxDD `-7.675`
- `risk_on_high->commodity_24h` score `8.5817` n `52` status `ready` deltaP `47.9167` edge `0.3957` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.5817` n `52` status `ready` deltaP `47.9167` edge `0.3957` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.2826` n `149` status `ready` deltaP `41.2053` edge `0.3847` maxDD `-0.8682`
- `news_risk_high->crypto_major_4h` score `5.1261` n `80` status `ready` deltaP `21.7683` edge `0.3995` maxDD `-8.0625`
- `risk_on_high->commodity_4h` score `2.8429` n `52` status `ready` deltaP `32.9972` edge `0.0519` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.8429` n `52` status `ready` deltaP `32.9972` edge `0.0519` maxDD `-0.1313`
- `news_risk_high->metal_24h` score `2.7541` n `39` status `ready` deltaP `20.0588` edge `0.1199` maxDD `-0.2629`
- `market_context_high->commodity_4h` score `2.7426` n `149` status `ready` deltaP `29.4995` edge `0.0737` maxDD `-0.345`
- `news_risk_high->crypto_alt_1h` score `2.515` n `80` status `ready` deltaP `14.1617` edge `0.162` maxDD `-2.0799`
- `news_risk_high->crypto_major_1h` score `2.0513` n `80` status `ready` deltaP `17.6123` edge `0.112` maxDD `-3.0111`
- `news_risk_high->equity_4h` score `1.7636` n `80` status `ready` deltaP `15.5793` edge `0.1331` maxDD `-4.1995`
- `news_risk_high->fx_4h` score `1.2919` n `80` status `ready` deltaP `14.4207` edge `0.0334` maxDD `-0.084`
- `market_context_high->commodity_1h` score `1.1217` n `149` status `ready` deltaP `16.2109` edge `0.0231` maxDD `-0.3491`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
