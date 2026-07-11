# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T01:04:44.644780+00:00`
- Price records: `672`
- Market context records: `6340`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11134`

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

- `news_risk_high->crypto_alt_24h` score `15.2915` n `32` status `ready` deltaP `43.0556` edge `1.002` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.0992` n `32` status `ready` deltaP `50.6944` edge `0.1703` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.3676` n `32` status `ready` deltaP `16.6667` edge `0.5268` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `4.2033` n `32` status `ready` deltaP `43.8262` edge `0.0627` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.526` n `32` status `ready` deltaP `31.0764` edge `0.1072` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.3883` n `32` status `ready` deltaP `28.7425` edge `0.0213` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.524` n `32` status `ready` deltaP `14.8765` edge `0.1429` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.9673` n `32` status `ready` deltaP `12.0696` edge `0.0897` maxDD `-1.6923`
- `market_context_high->metal_4h` score `0.5212` n `196` status `ready` deltaP `12.2232` edge `0.0416` maxDD `-2.7056`
- `market_context_high->unknown_1h` score `0.1789` n `207` status `ready` deltaP `-7.182` edge `0.1636` maxDD `-3.7317`
- `market_context_high->index_4h` score `0.0665` n `196` status `ready` deltaP `6.4118` edge `0.0221` maxDD `-0.4108`
- `market_context_high->metal_1h` score `-0.3791` n `207` status `ready` deltaP `4.0448` edge `0.0022` maxDD `-1.8877`
- `market_context_high->commodity_1h` score `-0.5473` n `207` status `ready` deltaP `-0.3233` edge `0.0003` maxDD `-2.1314`
- `market_context_high->metal_24h` score `-0.5602` n `137` status `ready` deltaP `15.6186` edge `0.0809` maxDD `-11.8809`
- `market_context_high->equity_4h` score `-0.6982` n `196` status `ready` deltaP `5.3198` edge `0.0449` maxDD `-8.2573`
- `news_risk_high->index_24h` score `-0.7109` n `32` status `ready` deltaP `0.3472` edge `-0.0063` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.7312` n `207` status `ready` deltaP `-0.8469` edge `-0.0019` maxDD `-0.9376`
- `news_risk_high->metal_1h` score `-0.7636` n `32` status `ready` deltaP `-3.4431` edge `-0.0252` maxDD `-1.6464`
- `news_risk_high->unknown_1h` score `-0.8451` n `32` status `ready` deltaP `5.3331` edge `-0.0715` maxDD `-0.7581`
- `market_context_high->commodity_24h` score `-1.0095` n `137` status `ready` deltaP `-3.6636` edge `0.1267` maxDD `-6.2457`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
