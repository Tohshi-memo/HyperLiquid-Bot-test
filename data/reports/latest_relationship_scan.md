# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T15:07:20.457463+00:00`
- Price records: `672`
- Market context records: `1748`
- Flow alert records: `6935`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8862`

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

- `market_context_high->metal_24h` score `7.1676` n `161` status `ready` deltaP `26.7307` edge `0.6617` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `5.8755` n `196` status `ready` deltaP `20.3615` edge `0.5305` maxDD `-9.1295`
- `market_context_high->index_24h` score `4.3274` n `161` status `ready` deltaP `19.1481` edge `0.3558` maxDD `-4.1604`
- `market_context_high->unknown_24h` score `4.241` n `161` status `ready` deltaP `15.2782` edge `0.7836` maxDD `-35.8966`
- `market_context_high->crypto_major_4h` score `4.2287` n `196` status `ready` deltaP `21.6526` edge `0.4486` maxDD `-10.9117`
- `market_context_high->equity_4h` score `2.9353` n `196` status `ready` deltaP `15.6545` edge `0.2497` maxDD `-5.0894`
- `market_context_high->equity_24h` score `2.8952` n `161` status `ready` deltaP `17.3569` edge `0.6154` maxDD `-33.1875`
- `market_context_high->unknown_4h` score `2.8793` n `196` status `ready` deltaP `12.8795` edge `0.3812` maxDD `-11.1695`
- `market_context_high->crypto_alt_1h` score `0.8196` n `196` status `ready` deltaP `7.7203` edge `0.1192` maxDD `-4.1892`
- `market_context_high->index_4h` score `0.7825` n `196` status `ready` deltaP `10.9508` edge `0.1011` maxDD `-3.7119`
- `market_context_high->crypto_major_24h` score `0.6796` n `161` status `ready` deltaP `19.6971` edge `0.7839` maxDD `-62.3533`
- `market_context_high->crypto_major_1h` score `0.258` n `196` status `ready` deltaP `5.0471` edge `0.0952` maxDD `-3.9211`
- `market_context_high->equity_1h` score `0.0658` n `196` status `ready` deltaP `4.9707` edge `0.0532` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.2239` n `196` status `ready` deltaP `3.6173` edge `0.0204` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.2654` n `196` status `ready` deltaP `12.444` edge `0.1522` maxDD `-12.5349`
- `market_context_high->crypto_alt_24h` score `-0.3255` n `161` status `ready` deltaP `20.6078` edge `1.0164` maxDD `-88.8062`
- `market_context_high->metal_1h` score `-0.4785` n `196` status `ready` deltaP `6.3944` edge `0.0296` maxDD `-6.3532`
- `market_context_high->fx_24h` score `-0.6497` n `161` status `ready` deltaP `6.6848` edge `0.0062` maxDD `-1.3925`
- `market_context_high->fx_1h` score `-0.6723` n `196` status `ready` deltaP `-3.2659` edge `-0.0012` maxDD `-0.3914`
- `market_context_high->unknown_1h` score `-1.7038` n `196` status `ready` deltaP `0.1894` edge `0.0037` maxDD `-7.7558`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
