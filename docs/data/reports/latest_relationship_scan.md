# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T04:07:25.141869+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9688`

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

- `market_context_high->unknown_4h` score `85.2756` n `151` status `ready` deltaP `1.7939` edge `7.1279` maxDD `-1.0178`
- `market_context_high->unknown_1h` score `12.5707` n `151` status `ready` deltaP `1.2581` edge `1.0881` maxDD `-1.5807`
- `market_context_high->fx_1h` score `0.3221` n `151` status `ready` deltaP `8.9632` edge `0.0029` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.3202` n `151` status `ready` deltaP `11.5843` edge `0.0093` maxDD `-0.4545`
- `market_context_high->index_24h` score `0.1283` n `122` status `ready` deltaP `17.679` edge `0.0148` maxDD `-3.9636`
- `market_context_high->metal_24h` score `0.1023` n `122` status `ready` deltaP `21.0898` edge `0.1267` maxDD `-6.3348`
- `market_context_high->metal_1h` score `-0.0721` n `151` status `ready` deltaP `9.0316` edge `0.0076` maxDD `-1.4974`
- `market_context_high->fx_24h` score `-0.1394` n `122` status `ready` deltaP `17.0938` edge `0.0254` maxDD `-1.2451`
- `market_context_high->commodity_1h` score `-0.1647` n `151` status `ready` deltaP `3.0208` edge `0.0162` maxDD `-1.0053`
- `market_context_high->commodity_4h` score `-0.2957` n `151` status `ready` deltaP `7.2687` edge `0.0498` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.6255` n `151` status `ready` deltaP `-0.6712` edge `-0.002` maxDD `-1.8971`
- `market_context_high->metal_4h` score `-0.8637` n `151` status `ready` deltaP `8.4578` edge `-0.0006` maxDD `-4.9875`
- `market_context_high->crypto_major_1h` score `-0.8952` n `151` status `ready` deltaP `4.4999` edge `0.0133` maxDD `-9.3126`
- `market_context_high->equity_1h` score `-1.8044` n `151` status `ready` deltaP `1.2115` edge `-0.0118` maxDD `-12.2088`
- `market_context_high->crypto_alt_1h` score `-2.0103` n `151` status `ready` deltaP `-0.4303` edge `-0.0064` maxDD `-13.2099`
- `market_context_high->index_4h` score `-3.5076` n `151` status `ready` deltaP `-7.1636` edge `-0.0269` maxDD `-6.7447`
- `market_context_high->crypto_major_24h` score `-4.0944` n `122` status `ready` deltaP `0.1193` edge `-0.04` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-4.5591` n `151` status `ready` deltaP `-0.5885` edge `-0.0885` maxDD `-32.0325`
- `market_context_high->equity_24h` score `-5.1849` n `122` status `ready` deltaP `-4.0728` edge `-0.1561` maxDD `-30.5188`
- `market_context_high->commodity_24h` score `-5.5607` n `122` status `ready` deltaP `-8.7749` edge `-0.0954` maxDD `-24.0547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
