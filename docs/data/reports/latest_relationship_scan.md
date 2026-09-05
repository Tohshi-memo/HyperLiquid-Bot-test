# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-05T16:00:28.935145+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10525`

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

- `risk_on_high->unknown_4h` score `21.5127` n `140` status `ready` deltaP `1.2979` edge `1.8878` maxDD `-2.9648`
- `risk_on_and_context->unknown_4h` score `21.5127` n `140` status `ready` deltaP `1.2979` edge `1.8878` maxDD `-2.9648`
- `market_context_high->unknown_4h` score `9.8257` n `228` status `ready` deltaP `3.942` edge `0.9139` maxDD `-3.3761`
- `news_risk_high->crypto_alt_24h` score `7.1579` n `37` status `ready` deltaP `25.1783` edge `0.4556` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `3.7805` n `37` status `ready` deltaP `19.7917` edge `0.1831` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.5778` n `37` status `ready` deltaP `17.1803` edge `0.2249` maxDD `-0.9693`
- `news_risk_high->metal_4h` score `2.3807` n `37` status `ready` deltaP `24.1513` edge `0.0595` maxDD `-0.7692`
- `news_risk_high->commodity_4h` score `1.8461` n `37` status `ready` deltaP `10.8191` edge `0.1018` maxDD `-0.2737`
- `news_risk_high->equity_1h` score `1.3221` n `37` status `ready` deltaP `11.1305` edge `0.0834` maxDD `-0.7941`
- `news_risk_high->metal_1h` score `1.2598` n `37` status `ready` deltaP `15.0146` edge `0.0242` maxDD `-0.2118`
- `news_risk_high->crypto_major_1h` score `1.2146` n `37` status `ready` deltaP `6.4655` edge `0.0764` maxDD `-0.4628`
- `news_risk_high->index_1h` score `1.1622` n `37` status `ready` deltaP `14.5736` edge `0.0131` maxDD `-0.0724`
- `market_context_high->equity_24h` score `1.1536` n `181` status `ready` deltaP `15.1003` edge `0.4411` maxDD `-20.984`
- `news_risk_high->crypto_alt_1h` score `1.0232` n `37` status `ready` deltaP `9.6254` edge `0.0476` maxDD `-0.7867`
- `news_risk_high->crypto_major_24h` score `0.9133` n `37` status `ready` deltaP `16.5776` edge `0.2842` maxDD `-18.2098`
- `news_risk_high->crypto_alt_4h` score `0.5849` n `37` status `ready` deltaP `5.941` edge `0.042` maxDD `-1.296`
- `news_risk_high->fx_24h` score `0.5581` n `37` status `ready` deltaP `15.7892` edge `0.0428` maxDD `-3.1244`
- `news_risk_high->commodity_1h` score `-0.0332` n `37` status `ready` deltaP `5.5754` edge `0.0032` maxDD `-0.9036`
- `risk_on_high->index_1h` score `-0.0527` n `149` status `ready` deltaP `6.0664` edge `-0.0025` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `-0.0527` n `149` status `ready` deltaP `6.0664` edge `-0.0025` maxDD `-0.5764`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
