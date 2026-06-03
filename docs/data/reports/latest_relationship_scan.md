# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T12:07:23.841303+00:00`
- Price records: `672`
- Market context records: `2762`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9237`

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

- `market_context_high->unknown_24h` score `5.4858` n `130` status `ready` deltaP `11.9498` edge `0.4103` maxDD `-1.6255`
- `market_context_high->crypto_alt_24h` score `3.7083` n `130` status `ready` deltaP `6.477` edge `0.7816` maxDD `-19.9486`
- `market_context_high->unknown_4h` score `0.9969` n `143` status `ready` deltaP `6.7063` edge `0.1437` maxDD `-3.7602`
- `market_context_high->index_4h` score `0.0387` n `143` status `ready` deltaP `10.2465` edge `0.0208` maxDD `-2.3986`
- `market_context_high->commodity_24h` score `-0.0821` n `130` status `ready` deltaP `8.2425` edge `0.2439` maxDD `-12.4171`
- `market_context_high->unknown_1h` score `-0.1017` n `143` status `ready` deltaP `3.797` edge `0.0393` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.1612` n `143` status `ready` deltaP `3.0506` edge `0.0084` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.5722` n `143` status `ready` deltaP `-0.9463` edge `0.003` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.6597` n `143` status `ready` deltaP `-0.247` edge `-0.0076` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.6711` n `143` status `ready` deltaP `5.8457` edge `0.051` maxDD `-10.747`
- `market_context_high->metal_1h` score `-0.7692` n `143` status `ready` deltaP `-0.9506` edge `-0.0077` maxDD `-3.0996`
- `market_context_high->crypto_major_1h` score `-0.9549` n `143` status `ready` deltaP `3.6473` edge `0.0402` maxDD `-9.622`
- `market_context_high->equity_1h` score `-1.1728` n `143` status `ready` deltaP `-3.7864` edge `0.0108` maxDD `-2.6634`
- `market_context_high->crypto_alt_4h` score `-1.2088` n `143` status `ready` deltaP `14.9913` edge `0.2334` maxDD `-28.7261`
- `market_context_high->fx_4h` score `-1.2307` n `143` status `ready` deltaP `-4.7075` edge `0.0067` maxDD `-0.5631`
- `market_context_high->fx_24h` score `-1.2545` n `130` status `ready` deltaP `0.187` edge `-0.0186` maxDD `-0.6418`
- `market_context_high->commodity_4h` score `-1.7048` n `143` status `ready` deltaP `-0.7728` edge `-0.0214` maxDD `-10.0279`
- `market_context_high->equity_4h` score `-2.1093` n `143` status `ready` deltaP `-1.0969` edge `-0.0305` maxDD `-5.7037`
- `market_context_high->metal_4h` score `-2.4537` n `143` status `ready` deltaP `-2.6437` edge `-0.0419` maxDD `-11.4038`
- `market_context_high->crypto_major_4h` score `-2.614` n `143` status `ready` deltaP `5.2277` edge `0.1206` maxDD `-32.2466`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
