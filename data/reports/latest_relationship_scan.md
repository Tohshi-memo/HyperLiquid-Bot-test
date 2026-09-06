# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T20:22:26.963762+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10299`

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

- `risk_on_high->unknown_24h` score `281.7291` n `103` status `ready` deltaP `26.8069` edge `23.3034` maxDD `-0.0416`
- `risk_on_and_context->unknown_24h` score `281.7291` n `103` status `ready` deltaP `26.8069` edge `23.3034` maxDD `-0.0416`
- `risk_on_high->crypto_major_24h` score `20.2352` n `103` status `ready` deltaP `33.1732` edge `1.5168` maxDD `-1.4687`
- `risk_on_and_context->crypto_major_24h` score `20.2352` n `103` status `ready` deltaP `33.1732` edge `1.5168` maxDD `-1.4687`
- `risk_on_high->crypto_alt_24h` score `13.218` n `103` status `ready` deltaP `27.3665` edge `0.9397` maxDD `-0.6512`
- `risk_on_and_context->crypto_alt_24h` score `13.218` n `103` status `ready` deltaP `27.3665` edge `0.9397` maxDD `-0.6512`
- `market_context_high->crypto_alt_24h` score `7.9933` n `196` status `ready` deltaP `21.5561` edge `0.5799` maxDD `-2.5998`
- `market_context_high->equity_24h` score `6.7456` n `196` status `ready` deltaP `23.0903` edge `0.4082` maxDD `0.0`
- `risk_on_high->equity_24h` score `6.0604` n `103` status `ready` deltaP `23.0903` edge `0.3511` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `6.0604` n `103` status `ready` deltaP `23.0903` edge `0.3511` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `4.0191` n `117` status `ready` deltaP `27.3087` edge `0.288` maxDD `-9.1438`
- `risk_on_and_context->crypto_alt_4h` score `4.0191` n `117` status `ready` deltaP `27.3087` edge `0.288` maxDD `-9.1438`
- `risk_on_high->crypto_major_4h` score `2.3088` n `117` status `ready` deltaP `21.2229` edge `0.2229` maxDD `-10.759`
- `risk_on_and_context->crypto_major_4h` score `2.3088` n `117` status `ready` deltaP `21.2229` edge `0.2229` maxDD `-10.759`
- `risk_on_high->index_24h` score `2.2722` n `103` status `ready` deltaP `20.2872` edge `0.0813` maxDD `-0.5094`
- `risk_on_and_context->index_24h` score `2.2722` n `103` status `ready` deltaP `20.2872` edge `0.0813` maxDD `-0.5094`
- `market_context_high->index_24h` score `2.0012` n `196` status `ready` deltaP `19.9404` edge `0.0924` maxDD `-1.0188`
- `risk_on_high->metal_24h` score `0.8124` n `103` status `ready` deltaP `14.7013` edge `0.1019` maxDD `-2.6605`
- `risk_on_and_context->metal_24h` score `0.8124` n `103` status `ready` deltaP `14.7013` edge `0.1019` maxDD `-2.6605`
- `risk_on_high->crypto_alt_1h` score `0.7788` n `129` status `ready` deltaP `4.4771` edge `0.0836` maxDD `-2.2169`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
