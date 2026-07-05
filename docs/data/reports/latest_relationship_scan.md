# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T21:07:25.186332+00:00`
- Price records: `672`
- Market context records: `5812`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9076`

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

- `market_context_high->equity_4h` score `0.1932` n `289` status `ready` deltaP `5.8766` edge `0.1227` maxDD `-6.9958`
- `market_context_high->equity_24h` score `0.1241` n `248` status `ready` deltaP `15.3954` edge `0.4156` maxDD `-31.6316`
- `market_context_high->fx_1h` score `-0.1866` n `289` status `ready` deltaP `3.4835` edge `0.0014` maxDD `-0.5499`
- `market_context_high->commodity_1h` score `-0.5995` n `289` status `ready` deltaP `-1.3877` edge `-0.003` maxDD `-2.5023`
- `market_context_high->index_1h` score `-0.6513` n `289` status `ready` deltaP `0.0503` edge `0.003` maxDD `-0.9472`
- `market_context_high->metal_1h` score `-0.686` n `289` status `ready` deltaP `1.6871` edge `-0.001` maxDD `-2.0596`
- `market_context_high->equity_1h` score `-0.6963` n `289` status `ready` deltaP `2.4698` edge `0.0262` maxDD `-5.0555`
- `market_context_high->crypto_major_1h` score `-0.9015` n `289` status `ready` deltaP `3.0712` edge `0.0365` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-1.0595` n `289` status `ready` deltaP `1.584` edge `0.0346` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.2393` n `289` status `ready` deltaP `-0.0834` edge `0.0104` maxDD `-3.165`
- `market_context_high->fx_24h` score `-1.4182` n `248` status `ready` deltaP `10.131` edge `0.0314` maxDD `-5.4612`
- `market_context_high->fx_4h` score `-1.4218` n `289` status `ready` deltaP `1.2644` edge `0.0042` maxDD `-2.2593`
- `market_context_high->metal_4h` score `-2.1916` n `289` status `ready` deltaP `-4.3469` edge `-0.0439` maxDD `-9.3146`
- `market_context_high->crypto_major_4h` score `-2.699` n `289` status `ready` deltaP `7.9986` edge `0.159` maxDD `-25.6458`
- `market_context_high->commodity_4h` score `-2.7569` n `289` status `ready` deltaP `-1.8356` edge `-0.0177` maxDD `-8.6511`
- `market_context_high->index_24h` score `-4.3273` n `248` status `ready` deltaP `3.7131` edge `0.0291` maxDD `-18.1572`
- `market_context_high->crypto_alt_4h` score `-4.3756` n `289` status `ready` deltaP `5.6877` edge `0.0983` maxDD `-28.7346`
- `market_context_high->metal_24h` score `-5.5009` n `248` status `ready` deltaP `-4.3067` edge `-0.2351` maxDD `-19.6484`
- `market_context_high->commodity_24h` score `-6.0284` n `248` status `ready` deltaP `-13.1496` edge `-0.0656` maxDD `-32.2348`
- `market_context_high->crypto_major_24h` score `-11.6386` n `248` status `ready` deltaP `-2.6826` edge `-0.2717` maxDD `-36.0908`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
