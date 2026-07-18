# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T09:37:27.210232+00:00`
- Price records: `672`
- Market context records: `7125`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11667`

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

- `market_context_high->fx_4h` score `0.4252` n `142` status `ready` deltaP `16.472` edge `0.0147` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.0329` n `151` status `ready` deltaP `5.7154` edge `0.0028` maxDD `-0.276`
- `market_context_high->unknown_1h` score `-0.3676` n `151` status `ready` deltaP `-2.186` edge `0.0398` maxDD `-1.4688`
- `market_context_high->crypto_alt_1h` score `-0.6359` n `151` status `ready` deltaP `-0.694` edge `0.0225` maxDD `-5.6189`
- `market_context_high->index_1h` score `-0.7116` n `151` status `ready` deltaP `1.8103` edge `-0.0049` maxDD `-2.3175`
- `market_context_high->commodity_1h` score `-0.8209` n `151` status `ready` deltaP `-3.6245` edge `-0.019` maxDD `-1.9668`
- `market_context_high->crypto_major_1h` score `-1.0449` n `151` status `ready` deltaP `2.6173` edge `0.0339` maxDD `-7.407`
- `market_context_high->unknown_4h` score `-1.4524` n `142` status `ready` deltaP `-5.9258` edge `0.0135` maxDD `-4.4825`
- `market_context_high->metal_1h` score `-1.4664` n `151` status `ready` deltaP `-6.0505` edge `-0.0053` maxDD `-2.1249`
- `market_context_high->commodity_4h` score `-2.2474` n `142` status `ready` deltaP `-5.8721` edge `-0.0446` maxDD `-2.9494`
- `market_context_high->crypto_major_4h` score `-3.0829` n `142` status `ready` deltaP `3.6005` edge `0.0092` maxDD `-24.6094`
- `market_context_high->equity_1h` score `-3.3076` n `151` status `ready` deltaP `1.9828` edge `-0.0446` maxDD `-14.8732`
- `market_context_high->commodity_24h` score `-3.9559` n `142` status `ready` deltaP `-10.6465` edge `-0.1278` maxDD `-4.4704`
- `market_context_high->index_4h` score `-4.2083` n `142` status `ready` deltaP `-4.4078` edge `-0.0514` maxDD `-12.2591`
- `market_context_high->metal_4h` score `-4.5164` n `142` status `ready` deltaP `-10.0502` edge `-0.013` maxDD `-5.3756`
- `market_context_high->fx_24h` score `-4.7284` n `142` status `ready` deltaP `-13.1578` edge `-0.0236` maxDD `-3.9503`
- `market_context_high->crypto_alt_4h` score `-4.753` n `142` status `ready` deltaP `0.1589` edge `-0.0186` maxDD `-22.2831`
- `market_context_high->unknown_24h` score `-9.5319` n `142` status `ready` deltaP `-28.2669` edge `-0.0912` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-13.8361` n `142` status `ready` deltaP `-2.4261` edge `-0.2498` maxDD `-63.963`
- `market_context_high->metal_24h` score `-14.7239` n `142` status `ready` deltaP `-28.3549` edge `-0.1695` maxDD `-41.8101`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
