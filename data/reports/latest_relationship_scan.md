# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T03:07:18.093142+00:00`
- Price records: `672`
- Market context records: `2523`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9312`

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

- `market_context_high->unknown_24h` score `4.9067` n `119` status `ready` deltaP `19.548` edge `0.3114` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `4.7631` n `158` status `ready` deltaP `22.5031` edge `0.5148` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.4012` n `158` status `ready` deltaP `15.7398` edge `0.3595` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `2.2356` n `119` status `ready` deltaP `11.6363` edge `0.5983` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `2.105` n `158` status `ready` deltaP `11.8034` edge `0.2017` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `1.0667` n `162` status `ready` deltaP `8.8841` edge `0.1484` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `0.6453` n `162` status `ready` deltaP `7.9489` edge `0.1202` maxDD `-4.2199`
- `market_context_high->crypto_alt_24h` score `0.0219` n `119` status `ready` deltaP `0.8782` edge `0.6927` maxDD `-43.6595`
- `market_context_high->index_24h` score `0.0049` n `119` status `ready` deltaP `3.373` edge `0.076` maxDD `-2.5127`
- `market_context_high->equity_24h` score `-0.1862` n `119` status `ready` deltaP `17.8324` edge `0.0183` maxDD `-6.8828`
- `market_context_high->index_4h` score `-0.1906` n `158` status `ready` deltaP `6.3253` edge `0.0261` maxDD `-2.3986`
- `market_context_high->commodity_1h` score `-0.368` n `162` status `ready` deltaP `4.2083` edge `0.0126` maxDD `-4.3601`
- `market_context_high->index_1h` score `-0.3812` n `162` status `ready` deltaP `1.4009` edge `0.0083` maxDD `-1.2855`
- `market_context_high->metal_1h` score `-0.4874` n `162` status `ready` deltaP `0.73` edge `0.0086` maxDD `-3.0759`
- `market_context_high->fx_1h` score `-0.5321` n `162` status `ready` deltaP `0.7855` edge `0.0039` maxDD `-0.278`
- `market_context_high->unknown_1h` score `-0.6068` n `162` status `ready` deltaP `1.5894` edge `0.0108` maxDD `-3.0902`
- `market_context_high->equity_1h` score `-0.8029` n `162` status `ready` deltaP `0.0518` edge `0.0166` maxDD `-2.7085`
- `market_context_high->fx_4h` score `-0.8277` n `158` status `ready` deltaP `0.8085` edge `0.0116` maxDD `-0.8774`
- `market_context_high->fx_24h` score `-0.8599` n `119` status `ready` deltaP `3.0798` edge `0.0043` maxDD `-2.4729`
- `market_context_high->metal_4h` score `-0.8763` n `158` status `ready` deltaP `3.1086` edge `0.045` maxDD `-4.7664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
