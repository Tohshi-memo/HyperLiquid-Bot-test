# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T23:37:27.545495+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8280`

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

- `market_context_high->unknown_24h` score `1250.8071` n `148` status `ready` deltaP `-2.135` edge `104.3409` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `21.3552` n `149` status `ready` deltaP `4.385` edge `1.7656` maxDD `-0.5521`
- `market_context_high->index_24h` score `0.9627` n `148` status `ready` deltaP `20.763` edge `0.0106` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.2691` n `149` status `ready` deltaP `8.4666` edge `0.0018` maxDD `-0.1986`
- `market_context_high->fx_4h` score `-0.0249` n `149` status `ready` deltaP `7.9913` edge `0.0045` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.1089` n `149` status `ready` deltaP `8.1773` edge `0.0062` maxDD `-1.3073`
- `market_context_high->commodity_4h` score `-0.3673` n `149` status `ready` deltaP `7.8112` edge `0.0392` maxDD `-1.0837`
- `market_context_high->crypto_major_1h` score `-0.3679` n `149` status `ready` deltaP `6.5306` edge `0.0376` maxDD `-6.9306`
- `market_context_high->commodity_1h` score `-0.6153` n `149` status `ready` deltaP `-0.1909` edge `0.0084` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.7515` n `149` status `ready` deltaP `-3.7737` edge `-0.0029` maxDD `-1.4631`
- `market_context_high->fx_24h` score `-0.8113` n `148` status `ready` deltaP `10.3228` edge `0.0208` maxDD `-1.2451`
- `market_context_high->metal_4h` score `-0.8666` n `149` status `ready` deltaP `7.227` edge `-0.0052` maxDD `-4.6603`
- `market_context_high->equity_1h` score `-1.4179` n `149` status `ready` deltaP `0.9394` edge `0.0032` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.5821` n `149` status `ready` deltaP `2.7458` edge `0.0152` maxDD `-12.2409`
- `market_context_high->index_4h` score `-3.059` n `149` status `ready` deltaP `-9.484` edge `-0.0295` maxDD `-5.6417`
- `market_context_high->crypto_major_4h` score `-3.4159` n `149` status `ready` deltaP `3.5092` edge `-0.0294` maxDD `-27.2215`
- `market_context_high->metal_24h` score `-3.5901` n `148` status `ready` deltaP `-0.2393` edge `0.0044` maxDD `-10.1587`
- `market_context_high->crypto_major_24h` score `-3.8095` n `148` status `ready` deltaP `-2.6229` edge `0.0148` maxDD `-29.1905`
- `market_context_high->equity_24h` score `-4.5017` n `148` status `ready` deltaP `3.3126` edge `-0.1008` maxDD `-15.7143`
- `market_context_high->equity_4h` score `-5.4595` n `149` status `ready` deltaP `-4.2396` edge `-0.1483` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
