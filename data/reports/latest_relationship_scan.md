# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-13T07:22:31.131678+00:00`
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

- `news_risk_high->equity_4h` score `6.8778` n `36` status `ready` deltaP `37.0427` edge `0.3262` maxDD `0.0`
- `risk_on_high->commodity_24h` score `2.8525` n `32` status `ready` deltaP `22.3958` edge `0.0884` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `2.8525` n `32` status `ready` deltaP `22.3958` edge `0.0884` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.2635` n `32` status `ready` deltaP `15.625` edge `0.1027` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.2635` n `32` status `ready` deltaP `15.625` edge `0.1027` maxDD `-0.1258`
- `risk_on_high->fx_24h` score `2.0688` n `32` status `ready` deltaP `23.0903` edge `0.0369` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `2.0688` n `32` status `ready` deltaP `23.0903` edge `0.0369` maxDD `-0.1418`
- `news_risk_high->index_4h` score `1.8947` n `36` status `ready` deltaP `21.5955` edge `0.0271` maxDD `-0.0546`
- `risk_on_high->crypto_major_24h` score `1.6095` n `32` status `ready` deltaP `14.0625` edge `0.2282` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `1.6095` n `32` status `ready` deltaP `14.0625` edge `0.2282` maxDD `-6.2481`
- `news_risk_high->equity_1h` score `1.5308` n `36` status `ready` deltaP `7.535` edge `0.1092` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.1005` n `32` status `ready` deltaP `12.0135` edge `0.0349` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.1005` n `32` status `ready` deltaP `12.0135` edge `0.0349` maxDD `-0.1957`
- `market_context_high->commodity_4h` score `1.082` n `161` status `ready` deltaP `13.2764` edge `0.0655` maxDD `-2.1077`
- `risk_on_high->fx_4h` score `0.9147` n `32` status `ready` deltaP `10.5945` edge `0.0197` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `0.9147` n `32` status `ready` deltaP `10.5945` edge `0.0197` maxDD `-0.1285`
- `market_context_high->commodity_24h` score `0.8835` n `161` status `ready` deltaP `12.4579` edge `0.0709` maxDD `-2.4263`
- `market_context_high->commodity_1h` score `0.8266` n `161` status `ready` deltaP `10.3442` edge `0.0296` maxDD `-0.3742`
- `risk_on_high->index_1h` score `0.2112` n `32` status `ready` deltaP `8.6078` edge `0.0072` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.2112` n `32` status `ready` deltaP `8.6078` edge `0.0072` maxDD `-0.3343`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
