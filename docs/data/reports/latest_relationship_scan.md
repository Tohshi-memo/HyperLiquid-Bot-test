# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T12:22:23.488643+00:00`
- Price records: `672`
- Market context records: `2560`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9198`

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

- `market_context_high->crypto_alt_4h` score `5.7611` n `149` status `ready` deltaP `25.3182` edge `0.5792` maxDD `-15.4319`
- `market_context_high->unknown_24h` score `4.9624` n `118` status `ready` deltaP `18.6087` edge `0.3223` maxDD `-1.626`
- `market_context_high->crypto_major_24h` score `4.8025` n `118` status `ready` deltaP `12.1704` edge `0.5844` maxDD `-15.2264`
- `market_context_high->crypto_major_4h` score `3.9327` n `149` status `ready` deltaP `17.4486` edge `0.3924` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `1.5801` n `149` status `ready` deltaP `9.5474` edge `0.173` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `1.2636` n `149` status `ready` deltaP `10.1756` edge `0.1562` maxDD `-6.1656`
- `market_context_high->equity_24h` score `1.1832` n `118` status `ready` deltaP `18.9972` edge `0.0303` maxDD `-2.0014`
- `market_context_high->crypto_major_1h` score `0.6886` n `149` status `ready` deltaP `8.2345` edge `0.1219` maxDD `-4.2199`
- `market_context_high->index_24h` score `0.6474` n `118` status `ready` deltaP `6.4383` edge `0.1091` maxDD `-2.5127`
- `market_context_high->crypto_alt_24h` score `0.1542` n `118` status `ready` deltaP `-0.9592` edge `0.6666` maxDD `-39.2351`
- `market_context_high->index_4h` score `0.0828` n `149` status `ready` deltaP `7.447` edge `0.0414` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1478` n `149` status `ready` deltaP `3.8983` edge `0.0111` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.3804` n `149` status `ready` deltaP `1.9672` edge `0.0242` maxDD `-2.8543`
- `market_context_high->metal_1h` score `-0.4309` n `149` status `ready` deltaP `1.3111` edge `0.0108` maxDD `-2.9823`
- `market_context_high->commodity_1h` score `-0.5254` n `149` status `ready` deltaP `4.2077` edge `0.016` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.5405` n `149` status `ready` deltaP `0.635` edge `0.0042` maxDD `-0.278`
- `market_context_high->equity_1h` score `-0.7362` n `149` status `ready` deltaP `0.3004` edge `0.0205` maxDD `-2.7085`
- `market_context_high->fx_24h` score `-0.7667` n `118` status `ready` deltaP `0.9093` edge `0.0033` maxDD `-1.946`
- `market_context_high->fx_4h` score `-0.8305` n `149` status `ready` deltaP `0.6087` edge `0.0127` maxDD `-0.8774`
- `market_context_high->metal_4h` score `-0.906` n `149` status `ready` deltaP `3.3823` edge `0.0407` maxDD `-4.7664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
