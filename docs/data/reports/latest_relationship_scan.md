# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T07:28:55.583955+00:00`
- Price records: `672`
- Market context records: `989`
- Flow alert records: `4756`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1440`

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

- `market_context_high->crypto_major_24h` score `12.7957` n `211` status `ready` deltaP `31.2846` edge `0.9166` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.1167` n `211` status `ready` deltaP `10.7034` edge `0.3951` maxDD `-9.5387`
- `market_context_high->fx_1h` score `-0.3631` n `211` status `ready` deltaP `1.7721` edge `-0.0003` maxDD `-0.3124`
- `market_context_high->commodity_1h` score `-0.4815` n `211` status `ready` deltaP `2.9941` edge `0.0207` maxDD `-3.7959`
- `market_context_high->equity_1h` score `-0.6566` n `211` status `ready` deltaP `0.9528` edge `0.0158` maxDD `-4.4826`
- `market_context_high->index_24h` score `-0.6984` n `211` status `ready` deltaP `2.8966` edge `0.122` maxDD `-5.9609`
- `market_context_high->fx_4h` score `-0.7307` n `211` status `ready` deltaP `0.7586` edge `0.0009` maxDD `-1.6381`
- `market_context_high->index_1h` score `-0.7736` n `211` status `ready` deltaP `2.4431` edge `0.0046` maxDD `-2.8282`
- `market_context_high->equity_24h` score `-1.2147` n `211` status `ready` deltaP `4.3721` edge `0.1301` maxDD `-10.5047`
- `market_context_high->crypto_major_1h` score `-1.2193` n `211` status `ready` deltaP `4.738` edge `-0.0156` maxDD `-11.4508`
- `market_context_high->equity_4h` score `-1.5343` n `211` status `ready` deltaP `1.6118` edge `0.0766` maxDD `-10.5498`
- `market_context_high->index_4h` score `-1.7663` n `211` status `ready` deltaP `-1.9084` edge `0.0178` maxDD `-6.5149`
- `market_context_high->metal_1h` score `-1.91` n `211` status `ready` deltaP `-1.5066` edge `-0.0389` maxDD `-9.0076`
- `market_context_high->crypto_alt_1h` score `-2.0466` n `211` status `ready` deltaP `-0.6272` edge `-0.0224` maxDD `-8.1842`
- `market_context_high->crypto_major_4h` score `-2.9442` n `211` status `ready` deltaP `7.0122` edge `0.0785` maxDD `-22.648`
- `market_context_high->commodity_4h` score `-3.316` n `211` status `ready` deltaP `-2.2312` edge `0.0553` maxDD `-13.0076`
- `market_context_high->crypto_alt_4h` score `-3.3629` n `211` status `ready` deltaP `-2.2842` edge `0.0128` maxDD `-15.2248`
- `market_context_high->fx_24h` score `-3.5748` n `211` status `ready` deltaP `-1.301` edge `-0.0217` maxDD `-20.2343`
- `market_context_high->metal_4h` score `-4.6257` n `211` status `ready` deltaP `-5.137` edge `-0.1631` maxDD `-24.9891`
- `market_context_high->commodity_24h` score `-8.3336` n `211` status `ready` deltaP `2.3655` edge `0.3806` maxDD `-102.8492`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
