# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T05:52:24.641028+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8825`

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

- `market_context_high->unknown_24h` score `1162.8346` n `135` status `ready` deltaP `-3.7616` edge `97.0207` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `42.7992` n `148` status `ready` deltaP `5.2406` edge `3.5469` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.9171` n `135` status `ready` deltaP `27.1875` edge `0.0473` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.305` n `148` status `ready` deltaP `8.7797` edge `0.0027` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.0556` n `148` status `ready` deltaP `8.6066` edge `0.0071` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.0585` n `148` status `ready` deltaP `8.7716` edge `0.0087` maxDD `-1.3073`
- `market_context_high->crypto_major_1h` score `-0.3119` n `148` status `ready` deltaP `7.3515` edge `0.0393` maxDD `-6.9306`
- `market_context_high->fx_24h` score `-0.3994` n `135` status `ready` deltaP `12.6042` edge `0.022` maxDD `-1.2451`
- `market_context_high->commodity_4h` score `-0.5734` n `148` status `ready` deltaP `5.7144` edge `0.036` maxDD `-1.0837`
- `market_context_high->metal_4h` score `-0.6699` n `148` status `ready` deltaP `10.0198` edge `0.0014` maxDD `-4.6603`
- `market_context_high->index_1h` score `-0.7082` n `148` status `ready` deltaP `-2.9252` edge `-0.003` maxDD `-1.4631`
- `market_context_high->commodity_1h` score `-0.7377` n `148` status `ready` deltaP `-1.1207` edge `0.0044` maxDD `-1.0053`
- `market_context_high->equity_24h` score `-1.1466` n `135` status `ready` deltaP `8.0671` edge `0.1471` maxDD `-15.7143`
- `market_context_high->equity_1h` score `-1.4989` n `148` status `ready` deltaP `0.2953` edge `-0.0029` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.5822` n `148` status `ready` deltaP `2.7593` edge `0.0151` maxDD `-12.2409`
- `market_context_high->metal_24h` score `-1.7736` n `135` status `ready` deltaP `9.6759` edge `0.0655` maxDD `-8.2244`
- `market_context_high->index_4h` score `-2.9962` n `148` status `ready` deltaP `-8.4748` edge `-0.031` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.1956` n `135` status `ready` deltaP `0.544` edge `0.0724` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.5281` n `148` status `ready` deltaP `3.2713` edge `-0.0422` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.6115` n `148` status `ready` deltaP `-3.9222` edge `-0.1699` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
