# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T14:22:34.227038+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8856`

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

- `market_context_high->unknown_4h` score `80.382` n `135` status `ready` deltaP `4.6997` edge `6.6824` maxDD `-0.5521`
- `market_context_high->unknown_1h` score `14.856` n `135` status `ready` deltaP `0.9193` edge `1.2808` maxDD `-1.5807`
- `market_context_high->index_24h` score `1.9845` n `134` status `ready` deltaP `27.0549` edge `0.0538` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.5074` n `135` status `ready` deltaP `11.2054` edge `0.0034` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.3556` n `135` status `ready` deltaP `11.9817` edge `0.0096` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.0101` n `135` status `ready` deltaP `9.5975` edge `0.0094` maxDD `-1.3073`
- `market_context_high->commodity_1h` score `-0.2746` n `135` status `ready` deltaP `2.4274` edge `0.011` maxDD `-1.0053`
- `market_context_high->crypto_major_1h` score `-0.4638` n `135` status `ready` deltaP `6.0357` edge `0.0286` maxDD `-6.9306`
- `market_context_high->index_1h` score `-0.5515` n `135` status `ready` deltaP `-0.0632` edge `-0.002` maxDD `-1.4631`
- `market_context_high->commodity_4h` score `-0.5782` n `135` status `ready` deltaP `4.86` edge `0.0413` maxDD `-1.0837`
- `market_context_high->fx_24h` score `-0.6605` n `134` status `ready` deltaP `8.1079` edge `0.0185` maxDD `-1.2451`
- `market_context_high->metal_4h` score `-0.8023` n `135` status `ready` deltaP `8.0137` edge `-0.0022` maxDD `-4.6603`
- `market_context_high->metal_24h` score `-0.9981` n `134` status `ready` deltaP `15.6794` edge `0.0901` maxDD `-8.2244`
- `market_context_high->equity_1h` score `-1.4043` n `135` status `ready` deltaP `2.19` edge `-0.0034` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.9164` n `135` status `ready` deltaP `-0.7419` edge `-0.0044` maxDD `-12.2409`
- `market_context_high->equity_24h` score `-2.1334` n `134` status `ready` deltaP `7.8073` edge `0.0666` maxDD `-15.7143`
- `market_context_high->index_4h` score `-2.7059` n `135` status `ready` deltaP `-5.2507` edge `-0.0283` maxDD `-5.6417`
- `market_context_high->crypto_major_4h` score `-3.7014` n `135` status `ready` deltaP `3.6597` edge `-0.067` maxDD `-27.2215`
- `market_context_high->crypto_major_24h` score `-4.1396` n `134` status `ready` deltaP `0.0` edge `-0.045` maxDD `-29.1905`
- `market_context_high->equity_4h` score `-5.119` n `135` status `ready` deltaP `1.6328` edge `-0.1438` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
