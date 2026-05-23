# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T11:52:13.449476+00:00`
- Price records: `672`
- Market context records: `1628`
- Flow alert records: `6593`
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

- `market_context_high->metal_24h` score `10.3776` n `187` status `ready` deltaP `26.5198` edge `0.9306` maxDD `-12.7414`
- `market_context_high->index_24h` score `3.1612` n `187` status `ready` deltaP `18.6656` edge `0.2768` maxDD `-5.3574`
- `market_context_high->equity_4h` score `1.4481` n `187` status `ready` deltaP `11.9742` edge `0.1503` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `0.9944` n `187` status `ready` deltaP `15.4681` edge `0.322` maxDD `-18.4769`
- `market_context_high->crypto_major_4h` score `0.5002` n `187` status `ready` deltaP `11.2675` edge `0.2599` maxDD `-13.3376`
- `market_context_high->equity_24h` score `0.3823` n `187` status `ready` deltaP `17.2209` edge `0.4069` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `-0.196` n `196` status `ready` deltaP `2.1355` edge `0.063` maxDD `-4.1892`
- `market_context_high->fx_24h` score `-0.2867` n `187` status `ready` deltaP `7.6519` edge `0.03` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.4431` n `196` status `ready` deltaP `2.0592` edge `0.0302` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.6663` n `196` status `ready` deltaP `0.5622` edge `0.0039` maxDD `-1.7205`
- `market_context_high->index_4h` score `-0.824` n `187` status `ready` deltaP `0.5144` edge `0.0368` maxDD `-3.7119`
- `market_context_high->fx_1h` score `-0.8337` n `196` status `ready` deltaP `-0.443` edge `-0.0033` maxDD `-0.3914`
- `market_context_high->crypto_major_1h` score `-0.8354` n `196` status `ready` deltaP `-0.5988` edge `0.03` maxDD `-5.9819`
- `market_context_high->commodity_1h` score `-1.037` n `196` status `ready` deltaP `0.6324` edge `0.0015` maxDD `-4.7041`
- `market_context_high->crypto_major_24h` score `-1.1021` n `187` status `ready` deltaP `22.6864` edge `0.6155` maxDD `-62.3533`
- `market_context_high->metal_1h` score `-1.2822` n `196` status `ready` deltaP `3.4553` edge `0.0037` maxDD `-6.3532`
- `market_context_high->fx_4h` score `-1.3516` n `187` status `ready` deltaP `-9.9582` edge `-0.014` maxDD `-1.4313`
- `market_context_high->metal_4h` score `-1.3641` n `187` status `ready` deltaP `8.9711` edge `0.0957` maxDD `-12.5349`
- `market_context_high->crypto_alt_24h` score `-2.7076` n `187` status `ready` deltaP `22.8117` edge `0.8032` maxDD `-88.8062`
- `market_context_high->unknown_4h` score `-4.5015` n `187` status `ready` deltaP `6.9144` edge `-0.1941` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
