# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T09:22:26.051737+00:00`
- Price records: `672`
- Market context records: `3059`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6969`

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

- `market_context_high->crypto_alt_24h` score `16.6823` n `95` status `ready` deltaP `12.5146` edge `2.447` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `14.0651` n `95` status `ready` deltaP `45.5939` edge `0.8922` maxDD `-1.2589`
- `market_context_high->unknown_24h` score `13.3076` n `95` status `ready` deltaP `23.9456` edge `0.9958` maxDD `-1.7175`
- `market_context_high->index_24h` score `10.671` n `95` status `ready` deltaP `26.8092` edge `0.8194` maxDD `-4.7103`
- `market_context_high->equity_24h` score `10.2536` n `95` status `ready` deltaP `24.8337` edge `1.4242` maxDD `-18.3486`
- `market_context_high->commodity_4h` score `2.4758` n `129` status `ready` deltaP `16.9101` edge `0.1583` maxDD `-2.8438`
- `market_context_high->commodity_1h` score `-0.199` n `132` status `ready` deltaP `0.626` edge `0.0215` maxDD `-1.7142`
- `market_context_high->unknown_4h` score `-0.3488` n `129` status `ready` deltaP `2.3208` edge `0.0608` maxDD `-3.7602`
- `market_context_high->index_1h` score `-0.53` n `132` status `ready` deltaP `3.4703` edge `0.0152` maxDD `-4.5023`
- `market_context_high->fx_1h` score `-0.6286` n `132` status `ready` deltaP `-6.2285` edge `-0.0018` maxDD `-0.3147`
- `market_context_high->crypto_alt_1h` score `-0.7229` n `132` status `ready` deltaP `4.3776` edge `0.0911` maxDD `-14.7034`
- `market_context_high->fx_24h` score `-0.7733` n `95` status `ready` deltaP `0.0073` edge `-0.012` maxDD `-0.6418`
- `market_context_high->equity_1h` score `-1.0081` n `132` status `ready` deltaP `1.5242` edge `0.006` maxDD `-8.6319`
- `market_context_high->unknown_1h` score `-1.0263` n `132` status `ready` deltaP `3.3842` edge `-0.035` maxDD `-3.1801`
- `market_context_high->crypto_major_1h` score `-1.0534` n `132` status `ready` deltaP `3.1255` edge `0.0704` maxDD `-15.1032`
- `market_context_high->fx_4h` score `-1.1912` n `129` status `ready` deltaP `-9.437` edge `-0.0056` maxDD `-1.0693`
- `market_context_high->metal_1h` score `-1.24` n `132` status `ready` deltaP `-2.6357` edge `-0.0046` maxDD `-7.278`
- `market_context_high->index_4h` score `-1.2547` n `129` status `ready` deltaP `10.5525` edge `0.0597` maxDD `-17.6057`
- `market_context_high->crypto_alt_4h` score `-2.8916` n `129` status `ready` deltaP `18.1745` edge `0.3126` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-3.3536` n `129` status `ready` deltaP `8.5968` edge `0.0252` maxDD `-35.3306`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
