# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T08:52:28.862033+00:00`
- Price records: `672`
- Market context records: `7122`
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

- `market_context_high->fx_4h` score `0.3584` n `145` status `ready` deltaP `15.2481` edge `0.0143` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.0595` n `151` status `ready` deltaP `5.2028` edge `0.0028` maxDD `-0.276`
- `market_context_high->unknown_1h` score `-0.2772` n `151` status `ready` deltaP `-1.1609` edge `0.0405` maxDD `-1.4688`
- `market_context_high->crypto_alt_1h` score `-0.4121` n `151` status `ready` deltaP `0.8437` edge `0.0303` maxDD `-4.7674`
- `market_context_high->index_1h` score `-0.8008` n `151` status `ready` deltaP `0.7852` edge `-0.0055` maxDD `-2.3175`
- `market_context_high->crypto_major_1h` score `-0.8285` n `151` status `ready` deltaP `4.1549` edge `0.0385` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-0.8499` n `151` status `ready` deltaP `-4.1371` edge `-0.0193` maxDD `-1.9668`
- `market_context_high->metal_1h` score `-1.3832` n `151` status `ready` deltaP `-5.0254` edge `-0.0052` maxDD `-2.1249`
- `market_context_high->commodity_4h` score `-1.4022` n `145` status `ready` deltaP `-4.8959` edge `-0.0436` maxDD `-2.9494`
- `market_context_high->unknown_4h` score `-1.527` n `145` status `ready` deltaP `-6.6106` edge `0.0085` maxDD `-4.4825`
- `market_context_high->crypto_major_4h` score `-3.0334` n `145` status `ready` deltaP `4.1631` edge `0.0118` maxDD `-24.6094`
- `market_context_high->equity_1h` score `-3.2286` n `151` status `ready` deltaP `2.4953` edge `-0.0434` maxDD `-14.716`
- `market_context_high->commodity_24h` score `-3.7971` n `145` status `ready` deltaP `-9.7869` edge `-0.1203` maxDD `-4.4704`
- `market_context_high->index_4h` score `-4.0987` n `145` status `ready` deltaP `-3.2927` edge `-0.0497` maxDD `-12.2591`
- `market_context_high->metal_4h` score `-4.5192` n `145` status `ready` deltaP `-10.0883` edge `-0.0125` maxDD `-5.414`
- `market_context_high->crypto_alt_4h` score `-4.6483` n `145` status `ready` deltaP `0.8526` edge `-0.0145` maxDD `-22.2831`
- `market_context_high->fx_24h` score `-4.6785` n `145` status `ready` deltaP `-12.6089` edge `-0.0231` maxDD `-3.9503`
- `market_context_high->unknown_24h` score `-9.4655` n `145` status `ready` deltaP `-28.0519` edge `-0.0871` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-13.7123` n `145` status `ready` deltaP `-2.1531` edge `-0.2413` maxDD `-63.963`
- `market_context_high->metal_24h` score `-14.8299` n `145` status `ready` deltaP `-28.0088` edge `-0.1641` maxDD `-42.1336`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
