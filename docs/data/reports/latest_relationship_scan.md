# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-01T07:52:24.937587+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11438`

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

- `risk_on_high->unknown_4h` score `7.2765` n `107` status `ready` deltaP `20.83` edge `0.5293` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.2765` n `107` status `ready` deltaP `20.83` edge `0.5293` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `5.8231` n `151` status `ready` deltaP `17.1226` edge `0.4406` maxDD `-2.5597`
- `risk_on_high->unknown_1h` score `2.179` n `107` status `ready` deltaP `4.8688` edge `0.2068` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `2.179` n `107` status `ready` deltaP `4.8688` edge `0.2068` maxDD `-1.9475`
- `market_context_high->unknown_1h` score `2.0482` n `151` status `ready` deltaP `4.2313` edge `0.2055` maxDD `-2.042`
- `news_risk_high->unknown_1h` score `1.273` n `61` status `ready` deltaP `1.9731` edge `0.1276` maxDD `-1.1072`
- `risk_on_high->commodity_24h` score `0.9314` n `107` status `ready` deltaP `10.8629` edge `0.104` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `0.9314` n `107` status `ready` deltaP `10.8629` edge `0.104` maxDD `-0.5706`
- `market_context_high->commodity_24h` score `0.3354` n `151` status `ready` deltaP `10.2315` edge `0.0793` maxDD `-1.2314`
- `news_risk_high->fx_4h` score `0.1535` n `61` status `ready` deltaP `10.6533` edge `0.0011` maxDD `-0.7461`
- `risk_on_high->crypto_alt_24h` score `0.0799` n `107` status `ready` deltaP `11.8818` edge `0.6214` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `0.0799` n `107` status `ready` deltaP `11.8818` edge `0.6214` maxDD `-42.8959`
- `market_context_high->commodity_1h` score `0.0166` n `151` status `ready` deltaP `7.8241` edge `0.0142` maxDD `-1.5315`
- `risk_on_high->index_1h` score `0.0068` n `107` status `ready` deltaP `6.7463` edge `0.0004` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.0068` n `107` status `ready` deltaP `6.7463` edge `0.0004` maxDD `-0.5605`
- `risk_on_high->fx_24h` score `-0.0594` n `107` status `ready` deltaP `35.7769` edge `0.0236` maxDD `-4.2453`
- `risk_on_and_context->fx_24h` score `-0.0594` n `107` status `ready` deltaP `35.7769` edge `0.0236` maxDD `-4.2453`
- `risk_on_high->commodity_1h` score `-0.0625` n `107` status `ready` deltaP `4.7233` edge `0.0127` maxDD `-0.8428`
- `risk_on_and_context->commodity_1h` score `-0.0625` n `107` status `ready` deltaP `4.7233` edge `0.0127` maxDD `-0.8428`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
