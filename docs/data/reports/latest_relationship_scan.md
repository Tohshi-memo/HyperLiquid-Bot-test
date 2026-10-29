# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-29T08:37:26.424353+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8148`

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

- `market_context_high->unknown_24h` score `1269.8115` n `148` status `ready` deltaP `-2.135` edge `105.9246` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `24.8304` n `149` status `ready` deltaP `4.385` edge `2.0552` maxDD `-0.5521`
- `market_context_high->index_24h` score `0.6101` n `148` status `ready` deltaP `18.6796` edge `-0.0049` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.159` n `149` status `ready` deltaP `7.1193` edge `0.0016` maxDD `-0.1986`
- `market_context_high->commodity_4h` score `-0.1315` n `149` status `ready` deltaP `10.0978` edge `0.0436` maxDD `-1.0837`
- `market_context_high->fx_4h` score `-0.1356` n `149` status `ready` deltaP `6.7718` edge `0.0034` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.1595` n `149` status `ready` deltaP `7.2791` edge `0.0057` maxDD `-1.3073`
- `market_context_high->crypto_major_1h` score `-0.4458` n `149` status `ready` deltaP `5.4827` edge `0.0346` maxDD `-6.9306`
- `market_context_high->commodity_1h` score `-0.4655` n `149` status `ready` deltaP `1.4558` edge `0.0099` maxDD `-1.0053`
- `market_context_high->metal_4h` score `-0.8367` n `149` status `ready` deltaP `7.5319` edge `-0.0034` maxDD `-4.6603`
- `market_context_high->index_1h` score `-0.8496` n `149` status `ready` deltaP `-5.4204` edge `-0.0045` maxDD `-1.4631`
- `market_context_high->fx_24h` score `-1.3262` n `148` status `ready` deltaP `5.4617` edge `0.0103` maxDD `-1.2451`
- `market_context_high->equity_1h` score `-1.5433` n `149` status `ready` deltaP `-0.5576` edge `-0.0029` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.6569` n `149` status `ready` deltaP `1.5482` edge `0.0136` maxDD `-12.2409`
- `market_context_high->index_4h` score `-3.1753` n `149` status `ready` deltaP `-10.3986` edge `-0.0331` maxDD `-5.6417`
- `market_context_high->crypto_major_4h` score `-3.4037` n `149` status `ready` deltaP `2.2897` edge `-0.0197` maxDD `-27.2215`
- `market_context_high->metal_24h` score `-3.8745` n `148` status `ready` deltaP `-0.2393` edge `-0.0193` maxDD `-10.1587`
- `market_context_high->crypto_major_24h` score `-3.8917` n `148` status `ready` deltaP `-3.3174` edge `0.0089` maxDD `-29.1905`
- `market_context_high->equity_4h` score `-5.5162` n `149` status `ready` deltaP `-4.8494` edge `-0.1515` maxDD `-35.2032`
- `market_context_high->equity_24h` score `-5.8643` n `148` status `ready` deltaP `2.271` edge `-0.2074` maxDD `-15.7143`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
