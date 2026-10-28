# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T01:07:31.326446+00:00`
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

- `market_context_high->unknown_24h` score `579.4246` n `135` status `ready` deltaP `-3.7616` edge `48.4032` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `47.4298` n `148` status `ready` deltaP `5.0882` edge `3.9338` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.9387` n `135` status `ready` deltaP `27.1875` edge `0.0491` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.3421` n `148` status `ready` deltaP `9.2288` edge `0.0028` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.0894` n `148` status `ready` deltaP `8.7591` edge `0.0089` maxDD `-0.4545`
- `market_context_high->commodity_4h` score `-0.1415` n `148` status `ready` deltaP `8.4583` edge `0.0537` maxDD `-1.0837`
- `market_context_high->metal_1h` score `-0.1652` n `148` status `ready` deltaP `7.1249` edge `0.006` maxDD `-1.3073`
- `market_context_high->fx_24h` score `-0.3704` n `135` status `ready` deltaP `12.9514` edge `0.0234` maxDD `-1.2451`
- `market_context_high->crypto_major_1h` score `-0.4343` n `148` status `ready` deltaP `6.7527` edge `0.0276` maxDD `-6.9306`
- `market_context_high->commodity_1h` score `-0.5567` n `148` status `ready` deltaP `0.3763` edge `0.0095` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.7043` n `148` status `ready` deltaP `-2.6258` edge `-0.0045` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.8702` n `148` status `ready` deltaP `7.4283` edge `-0.007` maxDD `-4.6603`
- `market_context_high->equity_24h` score `-1.1982` n `135` status `ready` deltaP `8.0671` edge `0.1428` maxDD `-15.7143`
- `market_context_high->equity_1h` score `-1.517` n `148` status `ready` deltaP `1.0438` edge `-0.0102` maxDD `-9.2993`
- `market_context_high->metal_24h` score `-1.5948` n `135` status `ready` deltaP `10.8912` edge `0.0723` maxDD `-8.2244`
- `market_context_high->crypto_alt_1h` score `-1.7678` n `148` status `ready` deltaP `1.7114` edge `-0.0017` maxDD `-12.2409`
- `market_context_high->index_4h` score `-3.0576` n `148` status `ready` deltaP `-8.6273` edge `-0.0351` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.584` n `135` status `ready` deltaP `0.544` edge `0.0226` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.7957` n `148` status `ready` deltaP `3.2713` edge `-0.0765` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.7876` n `148` status `ready` deltaP `-3.7698` edge `-0.1935` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
