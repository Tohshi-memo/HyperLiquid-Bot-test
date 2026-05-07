# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T02:26:04.914821+00:00`
- Price records: `509`
- Market context records: `604`
- Flow alert records: `1707`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `807`

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

- `market_context_high->crypto_alt_24h` score `4.7398` n `146` status `ready` deltaP `7.0633` edge `0.3527` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `3.9237` n `146` status `ready` deltaP `11.6355` edge `0.2828` maxDD `-1.3382`
- `market_context_high->fx_4h` score `0.0135` n `146` status `ready` deltaP `10.5709` edge `0.0184` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3194` n `146` status `ready` deltaP `1.9591` edge `0.0038` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.6043` n `146` status `ready` deltaP `1.4382` edge `0.0375` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6523` n `146` status `ready` deltaP `0.6795` edge `-0.0028` maxDD `-2.8282`
- `market_context_high->crypto_alt_1h` score `-1.075` n `146` status `ready` deltaP `5.9678` edge `0.0021` maxDD `-8.1842`
- `market_context_high->unknown_1h` score `-1.1192` n `146` status `ready` deltaP `-3.7542` edge `-0.0079` maxDD `-2.1602`
- `market_context_high->equity_1h` score `-1.2153` n `146` status `ready` deltaP `-1.7158` edge `-0.0088` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.6997` n `146` status `ready` deltaP `5.5296` edge `-0.0062` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-1.8046` n `146` status `ready` deltaP `4.1693` edge `0.0788` maxDD `-15.2248`
- `market_context_high->index_4h` score `-2.2159` n `146` status `ready` deltaP `0.2423` edge `-0.034` maxDD `-6.5149`
- `market_context_high->index_24h` score `-2.5254` n `146` status `ready` deltaP `-7.0553` edge `0.0361` maxDD `-5.9609`
- `market_context_high->crypto_major_4h` score `-2.5404` n `146` status `ready` deltaP `13.5` edge `0.0689` maxDD `-22.648`
- `market_context_high->equity_4h` score `-3.1968` n `146` status `ready` deltaP `-3.0297` edge `-0.031` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.3503` n `146` status `ready` deltaP `-4.8841` edge `-0.0507` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.7973` n `146` status `ready` deltaP `-7.2667` edge `0.0821` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-4.3048` n `146` status `ready` deltaP `-3.0177` edge `-0.0146` maxDD `-21.0414`
- `market_context_high->equity_24h` score `-4.575` n `146` status `ready` deltaP `-10.7211` edge `-0.0493` maxDD `-10.5047`
- `market_context_high->unknown_4h` score `-4.9531` n `146` status `ready` deltaP `1.224` edge `-0.2331` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
