# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T00:07:27.600563+00:00`
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

- `market_context_high->unknown_24h` score `157.9906` n `135` status `ready` deltaP `-3.7616` edge `13.2837` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `49.2454` n `148` status `ready` deltaP `5.0882` edge `4.0851` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.9423` n `135` status `ready` deltaP `27.1875` edge `0.0494` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.3685` n `148` status `ready` deltaP `9.5282` edge `0.003` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.0906` n `148` status `ready` deltaP `8.7591` edge `0.009` maxDD `-0.4545`
- `market_context_high->commodity_4h` score `-0.0759` n `148` status `ready` deltaP `9.068` edge `0.0551` maxDD `-1.0837`
- `market_context_high->metal_1h` score `-0.1644` n `148` status `ready` deltaP `7.1249` edge `0.0061` maxDD `-1.3073`
- `market_context_high->fx_24h` score `-0.3983` n `135` status `ready` deltaP `12.4306` edge `0.0233` maxDD `-1.2451`
- `market_context_high->crypto_major_1h` score `-0.4452` n `148` status `ready` deltaP `6.603` edge `0.0272` maxDD `-6.9306`
- `market_context_high->commodity_1h` score `-0.5255` n `148` status `ready` deltaP `0.6757` edge `0.0101` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.6934` n `148` status `ready` deltaP `-2.4761` edge `-0.0041` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.852` n `148` status `ready` deltaP `7.7332` edge `-0.0067` maxDD `-4.6603`
- `market_context_high->equity_24h` score `-1.2822` n `135` status `ready` deltaP `8.0671` edge `0.1358` maxDD `-15.7143`
- `market_context_high->equity_1h` score `-1.4827` n `148` status `ready` deltaP `1.3432` edge `-0.0078` maxDD `-9.2993`
- `market_context_high->metal_24h` score `-1.5032` n `135` status `ready` deltaP `11.5856` edge `0.0753` maxDD `-8.2244`
- `market_context_high->crypto_alt_1h` score `-1.7576` n `148` status `ready` deltaP `1.8611` edge `-0.0014` maxDD `-12.2409`
- `market_context_high->index_4h` score `-3.0418` n `148` status `ready` deltaP `-8.4748` edge `-0.0348` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.6714` n `135` status `ready` deltaP `0.544` edge `0.0114` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.8066` n `148` status `ready` deltaP `3.2713` edge `-0.0779` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.7445` n `148` status `ready` deltaP `-3.4649` edge `-0.19` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
