# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-14T02:52:23.694911+00:00`
- Price records: `672`
- Market context records: `6667`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11784`

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

- `market_context_high->unknown_1h` score `2.5597` n `202` status `ready` deltaP `-4.8126` edge `0.3355` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `1.2154` n `202` status `ready` deltaP `12.2852` edge `0.2062` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `0.0445` n `202` status `ready` deltaP `7.863` edge `0.0476` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.1068` n `202` status `ready` deltaP `5.5834` edge `0.0428` maxDD `-3.7803`
- `market_context_high->unknown_4h` score `-0.1471` n `202` status `ready` deltaP `-14.3534` edge `0.324` maxDD `-10.5788`
- `market_context_high->fx_1h` score `-0.2419` n `202` status `ready` deltaP `2.8221` edge `0.0009` maxDD `-0.7249`
- `market_context_high->unknown_24h` score `-0.2497` n `202` status `ready` deltaP `-4.1082` edge `0.3706` maxDD `-12.3511`
- `market_context_high->index_1h` score `-0.4735` n `202` status `ready` deltaP `0.8641` edge `0.0053` maxDD `-0.7417`
- `market_context_high->commodity_1h` score `-0.6338` n `202` status `ready` deltaP `-0.6225` edge `-0.0088` maxDD `-2.1314`
- `market_context_high->index_4h` score `-0.8306` n `202` status `ready` deltaP `10.7387` edge `0.0099` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-0.8376` n `202` status `ready` deltaP `3.615` edge `0.0088` maxDD `-3.8827`
- `market_context_high->crypto_major_4h` score `-1.1746` n `202` status `ready` deltaP `10.3598` edge `0.1118` maxDD `-16.8495`
- `market_context_high->metal_1h` score `-1.1829` n `202` status `ready` deltaP `-3.787` edge `0.0008` maxDD `-1.5966`
- `market_context_high->fx_4h` score `-1.3972` n `202` status `ready` deltaP `6.253` edge `0.0004` maxDD `-3.3635`
- `market_context_high->commodity_4h` score `-1.4699` n `202` status `ready` deltaP `-1.3765` edge `-0.0298` maxDD `-5.6246`
- `market_context_high->crypto_alt_4h` score `-1.4777` n `202` status `ready` deltaP `7.6551` edge `0.0997` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.0139` n `202` status `ready` deltaP `0.0075` edge `0.0278` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-4.6438` n `202` status `ready` deltaP `7.9993` edge `-0.0134` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-6.4242` n `202` status `ready` deltaP `-12.3367` edge `-0.0132` maxDD `-10.8591`
- `market_context_high->metal_24h` score `-6.831` n `202` status `ready` deltaP `-4.672` edge `0.0039` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
