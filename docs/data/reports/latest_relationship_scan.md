# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-01T02:07:27.784848+00:00`
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

- `risk_on_high->unknown_4h` score `7.5916` n `107` status `ready` deltaP `23.2691` edge `0.5393` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.5916` n `107` status `ready` deltaP `23.2691` edge `0.5393` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `6.0615` n `156` status `ready` deltaP `19.5787` edge `0.4441` maxDD `-2.5597`
- `risk_on_high->unknown_1h` score `2.0314` n `107` status `ready` deltaP `4.8688` edge `0.1945` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `2.0314` n `107` status `ready` deltaP `4.8688` edge `0.1945` maxDD `-1.9475`
- `market_context_high->unknown_1h` score `1.8979` n `156` status `ready` deltaP `4.1379` edge `0.1936` maxDD `-2.042`
- `risk_on_high->commodity_24h` score `1.6536` n `101` status `ready` deltaP `13.6345` edge `0.1457` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `1.6536` n `101` status `ready` deltaP `13.6345` edge `0.1457` maxDD `-0.5706`
- `news_risk_high->unknown_1h` score `1.1254` n `61` status `ready` deltaP `1.9731` edge `0.1153` maxDD `-1.1072`
- `risk_on_high->crypto_alt_24h` score `0.9586` n `101` status `ready` deltaP `13.7651` edge `0.7215` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `0.9586` n `101` status `ready` deltaP `13.7651` edge `0.7215` maxDD `-42.8959`
- `risk_on_high->fx_24h` score `0.2817` n `101` status `ready` deltaP `38.3096` edge `0.0235` maxDD `-4.0896`
- `risk_on_and_context->fx_24h` score `0.2817` n `101` status `ready` deltaP `38.3096` edge `0.0235` maxDD `-4.0896`
- `news_risk_high->commodity_4h` score `0.1696` n `61` status `ready` deltaP `6.1201` edge `0.0226` maxDD `-1.3325`
- `news_risk_high->fx_4h` score `0.1353` n `61` status `ready` deltaP `10.5008` edge `0.0006` maxDD `-0.7461`
- `market_context_high->commodity_1h` score `0.1038` n `156` status `ready` deltaP `8.6289` edge `0.0161` maxDD `-1.5315`
- `risk_on_high->commodity_1h` score `-0.0002` n `107` status `ready` deltaP `5.6215` edge `0.0147` maxDD `-0.8428`
- `risk_on_and_context->commodity_1h` score `-0.0002` n `107` status `ready` deltaP `5.6215` edge `0.0147` maxDD `-0.8428`
- `market_context_high->commodity_24h` score `-0.0333` n `150` status `ready` deltaP `10.75` edge `0.0839` maxDD `-4.3342`
- `risk_on_high->index_1h` score `-0.0633` n `107` status `ready` deltaP `5.5487` edge `-0.0006` maxDD `-0.5605`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
