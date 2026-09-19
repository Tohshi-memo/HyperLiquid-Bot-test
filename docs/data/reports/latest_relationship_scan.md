# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T07:52:32.883926+00:00`
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

- `news_risk_high->crypto_major_24h` score `56.6258` n `68` status `ready` deltaP `35.6107` edge `4.5706` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `49.7383` n `68` status `ready` deltaP `39.1749` edge `4.0216` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `34.4825` n `149` status `ready` deltaP `-1.8354` edge `2.9091` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `12.1616` n `68` status `ready` deltaP `45.4044` edge `0.715` maxDD `-0.0053`
- `risk_on_high->unknown_4h` score `8.3611` n `52` status `ready` deltaP `-9.076` edge `0.7798` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `8.3611` n `52` status `ready` deltaP `-9.076` edge `0.7798` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.2448` n `52` status `ready` deltaP `44.9653` edge `0.3873` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.2448` n `52` status `ready` deltaP `44.9653` edge `0.3873` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.9457` n `149` status `ready` deltaP `38.2539` edge `0.3763` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `6.6901` n `81` status `ready` deltaP `22.7925` edge `0.5265` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.5617` n `81` status `ready` deltaP `19.6834` edge `0.3747` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `3.3909` n `81` status `ready` deltaP `17.7497` edge `0.2108` maxDD `-2.058`
- `news_risk_high->metal_24h` score `2.7354` n `68` status `ready` deltaP `27.8493` edge `0.098` maxDD `-1.457`
- `news_risk_high->crypto_major_1h` score `2.712` n `81` status `ready` deltaP `20.8176` edge `0.1395` maxDD `-2.8494`
- `risk_on_high->commodity_4h` score `2.6027` n `52` status `ready` deltaP `31.0155` edge `0.0451` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.6027` n `52` status `ready` deltaP `31.0155` edge `0.0451` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.5025` n `149` status `ready` deltaP `27.5178` edge `0.0669` maxDD `-0.345`
- `news_risk_high->fx_4h` score `1.296` n `81` status `ready` deltaP `14.6078` edge `0.0325` maxDD `-0.084`
- `market_context_high->commodity_1h` score `1.0378` n `149` status `ready` deltaP `15.4624` edge `0.0211` maxDD `-0.3491`
- `news_risk_high->fx_24h` score `0.9714` n `68` status `ready` deltaP `5.6475` edge `0.0475` maxDD `-0.0029`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
