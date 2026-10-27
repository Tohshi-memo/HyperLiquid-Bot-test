# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T18:37:29.451778+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8651`

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

- `market_context_high->unknown_4h` score `80.5306` n `135` status `ready` deltaP `4.5472` edge `6.6958` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.9831` n `135` status `ready` deltaP `27.1875` edge `0.0528` maxDD `-2.17`
- `market_context_high->unknown_1h` score `1.3243` n `146` status `ready` deltaP `0.6275` edge `0.1551` maxDD `-1.5807`
- `market_context_high->fx_4h` score `0.4383` n `135` status `ready` deltaP `12.8963` edge `0.0104` maxDD `-0.4545`
- `market_context_high->fx_1h` score `0.4269` n `146` status `ready` deltaP `10.2288` edge `0.0032` maxDD `-0.1986`
- `market_context_high->metal_1h` score `-0.0715` n `146` status `ready` deltaP `8.6867` edge `0.0076` maxDD `-1.3073`
- `market_context_high->commodity_4h` score `-0.3222` n `135` status `ready` deltaP `6.9941` edge `0.0484` maxDD `-1.0837`
- `market_context_high->crypto_major_1h` score `-0.3664` n `146` status `ready` deltaP `7.4891` edge `0.0314` maxDD `-6.9306`
- `market_context_high->commodity_1h` score `-0.4167` n `146` status `ready` deltaP `0.7711` edge `0.0102` maxDD `-1.0053`
- `market_context_high->fx_24h` score `-0.5034` n `135` status `ready` deltaP `10.6945` edge `0.0214` maxDD `-1.2451`
- `market_context_high->index_1h` score `-0.6333` n `146` status `ready` deltaP `-1.456` edge `-0.0032` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.8659` n `135` status `ready` deltaP `7.5564` edge `-0.0073` maxDD `-4.6603`
- `market_context_high->metal_24h` score `-1.0201` n `135` status `ready` deltaP `15.4051` edge `0.0901` maxDD `-8.2244`
- `market_context_high->equity_1h` score `-1.4507` n `146` status `ready` deltaP `1.3883` edge `-0.004` maxDD `-9.2993`
- `market_context_high->equity_24h` score `-1.6866` n `135` status `ready` deltaP `8.0671` edge `0.1021` maxDD `-15.7143`
- `market_context_high->crypto_alt_1h` score `-1.7271` n `146` status `ready` deltaP `1.8784` edge `0.0024` maxDD `-12.2409`
- `market_context_high->index_4h` score `-2.9936` n `135` status `ready` deltaP `-7.8422` edge `-0.035` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.7759` n `135` status `ready` deltaP `0.544` edge `-0.002` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.8853` n `135` status `ready` deltaP `2.8975` edge `-0.0855` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.5702` n `135` status `ready` deltaP `-0.6538` edge `-0.1864` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
