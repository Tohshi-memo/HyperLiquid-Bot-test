# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T17:07:44.856785+00:00`
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

- `market_context_high->unknown_4h` score `81.0562` n `135` status `ready` deltaP `4.5472` edge `6.7396` maxDD `-0.5521`
- `market_context_high->unknown_1h` score `8.5319` n `140` status `ready` deltaP `1.0522` edge `0.7529` maxDD `-1.5807`
- `market_context_high->index_24h` score `1.9915` n `135` status `ready` deltaP `27.1875` edge `0.0535` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.4871` n `140` status `ready` deltaP `10.9666` edge `0.0033` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.4225` n `135` status `ready` deltaP `12.7439` edge `0.0101` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.0454` n `140` status `ready` deltaP `9.1574` edge `0.0078` maxDD `-1.3073`
- `market_context_high->commodity_1h` score `-0.2729` n `140` status `ready` deltaP `2.3738` edge `0.0115` maxDD `-1.0053`
- `market_context_high->commodity_4h` score `-0.4206` n `135` status `ready` deltaP `6.0795` edge `0.0463` maxDD `-1.0837`
- `market_context_high->crypto_major_1h` score `-0.4318` n `140` status `ready` deltaP `6.6809` edge `0.0284` maxDD `-6.9306`
- `market_context_high->fx_24h` score `-0.5677` n `135` status `ready` deltaP `9.6528` edge `0.0201` maxDD `-1.2451`
- `market_context_high->index_1h` score `-0.5729` n `140` status `ready` deltaP `-0.4149` edge `-0.0024` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.8296` n `135` status `ready` deltaP `8.0137` edge `-0.0057` maxDD `-4.6603`
- `market_context_high->metal_24h` score `-0.9465` n `135` status `ready` deltaP `16.0995` edge `0.0916` maxDD `-8.2244`
- `market_context_high->equity_1h` score `-1.3817` n `140` status `ready` deltaP `2.4294` edge `-0.0021` maxDD `-9.2993`
- `market_context_high->equity_24h` score `-1.7994` n `135` status `ready` deltaP `8.0671` edge `0.0927` maxDD `-15.7143`
- `market_context_high->crypto_alt_1h` score `-1.9054` n `140` status `ready` deltaP `-0.4406` edge `-0.005` maxDD `-12.2409`
- `market_context_high->index_4h` score `-2.8905` n `135` status `ready` deltaP `-6.9276` edge `-0.0325` maxDD `-5.6417`
- `market_context_high->crypto_major_4h` score `-3.8071` n `135` status `ready` deltaP `3.2024` edge `-0.0775` maxDD `-27.2215`
- `market_context_high->crypto_major_24h` score `-3.8796` n `135` status `ready` deltaP `0.544` edge `-0.0153` maxDD `-29.1905`
- `market_context_high->equity_4h` score `-5.3963` n `135` status `ready` deltaP `0.2609` edge `-0.1702` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
