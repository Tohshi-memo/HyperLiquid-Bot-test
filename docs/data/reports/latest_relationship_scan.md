# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T00:52:27.246667+00:00`
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

- `market_context_high->unknown_24h` score `474.0346` n `135` status `ready` deltaP `-3.7616` edge `39.6207` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `49.2862` n `148` status `ready` deltaP `5.0882` edge `4.0885` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.9399` n `135` status `ready` deltaP `27.1875` edge `0.0492` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.3553` n `148` status `ready` deltaP `9.3785` edge `0.0029` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.0894` n `148` status `ready` deltaP `8.7591` edge `0.0089` maxDD `-0.4545`
- `market_context_high->commodity_4h` score `-0.1209` n `148` status `ready` deltaP `8.6107` edge `0.0544` maxDD `-1.0837`
- `market_context_high->metal_1h` score `-0.1659` n `148` status `ready` deltaP `7.1249` edge `0.0059` maxDD `-1.3073`
- `market_context_high->fx_24h` score `-0.3704` n `135` status `ready` deltaP `12.9514` edge `0.0234` maxDD `-1.2451`
- `market_context_high->crypto_major_1h` score `-0.4343` n `148` status `ready` deltaP `6.7527` edge `0.0276` maxDD `-6.9306`
- `market_context_high->commodity_1h` score `-0.5411` n `148` status `ready` deltaP `0.526` edge `0.0098` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.7027` n `148` status `ready` deltaP `-2.6258` edge `-0.0043` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.8789` n `148` status `ready` deltaP `7.2759` edge `-0.0071` maxDD `-4.6603`
- `market_context_high->equity_24h` score `-1.2186` n `135` status `ready` deltaP `8.0671` edge `0.1411` maxDD `-15.7143`
- `market_context_high->equity_1h` score `-1.5029` n `148` status `ready` deltaP `1.1935` edge `-0.0094` maxDD `-9.2993`
- `market_context_high->metal_24h` score `-1.5725` n `135` status `ready` deltaP `11.0648` edge `0.073` maxDD `-8.2244`
- `market_context_high->crypto_alt_1h` score `-1.7685` n `148` status `ready` deltaP `1.7114` edge `-0.0018` maxDD `-12.2409`
- `market_context_high->index_4h` score `-3.0564` n `148` status `ready` deltaP `-8.6273` edge `-0.035` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.6066` n `135` status `ready` deltaP `0.544` edge `0.0197` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.8011` n `148` status `ready` deltaP `3.2713` edge `-0.0772` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.7814` n `148` status `ready` deltaP `-3.7698` edge `-0.1927` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
