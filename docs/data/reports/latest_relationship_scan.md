# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T03:22:36.985321+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9134`

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

- `news_risk_high->crypto_major_24h` score `40.4006` n `81` status `ready` deltaP `16.2423` edge `3.4252` maxDD `-10.3413`
- `news_risk_high->crypto_alt_24h` score `37.4723` n `81` status `ready` deltaP `29.2052` edge `3.0659` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `27.5771` n `91` status `ready` deltaP `-2.573` edge `2.3344` maxDD `-0.5326`
- `market_context_high->commodity_24h` score `7.5993` n `89` status `ready` deltaP `38.0696` edge `0.432` maxDD `-0.8682`
- `news_risk_high->equity_24h` score `6.514` n `81` status `ready` deltaP `33.2755` edge `0.3346` maxDD `-0.4217`
- `news_risk_high->crypto_alt_4h` score `6.0452` n `98` status `ready` deltaP `23.2951` edge `0.4694` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.7388` n `98` status `ready` deltaP `23.1427` edge `0.3664` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `3.9056` n `91` status `ready` deltaP `35.5937` edge `0.1015` maxDD `-0.0659`
- `news_risk_high->crypto_alt_1h` score `3.3828` n `98` status `ready` deltaP `18.9234` edge `0.2023` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.6345` n `98` status `ready` deltaP `21.3186` edge `0.1297` maxDD `-2.8494`
- `market_context_high->commodity_1h` score `1.954` n `92` status `ready` deltaP `22.4942` edge `0.0339` maxDD `-0.3491`
- `news_risk_high->metal_24h` score `1.4863` n `81` status `ready` deltaP `22.3765` edge `0.0591` maxDD `-2.4203`
- `market_context_high->fx_4h` score `1.3078` n `91` status `ready` deltaP `22.2611` edge `0.0032` maxDD `-0.0768`
- `news_risk_high->metal_4h` score `0.8698` n `98` status `ready` deltaP `19.7393` edge `0.0463` maxDD `-2.0994`
- `market_context_high->fx_24h` score `0.7728` n `89` status `ready` deltaP `12.7653` edge `-0.0165` maxDD `-0.0027`
- `news_risk_high->metal_1h` score `0.7315` n `98` status `ready` deltaP `15.7552` edge `0.0161` maxDD `-0.8144`
- `market_context_high->fx_1h` score `0.4354` n `92` status `ready` deltaP `8.8909` edge `0.0028` maxDD `-0.063`
- `news_risk_high->equity_1h` score `0.3899` n `98` status `ready` deltaP `6.2172` edge `0.0316` maxDD `-0.9112`
- `news_risk_high->commodity_24h` score `0.2639` n `81` status `ready` deltaP `17.2068` edge `0.0497` maxDD `-3.4467`
- `news_risk_high->fx_4h` score `-0.0683` n `98` status `ready` deltaP `5.3851` edge `0.022` maxDD `-0.421`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
