# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T12:06:11.909244+00:00`
- Price records: `672`
- Market context records: `1629`
- Flow alert records: `6596`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8824`

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

- `market_context_high->metal_24h` score `10.3346` n `186` status `ready` deltaP `26.6129` edge `0.9264` maxDD `-12.7414`
- `market_context_high->index_24h` score `3.1848` n `186` status `ready` deltaP `18.75` edge `0.2782` maxDD `-5.3574`
- `market_context_high->equity_4h` score `1.4316` n `186` status `ready` deltaP `11.8132` edge `0.15` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `1.1332` n `186` status `ready` deltaP `15.6636` edge `0.3252` maxDD `-17.7476`
- `market_context_high->crypto_major_4h` score `0.5288` n `186` status `ready` deltaP `11.4427` edge `0.2624` maxDD `-13.3376`
- `market_context_high->equity_24h` score `0.4386` n `186` status `ready` deltaP `17.2939` edge `0.4111` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `-0.2061` n `196` status `ready` deltaP `2.1355` edge `0.0617` maxDD `-4.1892`
- `market_context_high->fx_24h` score `-0.297` n `186` status `ready` deltaP `7.5829` edge `0.0296` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.4791` n `196` status `ready` deltaP `1.6987` edge `0.0296` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.6615` n `196` status `ready` deltaP `0.5622` edge `0.0043` maxDD `-1.7205`
- `market_context_high->index_4h` score `-0.8432` n `186` status `ready` deltaP `0.2901` edge `0.0367` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `-0.8588` n `196` status `ready` deltaP `-0.9593` edge `0.0294` maxDD `-5.9819`
- `market_context_high->fx_1h` score `-0.8638` n `196` status `ready` deltaP `-0.8035` edge `-0.0034` maxDD `-0.3914`
- `market_context_high->crypto_major_24h` score `-1.0037` n `186` status `ready` deltaP `22.7767` edge `0.6231` maxDD `-62.3533`
- `market_context_high->commodity_1h` score `-1.0418` n `196` status `ready` deltaP `0.6324` edge `0.0011` maxDD `-4.7041`
- `market_context_high->metal_1h` score `-1.2822` n `196` status `ready` deltaP `3.4553` edge `0.0037` maxDD `-6.3532`
- `market_context_high->fx_4h` score `-1.3591` n `186` status `ready` deltaP `-10.1019` edge `-0.014` maxDD `-1.4313`
- `market_context_high->metal_4h` score `-1.3682` n `186` status `ready` deltaP `8.8906` edge `0.0959` maxDD `-12.5349`
- `market_context_high->crypto_alt_24h` score `-2.5243` n `186` status `ready` deltaP `22.9279` edge `0.8177` maxDD `-88.8062`
- `market_context_high->unknown_4h` score `-4.2731` n `186` status `ready` deltaP `7.0696` edge `-0.1761` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
