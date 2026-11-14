# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-14T23:21:35.708702+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `9354`

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

- `market_context_high->unknown_24h` score `573.3249` n `66` status `ready` deltaP `2.9514` edge `47.7574` maxDD `0.0`
- `news_risk_high->equity_24h` score `40.9758` n `53` status `ready` deltaP `44.9522` edge `3.1856` maxDD `-3.6503`
- `market_context_high->equity_24h` score `37.2222` n `66` status `ready` deltaP `39.9779` edge `2.9895` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `27.5354` n `66` status `ready` deltaP `57.7652` edge `2.0172` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `19.9296` n `53` status `ready` deltaP `43.0851` edge `2.4644` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.8123` n `53` status `ready` deltaP `38.8316` edge `0.8385` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `7.348` n `53` status `ready` deltaP `51.2153` edge `0.2709` maxDD `0.0`
- `market_context_high->index_24h` score `7.2344` n `66` status `ready` deltaP `42.077` edge `0.3315` maxDD `-0.0653`
- `news_risk_high->index_24h` score `5.8764` n `53` status `ready` deltaP `38.332` edge `0.2645` maxDD `-0.4279`
- `news_risk_high->crypto_major_4h` score `5.806` n `53` status `ready` deltaP `22.5725` edge `0.4821` maxDD `-9.2335`
- `market_context_high->metal_24h` score `5.3889` n `66` status `ready` deltaP `51.5152` edge `0.4366` maxDD `-3.7989`
- `news_risk_high->crypto_alt_24h` score `5.0568` n `53` status `ready` deltaP `14.4261` edge `1.0027` maxDD `-29.0448`
- `news_risk_high->metal_4h` score `5.0557` n `53` status `ready` deltaP `46.701` edge `0.1476` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `3.8369` n `53` status `ready` deltaP `20.7095` edge `0.2447` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.4998` n `53` status `ready` deltaP `32.5041` edge `0.1003` maxDD `-0.3611`
- `news_risk_high->crypto_alt_4h` score `3.3747` n `53` status `ready` deltaP `28.0229` edge `0.4097` maxDD `-10.1088`
- `news_risk_high->index_4h` score `2.534` n `53` status `ready` deltaP `26.2339` edge `0.0799` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `2.2626` n `53` status `ready` deltaP `26.0394` edge `0.0404` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.4023` n `53` status `ready` deltaP `18.673` edge `0.0225` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `1.2083` n `53` status `ready` deltaP `20.2886` edge `0.1176` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
