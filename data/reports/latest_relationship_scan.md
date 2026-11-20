# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-20T14:52:25.246859+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2654`

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

- `market_context_high->unknown_1h` score `10462.5604` n `123` status `ready` deltaP `1.7916` edge `871.8879` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `6800.9021` n `117` status `ready` deltaP `1.0892` edge `566.763` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `4.7638` n `107` status `ready` deltaP `27.4257` edge `1.1409` maxDD `-50.7065`
- `market_context_high->crypto_alt_24h` score `1.5647` n `107` status `ready` deltaP `14.3156` edge `0.947` maxDD `-66.63`
- `market_context_high->crypto_major_4h` score `0.4559` n `117` status `ready` deltaP `2.981` edge `0.3095` maxDD `-16.9772`
- `market_context_high->metal_4h` score `0.1721` n `117` status `ready` deltaP `15.7638` edge `0.0523` maxDD `-7.1105`
- `market_context_high->metal_1h` score `-0.1403` n `123` status `ready` deltaP `4.6188` edge `0.0177` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.2802` n `123` status `ready` deltaP `3.207` edge `0.0039` maxDD `-1.2295`
- `market_context_high->crypto_alt_4h` score `-0.4552` n `117` status `ready` deltaP `4.0481` edge `0.2218` maxDD `-19.5714`
- `market_context_high->crypto_major_1h` score `-0.9983` n `123` status `ready` deltaP `3.4212` edge `0.0506` maxDD `-7.8611`
- `market_context_high->fx_1h` score `-1.2576` n `123` status `ready` deltaP `-7.1479` edge `-0.0012` maxDD `-0.4757`
- `market_context_high->equity_1h` score `-1.3694` n `123` status `ready` deltaP `6.0951` edge `0.0314` maxDD `-11.559`
- `market_context_high->crypto_alt_1h` score `-1.7703` n `123` status `ready` deltaP `-2.2699` edge `0.0272` maxDD `-8.4343`
- `market_context_high->index_4h` score `-1.9191` n `117` status `ready` deltaP `-2.2671` edge `-0.0092` maxDD `-4.8491`
- `market_context_high->commodity_1h` score `-1.9316` n `123` status `ready` deltaP `-5.158` edge `-0.0134` maxDD `-4.3877`
- `market_context_high->fx_4h` score `-2.0873` n `117` status `ready` deltaP `-9.8721` edge `-0.0002` maxDD `-1.794`
- `market_context_high->metal_24h` score `-5.9146` n `107` status `ready` deltaP `13.2139` edge `0.092` maxDD `-43.8379`
- `market_context_high->fx_24h` score `-6.6396` n `107` status `ready` deltaP `-17.5785` edge `-0.0088` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-6.996` n `117` status `ready` deltaP `-21.348` edge `-0.0714` maxDD `-15.5426`
- `market_context_high->equity_4h` score `-10.6079` n `117` status `ready` deltaP `-5.5387` edge `-0.0852` maxDD `-50.6163`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
