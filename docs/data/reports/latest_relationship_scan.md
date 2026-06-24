# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T08:52:27.005571+00:00`
- Price records: `672`
- Market context records: `4605`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9851`

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

- `market_context_high->unknown_1h` score `68.5666` n `148` status `ready` deltaP `6.777` edge `5.7146` maxDD `-2.0052`
- `market_context_high->unknown_4h` score `4.1983` n `148` status `ready` deltaP `8.9856` edge `0.411` maxDD `-4.6834`
- `market_context_high->commodity_1h` score `-0.4991` n `148` status `ready` deltaP `1.8611` edge `0.0256` maxDD `-2.0345`
- `market_context_high->fx_1h` score `-0.5337` n `148` status `ready` deltaP `-1.3595` edge `-0.0039` maxDD `-1.1038`
- `market_context_high->fx_4h` score `-0.7486` n `148` status `ready` deltaP `1.9158` edge `-0.0005` maxDD `-1.9927`
- `market_context_high->index_4h` score `-0.935` n `148` status `ready` deltaP `1.0506` edge `-0.0146` maxDD `-5.9823`
- `market_context_high->equity_1h` score `-0.9366` n `148` status `ready` deltaP `-2.9212` edge `-0.0019` maxDD `-5.5624`
- `market_context_high->commodity_4h` score `-1.144` n `148` status `ready` deltaP `3.9593` edge `0.0377` maxDD `-9.1941`
- `market_context_high->index_1h` score `-1.7272` n `148` status `ready` deltaP `-4.4951` edge `-0.0131` maxDD `-2.7358`
- `market_context_high->equity_4h` score `-1.8049` n `148` status `ready` deltaP `-1.5861` edge `-0.0439` maxDD `-8.8203`
- `market_context_high->unknown_24h` score `-2.342` n `146` status `ready` deltaP `2.7254` edge `-0.121` maxDD `-4.7201`
- `market_context_high->metal_1h` score `-2.9931` n `148` status `ready` deltaP `-4.5113` edge `-0.0885` maxDD `-17.8795`
- `market_context_high->commodity_24h` score `-4.6844` n `146` status `ready` deltaP `11.2847` edge `0.0593` maxDD `-29.3255`
- `market_context_high->fx_24h` score `-5.3236` n `146` status `ready` deltaP `-12.3311` edge `-0.0102` maxDD `-6.0982`
- `market_context_high->crypto_alt_1h` score `-5.5679` n `148` status `ready` deltaP `-2.3952` edge `-0.1193` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.822` n `148` status `ready` deltaP `-6.077` edge `-0.1527` maxDD `-27.356`
- `market_context_high->index_24h` score `-8.3716` n `146` status `ready` deltaP `-7.9576` edge `-0.1071` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-9.2648` n `148` status `ready` deltaP `-4.1818` edge `-0.2942` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-10.3841` n `148` status `ready` deltaP `-7.4571` edge `-0.3602` maxDD `-67.3775`
- `market_context_high->crypto_major_4h` score `-12.403` n `148` status `ready` deltaP `-6.1882` edge `-0.4545` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
