# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T14:37:18.839968+00:00`
- Price records: `672`
- Market context records: `1746`
- Flow alert records: `6929`
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

- `market_context_high->metal_24h` score `7.1712` n `159` status `ready` deltaP `26.5198` edge `0.6634` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `5.8431` n `196` status `ready` deltaP `20.3615` edge `0.5278` maxDD `-9.1295`
- `market_context_high->index_24h` score `4.3777` n `159` status `ready` deltaP `19.087` edge `0.3604` maxDD `-4.1604`
- `market_context_high->unknown_24h` score `4.3437` n `159` status `ready` deltaP `15.4529` edge `0.791` maxDD `-35.8966`
- `market_context_high->crypto_major_4h` score `4.1647` n `196` status `ready` deltaP `21.3477` edge `0.4453` maxDD `-10.9117`
- `market_context_high->unknown_4h` score `2.9625` n `196` status `ready` deltaP `13.1844` edge `0.3861` maxDD `-11.1695`
- `market_context_high->equity_24h` score `2.9161` n `159` status `ready` deltaP `17.4379` edge `0.6166` maxDD `-33.1875`
- `market_context_high->equity_4h` score `2.899` n `196` status `ready` deltaP `15.3497` edge `0.2487` maxDD `-5.0894`
- `market_context_high->crypto_alt_1h` score `0.7705` n `196` status `ready` deltaP `7.4209` edge `0.1171` maxDD `-4.1892`
- `market_context_high->index_4h` score `0.7437` n `196` status `ready` deltaP `10.6459` edge `0.0999` maxDD `-3.7119`
- `market_context_high->crypto_major_24h` score `0.6826` n `159` status `ready` deltaP `19.8249` edge `0.7833` maxDD `-62.3533`
- `market_context_high->crypto_major_1h` score `0.2041` n `196` status `ready` deltaP `4.7477` edge `0.0927` maxDD `-3.9211`
- `market_context_high->equity_1h` score `0.0299` n `196` status `ready` deltaP `4.6713` edge `0.0522` maxDD `-2.8014`
- `market_context_high->crypto_alt_24h` score `-0.0781` n `159` status `ready` deltaP `20.8059` edge `1.0357` maxDD `-88.8062`
- `market_context_high->index_1h` score `-0.2562` n `196` status `ready` deltaP `3.3179` edge `0.0197` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.2787` n `196` status `ready` deltaP `12.444` edge `0.1505` maxDD `-12.5349`
- `market_context_high->metal_1h` score `-0.4949` n `196` status `ready` deltaP `6.2447` edge `0.0285` maxDD `-6.3532`
- `market_context_high->fx_24h` score `-0.6641` n `159` status `ready` deltaP `6.5051` edge `0.0062` maxDD `-1.3925`
- `market_context_high->fx_1h` score `-0.6809` n `196` status `ready` deltaP `-3.4156` edge `-0.0013` maxDD `-0.3914`
- `market_context_high->unknown_1h` score `-1.6642` n `196` status `ready` deltaP `0.3391` edge `0.006` maxDD `-7.7558`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
