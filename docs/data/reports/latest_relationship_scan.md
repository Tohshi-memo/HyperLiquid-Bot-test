# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T23:37:32.998675+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8775`

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

- `market_context_high->unknown_4h` score `49.297` n `148` status `ready` deltaP `5.0882` edge `4.0894` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.9435` n `135` status `ready` deltaP `27.1875` edge `0.0495` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.3936` n `148` status `ready` deltaP `9.8276` edge `0.0031` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.0772` n `148` status `ready` deltaP `8.6066` edge `0.0089` maxDD `-0.4545`
- `market_context_high->commodity_4h` score `-0.0637` n `148` status `ready` deltaP `9.2205` edge `0.0551` maxDD `-1.0837`
- `market_context_high->metal_1h` score `-0.155` n `148` status `ready` deltaP `7.2746` edge `0.0063` maxDD `-1.3073`
- `market_context_high->fx_24h` score `-0.4179` n `135` status `ready` deltaP `12.0833` edge `0.0231` maxDD `-1.2451`
- `market_context_high->crypto_major_1h` score `-0.4437` n `148` status `ready` deltaP `6.603` edge `0.0274` maxDD `-6.9306`
- `market_context_high->commodity_1h` score `-0.5267` n `148` status `ready` deltaP `0.6757` edge `0.01` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.684` n `148` status `ready` deltaP `-2.3264` edge `-0.0039` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.8299` n `148` status `ready` deltaP `8.0381` edge `-0.0059` maxDD `-4.6603`
- `market_context_high->equity_24h` score `-1.329` n `135` status `ready` deltaP `8.0671` edge `0.1319` maxDD `-15.7143`
- `market_context_high->equity_1h` score `-1.4554` n `148` status `ready` deltaP `1.6426` edge `-0.0063` maxDD `-9.2993`
- `market_context_high->metal_24h` score `-1.4574` n `135` status `ready` deltaP `11.9329` edge `0.0768` maxDD `-8.2244`
- `market_context_high->crypto_alt_1h` score `-1.742` n `148` status `ready` deltaP `2.0108` edge `-0.0004` maxDD `-12.2409`
- `market_context_high->index_4h` score `-3.0236` n `148` status `ready` deltaP `-8.3224` edge `-0.0343` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.7088` n `135` status `ready` deltaP `0.544` edge `0.0066` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.8058` n `148` status `ready` deltaP `3.2713` edge `-0.0778` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.7084` n `148` status `ready` deltaP `-3.16` edge `-0.1874` maxDD `-35.2032`
- `market_context_high->commodity_24h` score `-6.8288` n `135` status `ready` deltaP `2.0023` edge `-0.0234` maxDD `-24.0547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
