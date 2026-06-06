# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T13:52:27.178699+00:00`
- Price records: `672`
- Market context records: `3079`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6901`

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

- `market_context_high->crypto_alt_24h` score `17.38` n `88` status `ready` deltaP `12.0265` edge `2.5397` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `15.3681` n `88` status `ready` deltaP `48.2165` edge `0.9833` maxDD `-1.2589`
- `market_context_high->unknown_24h` score `14.0228` n `88` status `ready` deltaP `23.3901` edge `1.0591` maxDD `-1.7175`
- `market_context_high->index_24h` score `13.2063` n `88` status `ready` deltaP `32.6705` edge `0.9666` maxDD `-4.7103`
- `market_context_high->equity_24h` score `11.5252` n `88` status `ready` deltaP `25.363` edge `1.5837` maxDD `-18.3486`
- `market_context_high->commodity_4h` score `2.5979` n `125` status `ready` deltaP `16.3598` edge `0.155` maxDD `-2.1389`
- `market_context_high->unknown_4h` score `-0.1591` n `125` status `ready` deltaP `3.0268` edge `0.0719` maxDD `-3.7602`
- `market_context_high->commodity_1h` score `-0.327` n `126` status `ready` deltaP `-0.8982` edge `0.021` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.6334` n `126` status `ready` deltaP `1.9461` edge `0.0121` maxDD `-4.5023`
- `market_context_high->fx_24h` score `-0.7419` n `88` status `ready` deltaP `-0.6787` edge `-0.0034` maxDD `-0.6418`
- `market_context_high->crypto_alt_1h` score `-0.7956` n `126` status `ready` deltaP `3.234` edge `0.0894` maxDD `-14.7034`
- `market_context_high->fx_1h` score `-1.0103` n `126` status `ready` deltaP `-6.7389` edge `-0.002` maxDD `-0.3147`
- `market_context_high->unknown_1h` score `-1.1242` n `126` status `ready` deltaP `1.0646` edge `-0.0277` maxDD `-3.1801`
- `market_context_high->equity_1h` score `-1.2025` n `126` status `ready` deltaP `-1.0931` edge `-0.0002` maxDD `-8.7345`
- `market_context_high->fx_4h` score `-1.3345` n `125` status `ready` deltaP `-12.0939` edge `-0.0061` maxDD `-1.0829`
- `market_context_high->index_4h` score `-1.4461` n `125` status `ready` deltaP `8.4012` edge `0.0495` maxDD `-17.6057`
- `market_context_high->crypto_major_1h` score `-1.8925` n `126` status `ready` deltaP `0.6273` edge `0.0644` maxDD `-15.1032`
- `market_context_high->metal_1h` score `-2.2182` n `126` status `ready` deltaP `-6.1259` edge `-0.0072` maxDD `-7.278`
- `market_context_high->crypto_alt_4h` score `-3.0086` n `125` status `ready` deltaP `18.3098` edge `0.2967` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-3.779` n `125` status `ready` deltaP `6.6098` edge `-0.0047` maxDD `-36.242`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
