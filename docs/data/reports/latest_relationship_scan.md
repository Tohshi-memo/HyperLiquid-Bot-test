# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-01T07:22:32.631883+00:00`
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

- `risk_on_high->unknown_4h` score `7.3105` n `107` status `ready` deltaP `21.1349` edge `0.5301` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.3105` n `107` status `ready` deltaP `21.1349` edge `0.5301` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `5.857` n `151` status `ready` deltaP `17.4275` edge `0.4414` maxDD `-2.5597`
- `risk_on_high->unknown_1h` score `2.1982` n `107` status `ready` deltaP `5.0185` edge `0.2074` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `2.1982` n `107` status `ready` deltaP `5.0185` edge `0.2074` maxDD `-1.9475`
- `market_context_high->unknown_1h` score `2.0674` n `151` status `ready` deltaP `4.381` edge `0.2061` maxDD `-2.042`
- `news_risk_high->unknown_1h` score `1.2921` n `61` status `ready` deltaP `2.1228` edge `0.1282` maxDD `-1.1072`
- `risk_on_high->commodity_24h` score `1.0072` n `107` status `ready` deltaP `11.2101` edge `0.108` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `1.0072` n `107` status `ready` deltaP `11.2101` edge `0.108` maxDD `-0.5706`
- `market_context_high->commodity_24h` score `0.4112` n `151` status `ready` deltaP `10.5787` edge `0.0833` maxDD `-1.2314`
- `risk_on_high->crypto_alt_24h` score `0.2009` n `107` status `ready` deltaP `12.2291` edge `0.6346` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `0.2009` n `107` status `ready` deltaP `12.2291` edge `0.6346` maxDD `-42.8959`
- `news_risk_high->fx_4h` score `0.1669` n `61` status `ready` deltaP `10.8057` edge `0.0012` maxDD `-0.7461`
- `market_context_high->commodity_1h` score `0.0322` n `151` status `ready` deltaP `7.9738` edge `0.0145` maxDD `-1.5315`
- `risk_on_high->index_1h` score `0.0068` n `107` status `ready` deltaP `6.7463` edge `0.0004` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.0068` n `107` status `ready` deltaP `6.7463` edge `0.0004` maxDD `-0.5605`
- `news_risk_high->commodity_4h` score `-0.0383` n `61` status `ready` deltaP `3.681` edge `0.0122` maxDD `-1.3325`
- `risk_on_high->fx_24h` score `-0.039` n `107` status `ready` deltaP `36.1241` edge `0.0239` maxDD `-4.2453`
- `risk_on_and_context->fx_24h` score `-0.039` n `107` status `ready` deltaP `36.1241` edge `0.0239` maxDD `-4.2453`
- `risk_on_high->commodity_1h` score `-0.0524` n `107` status `ready` deltaP `4.873` edge `0.013` maxDD `-0.8428`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
