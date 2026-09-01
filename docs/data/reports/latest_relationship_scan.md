# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-01T02:22:22.315208+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11496`

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

- `risk_on_high->unknown_4h` score `7.588` n `107` status `ready` deltaP `23.2691` edge `0.539` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.588` n `107` status `ready` deltaP `23.2691` edge `0.539` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `6.0305` n `155` status `ready` deltaP `19.4463` edge `0.4424` maxDD `-2.5597`
- `risk_on_high->unknown_1h` score `2.0146` n `107` status `ready` deltaP `4.7191` edge `0.1941` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `2.0146` n `107` status `ready` deltaP `4.7191` edge `0.1941` maxDD `-1.9475`
- `market_context_high->unknown_1h` score `1.958` n `155` status `ready` deltaP `4.3935` edge `0.1969` maxDD `-2.042`
- `risk_on_high->commodity_24h` score `1.6388` n `102` status `ready` deltaP `13.6745` edge `0.1442` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `1.6388` n `102` status `ready` deltaP `13.6745` edge `0.1442` maxDD `-0.5706`
- `news_risk_high->unknown_1h` score `1.1086` n `61` status `ready` deltaP `1.8234` edge `0.1149` maxDD `-1.1072`
- `risk_on_high->crypto_alt_24h` score `1.007` n `102` status `ready` deltaP `13.9604` edge `0.7264` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `1.007` n `102` status `ready` deltaP `13.9604` edge `0.7264` maxDD `-42.8959`
- `risk_on_high->fx_24h` score `0.2263` n `102` status `ready` deltaP `37.9494` edge `0.0235` maxDD `-4.1325`
- `risk_on_and_context->fx_24h` score `0.2263` n `102` status `ready` deltaP `37.9494` edge `0.0235` maxDD `-4.1325`
- `market_context_high->commodity_24h` score `0.1982` n `150` status `ready` deltaP `11.2431` edge `0.0896` maxDD `-3.5095`
- `news_risk_high->commodity_4h` score `0.1593` n `61` status `ready` deltaP `5.9676` edge `0.0223` maxDD `-1.3325`
- `news_risk_high->fx_4h` score `0.1365` n `61` status `ready` deltaP `10.5008` edge `0.0007` maxDD `-0.7461`
- `market_context_high->commodity_1h` score `0.0918` n `155` status `ready` deltaP `8.5387` edge `0.0157` maxDD `-1.5315`
- `risk_on_high->commodity_1h` score `0.0091` n `107` status `ready` deltaP `5.7712` edge `0.0149` maxDD `-0.8428`
- `risk_on_and_context->commodity_1h` score `0.0091` n `107` status `ready` deltaP `5.7712` edge `0.0149` maxDD `-0.8428`
- `risk_on_high->index_1h` score `-0.0547` n `107` status `ready` deltaP `5.6984` edge `-0.0005` maxDD `-0.5605`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
