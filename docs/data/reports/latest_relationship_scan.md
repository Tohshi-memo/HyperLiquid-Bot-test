# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-19T20:52:24.159830+00:00`
- Price records: `672`
- Market context records: `7289`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13807`

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

- `market_context_high->fx_1h` score `-0.1573` n `131` status `ready` deltaP `4.0609` edge `0.0017` maxDD `-0.5817`
- `market_context_high->commodity_1h` score `-0.7032` n `131` status `ready` deltaP `-1.8706` edge `-0.0156` maxDD `-1.9668`
- `market_context_high->crypto_alt_1h` score `-0.7825` n `131` status `ready` deltaP `-1.3096` edge `0.0123` maxDD `-5.9775`
- `market_context_high->fx_4h` score `-0.7904` n `128` status `ready` deltaP `6.5916` edge `0.0147` maxDD `-1.4649`
- `market_context_high->crypto_major_1h` score `-0.8739` n `131` status `ready` deltaP `2.5369` edge `0.0121` maxDD `-7.6171`
- `market_context_high->fx_24h` score `-0.9623` n `125` status `ready` deltaP `-0.313` edge `0.0015` maxDD `-2.1564`
- `market_context_high->unknown_1h` score `-1.1592` n `131` status `ready` deltaP `0.9508` edge `-0.0926` maxDD `-1.3212`
- `market_context_high->commodity_4h` score `-1.2384` n `128` status `ready` deltaP `1.1014` edge `-0.0137` maxDD `-2.4139`
- `market_context_high->unknown_4h` score `-1.3101` n `128` status `ready` deltaP `6.269` edge `0.0849` maxDD `-6.2026`
- `market_context_high->index_1h` score `-1.4571` n `131` status `ready` deltaP `-6.5894` edge `-0.0103` maxDD `-2.3756`
- `market_context_high->metal_1h` score `-2.3492` n `131` status `ready` deltaP `-10.8436` edge `-0.0077` maxDD `-1.9289`
- `market_context_high->metal_4h` score `-2.5775` n `128` status `ready` deltaP `-10.9946` edge `-0.0116` maxDD `-4.6441`
- `market_context_high->commodity_24h` score `-2.9581` n `125` status `ready` deltaP `-5.4957` edge `-0.1301` maxDD `-2.3815`
- `market_context_high->crypto_alt_4h` score `-3.8448` n `128` status `ready` deltaP `-0.6479` edge `-0.0235` maxDD `-16.7399`
- `market_context_high->equity_1h` score `-4.7132` n `131` status `ready` deltaP `-10.256` edge `-0.0719` maxDD `-15.5328`
- `market_context_high->crypto_major_4h` score `-5.0649` n `128` status `ready` deltaP `-0.667` edge `-0.0282` maxDD `-23.4879`
- `market_context_high->index_4h` score `-5.3746` n `128` status `ready` deltaP `-15.3503` edge `-0.0653` maxDD `-12.0863`
- `market_context_high->unknown_24h` score `-5.7859` n `126` status `ready` deltaP `-10.5655` edge `-0.0543` maxDD `-16.594`
- `market_context_high->metal_24h` score `-11.6379` n `126` status `ready` deltaP `-29.365` edge `-0.1363` maxDD `-24.3539`
- `market_context_high->index_24h` score `-14.0224` n `125` status `ready` deltaP `-29.6` edge `-0.1745` maxDD `-37.7363`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
