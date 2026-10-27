# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T13:52:39.501755+00:00`
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

- `market_context_high->unknown_4h` score `80.4338` n `135` status `ready` deltaP `4.8521` edge `6.6857` maxDD `-0.5521`
- `market_context_high->unknown_1h` score `14.8704` n `135` status `ready` deltaP `1.069` edge `1.281` maxDD `-1.5807`
- `market_context_high->index_24h` score `1.9411` n `133` status `ready` deltaP `26.8422` edge `0.0516` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.4835` n `135` status `ready` deltaP `10.906` edge `0.0034` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.369` n `135` status `ready` deltaP `12.1341` edge `0.0097` maxDD `-0.4545`
- `market_context_high->metal_1h` score `0.0086` n `135` status `ready` deltaP `9.8969` edge `0.0098` maxDD `-1.3073`
- `market_context_high->commodity_1h` score `-0.301` n `135` status `ready` deltaP `2.128` edge `0.0108` maxDD `-1.0053`
- `market_context_high->crypto_major_1h` score `-0.4661` n `135` status `ready` deltaP `6.0357` edge `0.0283` maxDD `-6.9306`
- `market_context_high->index_1h` score `-0.5515` n `135` status `ready` deltaP `-0.0632` edge `-0.002` maxDD `-1.4631`
- `market_context_high->commodity_4h` score `-0.6145` n `135` status `ready` deltaP `4.5551` edge `0.0403` maxDD `-1.0837`
- `market_context_high->fx_24h` score `-0.6563` n `133` status `ready` deltaP `8.203` edge `0.0184` maxDD `-1.2451`
- `market_context_high->metal_4h` score `-0.7882` n `135` status `ready` deltaP `8.1662` edge `-0.0014` maxDD `-4.6603`
- `market_context_high->metal_24h` score `-1.0627` n `133` status `ready` deltaP `15.1275` edge `0.0884` maxDD `-8.2244`
- `market_context_high->equity_1h` score `-1.3778` n `135` status `ready` deltaP `2.4894` edge `-0.002` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.9265` n `135` status `ready` deltaP `-0.8916` edge `-0.0047` maxDD `-12.2409`
- `market_context_high->equity_24h` score `-2.3476` n `133` status `ready` deltaP `7.4693` edge `0.051` maxDD `-15.7143`
- `market_context_high->index_4h` score `-2.6731` n `135` status `ready` deltaP `-4.9458` edge `-0.0276` maxDD `-5.6417`
- `market_context_high->crypto_major_4h` score `-3.6536` n `135` status `ready` deltaP `3.9646` edge `-0.0629` maxDD `-27.2215`
- `market_context_high->crypto_major_24h` score `-4.2518` n `133` status `ready` deltaP `-0.4626` edge `-0.0563` maxDD `-29.1905`
- `market_context_high->equity_4h` score `-5.0642` n `135` status `ready` deltaP `1.9377` edge `-0.1388` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
