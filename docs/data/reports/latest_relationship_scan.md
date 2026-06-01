# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T02:22:23.279655+00:00`
- Price records: `672`
- Market context records: `2520`
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

- `market_context_high->unknown_24h` score `4.9619` n `119` status `ready` deltaP `19.548` edge `0.316` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `4.7655` n `155` status `ready` deltaP `22.2934` edge `0.5164` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.6166` n `155` status `ready` deltaP `16.5578` edge `0.372` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `2.2602` n `119` status `ready` deltaP `11.8099` edge `0.6003` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `2.2221` n `155` status `ready` deltaP `12.322` edge `0.208` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `1.1015` n `162` status `ready` deltaP `8.8841` edge `0.1513` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `0.6981` n `162` status `ready` deltaP `8.2483` edge `0.1226` maxDD `-4.2199`
- `market_context_high->crypto_alt_24h` score `0.0352` n `119` status `ready` deltaP `0.8782` edge `0.6944` maxDD `-43.6595`
- `market_context_high->index_24h` score `-0.0066` n `119` status `ready` deltaP `3.1994` edge `0.0762` maxDD `-2.5127`
- `market_context_high->equity_24h` score `-0.155` n `119` status `ready` deltaP `17.8324` edge `0.0209` maxDD `-6.8828`
- `market_context_high->index_4h` score `-0.2012` n `155` status `ready` deltaP `6.132` edge `0.0265` maxDD `-2.3986`
- `market_context_high->commodity_1h` score `-0.396` n `162` status `ready` deltaP `3.7592` edge `0.012` maxDD `-4.3601`
- `market_context_high->index_1h` score `-0.3991` n `162` status `ready` deltaP `1.2512` edge `0.0078` maxDD `-1.2855`
- `market_context_high->metal_1h` score `-0.4757` n `162` status `ready` deltaP `0.8797` edge `0.0091` maxDD `-3.0759`
- `market_context_high->fx_1h` score `-0.4925` n `162` status `ready` deltaP `1.2346` edge `0.0042` maxDD `-0.278`
- `market_context_high->unknown_1h` score `-0.5409` n `162` status `ready` deltaP `2.0385` edge `0.0133` maxDD `-3.0902`
- `market_context_high->equity_1h` score `-0.785` n `162` status `ready` deltaP `0.2015` edge `0.0171` maxDD `-2.7085`
- `market_context_high->fx_24h` score `-0.8387` n `119` status `ready` deltaP `3.427` edge `0.0047` maxDD `-2.4729`
- `market_context_high->fx_4h` score `-0.8762` n `155` status `ready` deltaP `0.3226` edge `0.0108` maxDD `-0.8774`
- `market_context_high->metal_4h` score `-0.9618` n `155` status `ready` deltaP `2.5492` edge `0.0416` maxDD `-4.7664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
