# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T08:22:19.149397+00:00`
- Price records: `672`
- Market context records: `2544`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9252`

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

- `market_context_high->crypto_alt_4h` score `5.3805` n `153` status `ready` deltaP `23.921` edge `0.5568` maxDD `-15.4319`
- `market_context_high->unknown_24h` score `5.3642` n `118` status `ready` deltaP `19.4768` edge `0.35` maxDD `-1.626`
- `market_context_high->crypto_major_24h` score `5.0318` n `118` status `ready` deltaP `12.1704` edge `0.6032` maxDD `-16.2014`
- `market_context_high->crypto_major_4h` score `3.7591` n `153` status `ready` deltaP `17.124` edge `0.3801` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `1.8921` n `153` status `ready` deltaP `10.7175` edge `0.1912` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `1.1657` n `153` status `ready` deltaP `9.7912` edge `0.1506` maxDD `-6.1656`
- `market_context_high->equity_24h` score `1.0859` n `118` status `ready` deltaP `18.9972` edge `0.0309` maxDD `-3.0311`
- `market_context_high->crypto_major_1h` score `0.711` n `153` status `ready` deltaP `8.3343` edge `0.1231` maxDD `-4.2199`
- `market_context_high->index_24h` score `0.537` n `118` status `ready` deltaP `5.4791` edge `0.1063` maxDD `-2.5127`
- `market_context_high->crypto_alt_24h` score `-0.0048` n `118` status `ready` deltaP `-0.9592` edge `0.671` maxDD `-41.2179`
- `market_context_high->unknown_1h` score `-0.1178` n `153` status `ready` deltaP `3.5547` edge `0.0355` maxDD `-2.8543`
- `market_context_high->index_4h` score `-0.1298` n `153` status `ready` deltaP `6.1255` edge `0.0325` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.26` n `153` status `ready` deltaP `2.9304` edge `0.0082` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.322` n `153` status `ready` deltaP `1.1849` edge `0.0043` maxDD `-0.278`
- `market_context_high->metal_1h` score `-0.3725` n `153` status `ready` deltaP `2.0283` edge `0.0135` maxDD `-2.9823`
- `market_context_high->commodity_1h` score `-0.3791` n `153` status `ready` deltaP `3.814` edge `0.0138` maxDD `-4.3601`
- `market_context_high->equity_1h` score `-0.7599` n `153` status `ready` deltaP `0.3053` edge `0.0185` maxDD `-2.7085`
- `market_context_high->metal_4h` score `-0.7793` n `153` status `ready` deltaP `4.0062` edge `0.0471` maxDD `-4.7664`
- `market_context_high->fx_4h` score `-0.8602` n `153` status `ready` deltaP `0.283` edge `0.0124` maxDD `-0.8774`
- `market_context_high->fx_24h` score `-0.9044` n `118` status `ready` deltaP `1.6037` edge `0.0028` maxDD `-2.3556`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
