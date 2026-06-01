# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T11:52:25.314503+00:00`
- Price records: `672`
- Market context records: `2558`
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

- `market_context_high->crypto_alt_4h` score `5.7271` n `149` status `ready` deltaP `25.0133` edge `0.5784` maxDD `-15.4319`
- `market_context_high->unknown_24h` score `5.139` n `118` status `ready` deltaP `18.956` edge `0.3347` maxDD `-1.626`
- `market_context_high->crypto_major_24h` score `4.8445` n `118` status `ready` deltaP `12.1704` edge `0.5879` maxDD `-15.2264`
- `market_context_high->crypto_major_4h` score `3.9533` n `149` status `ready` deltaP `17.6011` edge `0.3931` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `1.6777` n `149` status `ready` deltaP `9.8522` edge `0.1791` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `1.2121` n `149` status `ready` deltaP `9.8762` edge `0.1539` maxDD `-6.1656`
- `market_context_high->equity_24h` score `1.188` n `118` status `ready` deltaP `18.9972` edge `0.0307` maxDD `-2.0014`
- `market_context_high->index_24h` score `0.6792` n `118` status `ready` deltaP `6.6119` edge `0.1106` maxDD `-2.5127`
- `market_context_high->crypto_major_1h` score `0.6778` n `149` status `ready` deltaP `8.2345` edge `0.121` maxDD `-4.2199`
- `market_context_high->crypto_alt_24h` score `0.1542` n `118` status `ready` deltaP `-0.9592` edge `0.6666` maxDD `-39.2351`
- `market_context_high->index_4h` score `0.05` n `149` status `ready` deltaP `7.1421` edge `0.0407` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1753` n `149` status `ready` deltaP `3.5989` edge `0.0108` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.3072` n `149` status `ready` deltaP `2.2666` edge `0.0283` maxDD `-2.8543`
- `market_context_high->metal_1h` score `-0.4441` n `149` status `ready` deltaP `1.1614` edge `0.0101` maxDD `-2.9823`
- `market_context_high->fx_1h` score `-0.5285` n `149` status `ready` deltaP `0.7847` edge `0.0042` maxDD `-0.278`
- `market_context_high->commodity_1h` score `-0.5386` n `149` status `ready` deltaP `4.2077` edge `0.0149` maxDD `-4.3601`
- `market_context_high->fx_24h` score `-0.7652` n `118` status `ready` deltaP `0.9093` edge `0.0035` maxDD `-1.946`
- `market_context_high->equity_1h` score `-0.7698` n `149` status `ready` deltaP `0.001` edge `0.0197` maxDD `-2.7085`
- `market_context_high->fx_4h` score `-0.8561` n `149` status `ready` deltaP `0.3038` edge `0.0126` maxDD `-0.8774`
- `market_context_high->metal_4h` score `-0.883` n `149` status `ready` deltaP `3.5348` edge `0.0416` maxDD `-4.7664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
