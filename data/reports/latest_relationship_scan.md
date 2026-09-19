# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T01:07:28.564692+00:00`
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

- `news_risk_high->crypto_major_24h` score `62.7835` n `43` status `ready` deltaP `33.2324` edge `5.0996` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `57.5287` n `43` status `ready` deltaP `34.8999` edge `4.6993` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `36.9611` n `149` status `ready` deltaP `-1.3781` edge `3.1126` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `15.2915` n `43` status `ready` deltaP `51.3889` edge `0.9317` maxDD `0.0`
- `risk_on_high->unknown_4h` score `10.8397` n `52` status `ready` deltaP `-8.6187` edge `0.9833` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `10.8397` n `52` status `ready` deltaP `-8.6187` edge `0.9833` maxDD `-0.4694`
- `news_risk_high->crypto_alt_4h` score `8.9044` n `72` status `ready` deltaP `28.3706` edge `0.6655` maxDD `-7.675`
- `risk_on_high->commodity_24h` score `8.4557` n `52` status `ready` deltaP `46.7014` edge `0.3933` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.4557` n `52` status `ready` deltaP `46.7014` edge `0.3933` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.1566` n `149` status `ready` deltaP `39.99` edge `0.3823` maxDD `-0.8682`
- `news_risk_high->crypto_major_4h` score `6.1333` n `72` status `ready` deltaP `25.254` edge `0.4602` maxDD `-8.0625`
- `news_risk_high->metal_24h` score `4.8606` n `43` status `ready` deltaP `35.4207` edge `0.1847` maxDD `-0.2629`
- `news_risk_high->crypto_alt_1h` score `3.1792` n `72` status `ready` deltaP `17.4734` edge `0.195` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.8629` n `72` status `ready` deltaP `21.9395` edge `0.1446` maxDD `-2.8494`
- `risk_on_high->commodity_4h` score `2.6959` n `52` status `ready` deltaP `31.6252` edge `0.0488` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.6959` n `52` status `ready` deltaP `31.6252` edge `0.0488` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.5956` n `149` status `ready` deltaP `28.1275` edge `0.0706` maxDD `-0.345`
- `news_risk_high->fx_24h` score `1.8382` n `43` status `ready` deltaP `9.1327` edge `0.0965` maxDD `-0.0029`
- `news_risk_high->equity_4h` score `1.5403` n `72` status `ready` deltaP `12.3984` edge `0.1357` maxDD `-4.1995`
- `news_risk_high->fx_4h` score `1.4873` n `72` status `ready` deltaP `16.1585` edge `0.0381` maxDD `-0.084`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
