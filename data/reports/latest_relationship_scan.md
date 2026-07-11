# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T01:37:24.376776+00:00`
- Price records: `672`
- Market context records: `6343`
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

- `news_risk_high->crypto_alt_24h` score `15.2543` n `32` status `ready` deltaP `43.0556` edge `0.9989` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.1064` n `32` status `ready` deltaP `50.6944` edge `0.1709` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.3606` n `32` status `ready` deltaP `16.6667` edge `0.5259` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `4.1911` n `32` status `ready` deltaP `43.6738` edge `0.0627` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.567` n `32` status `ready` deltaP `31.4236` edge `0.1083` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.3751` n `32` status `ready` deltaP `28.5928` edge `0.0212` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.5115` n `32` status `ready` deltaP `14.7268` edge `0.1423` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.9431` n `32` status `ready` deltaP `11.7702` edge `0.0886` maxDD `-1.6923`
- `market_context_high->metal_4h` score `0.5809` n `196` status `ready` deltaP `12.9387` edge `0.0418` maxDD `-2.7056`
- `market_context_high->unknown_1h` score `0.2005` n `207` status `ready` deltaP `-7.182` edge `0.1654` maxDD `-3.7317`
- `market_context_high->index_4h` score `0.0677` n `196` status `ready` deltaP `6.4118` edge `0.0222` maxDD `-0.4108`
- `market_context_high->metal_1h` score `-0.398` n `207` status `ready` deltaP `3.7114` edge `0.002` maxDD `-1.8877`
- `market_context_high->commodity_1h` score `-0.5481` n `207` status `ready` deltaP `-0.3233` edge `0.0002` maxDD `-2.1314`
- `market_context_high->metal_24h` score `-0.6077` n `135` status `ready` deltaP `15.0347` edge `0.0787` maxDD `-11.8809`
- `market_context_high->commodity_24h` score `-0.6512` n `135` status `ready` deltaP `-4.0625` edge `0.13` maxDD `-6.2457`
- `market_context_high->equity_4h` score `-0.6967` n `196` status `ready` deltaP `5.3198` edge `0.0451` maxDD `-8.2573`
- `market_context_high->fx_1h` score `-0.7045` n `207` status `ready` deltaP `-0.5135` edge `-0.0019` maxDD `-0.9376`
- `news_risk_high->index_24h` score `-0.7125` n `32` status `ready` deltaP `0.3472` edge `-0.0065` maxDD `-2.3058`
- `news_risk_high->metal_1h` score `-0.7551` n `32` status `ready` deltaP `-3.2934` edge `-0.0251` maxDD `-1.6464`
- `news_risk_high->unknown_1h` score `-0.8535` n `32` status `ready` deltaP `5.3331` edge `-0.0722` maxDD `-0.7581`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
