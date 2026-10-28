# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T16:08:14.480166+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8520`

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

- `market_context_high->unknown_24h` score `1390.7855` n `140` status `ready` deltaP `-3.1002` edge `116.0122` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `22.1256` n `149` status `ready` deltaP `4.385` edge `1.8298` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.5129` n `140` status `ready` deltaP `25.0446` edge `0.0279` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.1757` n `149` status `ready` deltaP `7.269` edge `0.002` maxDD `-0.1986`
- `market_context_high->fx_4h` score `-0.0227` n `149` status `ready` deltaP `7.8388` edge `0.0057` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.0808` n `149` status `ready` deltaP `8.4767` edge `0.0078` maxDD `-1.3073`
- `market_context_high->crypto_major_1h` score `-0.2775` n `149` status `ready` deltaP `7.5785` edge `0.0422` maxDD `-6.9306`
- `market_context_high->commodity_4h` score `-0.3834` n `149` status `ready` deltaP `7.3539` edge `0.0409` maxDD `-1.0837`
- `market_context_high->fx_24h` score `-0.6152` n `140` status `ready` deltaP `12.5199` edge `0.0225` maxDD `-1.2451`
- `market_context_high->commodity_1h` score `-0.7051` n `149` status `ready` deltaP `-0.9394` edge `0.0059` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.7367` n `149` status `ready` deltaP `-3.4743` edge `-0.003` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.7442` n `149` status `ready` deltaP `9.0563` edge `-0.0017` maxDD `-4.6603`
- `market_context_high->equity_1h` score `-1.396` n `149` status `ready` deltaP `1.0891` edge `0.005` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.5494` n `149` status `ready` deltaP `2.8955` edge `0.0184` maxDD `-12.2409`
- `market_context_high->equity_24h` score `-2.7794` n `140` status `ready` deltaP `6.7064` edge `0.0201` maxDD `-15.7143`
- `market_context_high->metal_24h` score `-2.8846` n `140` status `ready` deltaP `2.386` edge `0.0288` maxDD `-8.8075`
- `market_context_high->index_4h` score `-3.003` n `149` status `ready` deltaP `-8.8742` edge `-0.0289` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.1495` n `140` status `ready` deltaP `1.7758` edge `0.0701` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.3616` n `149` status `ready` deltaP `4.119` edge `-0.0265` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.2976` n `149` status `ready` deltaP `-2.7152` edge `-0.1377` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
