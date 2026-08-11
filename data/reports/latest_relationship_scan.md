# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-11T01:52:27.834904+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11744`

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

- `market_context_high->unknown_24h` score `11.2129` n `145` status `ready` deltaP `-14.5772` edge `1.277` maxDD `-9.6329`
- `market_context_high->fx_24h` score `1.1061` n `145` status `ready` deltaP `20.4064` edge `0.0369` maxDD `-1.4613`
- `market_context_high->commodity_4h` score `0.9569` n `168` status `ready` deltaP `12.4201` edge `0.0684` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.7138` n `180` status `ready` deltaP `9.7173` edge `0.029` maxDD `-0.7439`
- `market_context_high->fx_4h` score `-0.1198` n `168` status `ready` deltaP `5.8072` edge `0.0059` maxDD `-0.4647`
- `market_context_high->fx_1h` score `-0.1442` n `180` status `ready` deltaP `4.1218` edge `-0.0008` maxDD `-0.613`
- `market_context_high->index_1h` score `-0.8647` n `180` status `ready` deltaP `-7.0758` edge `-0.0049` maxDD `-1.0359`
- `market_context_high->metal_1h` score `-1.2852` n `180` status `ready` deltaP `-5.2195` edge `-0.0087` maxDD `-2.0884`
- `market_context_high->equity_1h` score `-1.4489` n `180` status `ready` deltaP `-6.0545` edge `-0.0177` maxDD `-6.8818`
- `market_context_high->metal_24h` score `-1.6206` n `145` status `ready` deltaP `2.5482` edge `-0.0196` maxDD `-2.9283`
- `market_context_high->index_4h` score `-1.977` n `168` status `ready` deltaP `-8.1446` edge `-0.02` maxDD `-1.5693`
- `market_context_high->index_24h` score `-2.0421` n `145` status `ready` deltaP `-8.5914` edge `0.005` maxDD `-6.7627`
- `market_context_high->crypto_alt_1h` score `-2.6787` n `180` status `ready` deltaP `-9.5143` edge `-0.0412` maxDD `-6.4874`
- `market_context_high->commodity_24h` score `-2.9171` n `145` status `ready` deltaP `6.7436` edge `0.0586` maxDD `-28.2037`
- `market_context_high->metal_4h` score `-3.2694` n `168` status `ready` deltaP `-8.5439` edge `-0.0391` maxDD `-6.1111`
- `market_context_high->crypto_major_1h` score `-3.7699` n `180` status `ready` deltaP `-10.2362` edge `-0.0555` maxDD `-11.9002`
- `market_context_high->equity_4h` score `-4.6168` n `168` status `ready` deltaP `-17.6829` edge `-0.1631` maxDD `-15.8728`
- `market_context_high->crypto_major_24h` score `-6.3546` n `145` status `ready` deltaP `-11.6931` edge `-0.1809` maxDD `-32.4675`
- `market_context_high->crypto_alt_4h` score `-6.9679` n `168` status `ready` deltaP `-14.0027` edge `-0.1525` maxDD `-20.1177`
- `market_context_high->equity_24h` score `-8.9428` n `145` status `ready` deltaP `-8.9524` edge `-0.2598` maxDD `-51.829`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
