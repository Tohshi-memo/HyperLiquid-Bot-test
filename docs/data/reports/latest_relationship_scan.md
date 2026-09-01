# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-01T06:52:30.784312+00:00`
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

- `risk_on_high->unknown_4h` score `7.3481` n `107` status `ready` deltaP `21.4398` edge `0.5312` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.3481` n `107` status `ready` deltaP `21.4398` edge `0.5312` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `5.8946` n `151` status `ready` deltaP `17.7324` edge `0.4425` maxDD `-2.5597`
- `risk_on_high->unknown_1h` score `2.2281` n `107` status `ready` deltaP `5.3179` edge `0.2079` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `2.2281` n `107` status `ready` deltaP `5.3179` edge `0.2079` maxDD `-1.9475`
- `market_context_high->unknown_1h` score `2.0973` n `151` status `ready` deltaP `4.6804` edge `0.2066` maxDD `-2.042`
- `news_risk_high->unknown_1h` score `1.3221` n `61` status `ready` deltaP `2.4222` edge `0.1287` maxDD `-1.1072`
- `risk_on_high->commodity_24h` score `1.0806` n `107` status `ready` deltaP `11.5574` edge `0.1118` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `1.0806` n `107` status `ready` deltaP `11.5574` edge `0.1118` maxDD `-0.5706`
- `market_context_high->commodity_24h` score `0.4846` n `151` status `ready` deltaP `10.926` edge `0.0871` maxDD `-1.2314`
- `risk_on_high->crypto_alt_24h` score `0.3344` n `107` status `ready` deltaP `12.5763` edge `0.6494` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `0.3344` n `107` status `ready` deltaP `12.5763` edge `0.6494` maxDD `-42.8959`
- `news_risk_high->fx_4h` score `0.1669` n `61` status `ready` deltaP `10.8057` edge `0.0012` maxDD `-0.7461`
- `market_context_high->commodity_1h` score `0.0334` n `151` status `ready` deltaP `7.9738` edge `0.0146` maxDD `-1.5315`
- `risk_on_high->index_1h` score `0.006` n `107` status `ready` deltaP `6.7463` edge `0.0003` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.006` n `107` status `ready` deltaP `6.7463` edge `0.0003` maxDD `-0.5605`
- `news_risk_high->commodity_4h` score `-0.0124` n `61` status `ready` deltaP `3.9859` edge `0.0135` maxDD `-1.3325`
- `risk_on_high->fx_24h` score `-0.0285` n `107` status `ready` deltaP `36.2977` edge `0.0241` maxDD `-4.2453`
- `risk_on_and_context->fx_24h` score `-0.0285` n `107` status `ready` deltaP `36.2977` edge `0.0241` maxDD `-4.2453`
- `risk_on_high->commodity_1h` score `-0.0516` n `107` status `ready` deltaP `4.873` edge `0.0131` maxDD `-0.8428`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
