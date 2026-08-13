# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-13T07:07:28.865185+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11712`

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

- `news_risk_high->equity_4h` score `6.844` n `36` status `ready` deltaP `36.8902` edge `0.3244` maxDD `0.0`
- `risk_on_high->commodity_24h` score `2.8242` n `32` status `ready` deltaP `22.2222` edge `0.0872` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `2.8242` n `32` status `ready` deltaP `22.2222` edge `0.0872` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.2781` n `32` status `ready` deltaP `15.7774` edge `0.1029` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.2781` n `32` status `ready` deltaP `15.7774` edge `0.1029` maxDD `-0.1258`
- `risk_on_high->fx_24h` score `2.0537` n `32` status `ready` deltaP `22.9167` edge `0.0368` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `2.0537` n `32` status `ready` deltaP `22.9167` edge `0.0368` maxDD `-0.1418`
- `news_risk_high->index_4h` score `1.8801` n `36` status `ready` deltaP `21.4431` edge `0.0269` maxDD `-0.0546`
- `risk_on_high->crypto_major_24h` score `1.6373` n `32` status `ready` deltaP `14.2361` edge `0.2306` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `1.6373` n `32` status `ready` deltaP `14.2361` edge `0.2306` maxDD `-6.2481`
- `news_risk_high->equity_1h` score `1.508` n `36` status `ready` deltaP `7.3853` edge `0.1083` maxDD `-0.5496`
- `market_context_high->commodity_4h` score `1.0965` n `161` status `ready` deltaP `13.4288` edge `0.0657` maxDD `-2.1077`
- `risk_on_high->commodity_1h` score `1.0873` n `32` status `ready` deltaP `11.8638` edge `0.0348` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.0873` n `32` status `ready` deltaP `11.8638` edge `0.0348` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `0.9147` n `32` status `ready` deltaP `10.5945` edge `0.0197` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `0.9147` n `32` status `ready` deltaP `10.5945` edge `0.0197` maxDD `-0.1285`
- `market_context_high->commodity_24h` score `0.8552` n `161` status `ready` deltaP `12.2843` edge `0.0697` maxDD `-2.4263`
- `market_context_high->commodity_1h` score `0.8134` n `161` status `ready` deltaP `10.1945` edge `0.0295` maxDD `-0.3742`
- `risk_on_high->index_1h` score `0.2112` n `32` status `ready` deltaP `8.6078` edge `0.0072` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.2112` n `32` status `ready` deltaP `8.6078` edge `0.0072` maxDD `-0.3343`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
