# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T17:22:26.479233+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10123`

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

- `risk_on_high->unknown_24h` score `159.8331` n `106` status `ready` deltaP `25.2948` edge `13.1607` maxDD `-0.1262`
- `risk_on_and_context->unknown_24h` score `159.8331` n `106` status `ready` deltaP `25.2948` edge `13.1607` maxDD `-0.1262`
- `risk_on_high->crypto_major_24h` score `16.2889` n `106` status `ready` deltaP `30.0217` edge `1.3645` maxDD `-12.579`
- `risk_on_and_context->crypto_major_24h` score `16.2889` n `106` status `ready` deltaP `30.0217` edge `1.3645` maxDD `-12.579`
- `risk_on_high->crypto_alt_24h` score `7.3994` n `106` status `ready` deltaP `18.239` edge `0.7166` maxDD `-12.7264`
- `risk_on_and_context->crypto_alt_24h` score `7.3994` n `106` status `ready` deltaP `18.239` edge `0.7166` maxDD `-12.7264`
- `market_context_high->equity_24h` score `4.7794` n `196` status `ready` deltaP `19.0512` edge `0.3798` maxDD `-4.6817`
- `market_context_high->crypto_alt_24h` score `4.3521` n `196` status `ready` deltaP `17.517` edge `0.4928` maxDD `-14.0858`
- `risk_on_high->equity_24h` score `3.0388` n `106` status `ready` deltaP `13.8528` edge `0.2694` maxDD `-4.6817`
- `risk_on_and_context->equity_24h` score `3.0388` n `106` status `ready` deltaP `13.8528` edge `0.2694` maxDD `-4.6817`
- `market_context_high->index_24h` score `0.6271` n `196` status `ready` deltaP `16.5745` edge `0.0829` maxDD `-3.6243`
- `risk_on_high->index_24h` score `0.3893` n `106` status `ready` deltaP `12.7817` edge `0.057` maxDD `-3.1149`
- `risk_on_and_context->index_24h` score `0.3893` n `106` status `ready` deltaP `12.7817` edge `0.057` maxDD `-3.1149`
- `risk_on_high->crypto_alt_1h` score `-0.1225` n `129` status `ready` deltaP `3.8516` edge `0.0658` maxDD `-5.4685`
- `risk_on_and_context->crypto_alt_1h` score `-0.1225` n `129` status `ready` deltaP `3.8516` edge `0.0658` maxDD `-5.4685`
- `risk_on_high->index_1h` score `-0.1268` n `129` status `ready` deltaP `4.7927` edge `-0.0035` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `-0.1268` n `129` status `ready` deltaP `4.7927` edge `-0.0035` maxDD `-0.5764`
- `risk_on_high->metal_1h` score `-0.3348` n `129` status `ready` deltaP `4.6059` edge `-0.003` maxDD `-1.6499`
- `risk_on_and_context->metal_1h` score `-0.3348` n `129` status `ready` deltaP `4.6059` edge `-0.003` maxDD `-1.6499`
- `risk_on_high->equity_1h` score `-0.3636` n `129` status `ready` deltaP `8.1071` edge `-0.0136` maxDD `-2.6312`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
