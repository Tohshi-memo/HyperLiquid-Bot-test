# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-01T17:52:26.155509+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11475`

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

- `risk_on_high->unknown_4h` score `7.2925` n `107` status `ready` deltaP `20.2203` edge `0.5347` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.2925` n `107` status `ready` deltaP `20.2203` edge `0.5347` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `5.8391` n `151` status `ready` deltaP `16.5129` edge `0.446` maxDD `-2.5597`
- `risk_on_high->unknown_1h` score `2.0747` n `107` status `ready` deltaP `4.27` edge `0.2021` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `2.0747` n `107` status `ready` deltaP `4.27` edge `0.2021` maxDD `-1.9475`
- `market_context_high->unknown_1h` score `1.9439` n `151` status `ready` deltaP `3.6325` edge `0.2008` maxDD `-2.042`
- `news_risk_high->unknown_1h` score `1.3644` n `59` status `ready` deltaP `1.7355` edge `0.1368` maxDD `-1.1072`
- `news_risk_high->fx_4h` score `0.1891` n `59` status `ready` deltaP `11.0971` edge `0.0011` maxDD `-0.7461`
- `risk_on_high->commodity_24h` score `0.1666` n `107` status `ready` deltaP `6.5226` edge `0.0692` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `0.1666` n `107` status `ready` deltaP `6.5226` edge `0.0692` maxDD `-0.5706`
- `risk_on_high->index_1h` score `0.08` n `107` status `ready` deltaP `7.7942` edge `0.0028` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.08` n `107` status `ready` deltaP `7.7942` edge `0.0028` maxDD `-0.5605`
- `risk_on_high->metal_1h` score `0.0305` n `107` status `ready` deltaP `11.0471` edge `0.0015` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0305` n `107` status `ready` deltaP `11.0471` edge `0.0015` maxDD `-1.699`
- `risk_on_high->index_4h` score `-0.0789` n `107` status `ready` deltaP `17.8867` edge `0.0037` maxDD `-3.6448`
- `risk_on_and_context->index_4h` score `-0.0789` n `107` status `ready` deltaP `17.8867` edge `0.0037` maxDD `-3.6448`
- `market_context_high->commodity_1h` score `-0.0793` n `151` status `ready` deltaP `7.375` edge `0.0092` maxDD `-1.5315`
- `news_risk_high->commodity_24h` score `-0.0816` n `59` status `ready` deltaP `3.3545` edge `-0.0099` maxDD `-0.2074`
- `news_risk_high->commodity_4h` score `-0.0833` n `59` status `ready` deltaP `2.6147` edge `0.0078` maxDD `-0.8733`
- `risk_on_high->commodity_1h` score `-0.1249` n `107` status `ready` deltaP `4.2742` edge `0.0077` maxDD `-0.8428`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
