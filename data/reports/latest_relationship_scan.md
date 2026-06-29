# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T12:37:26.965607+00:00`
- Price records: `672`
- Market context records: `5144`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5596`

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

- `market_context_high->unknown_24h` score `25.7802` n `68` status `ready` deltaP `31.5462` edge `1.9723` maxDD `-1.4072`
- `market_context_high->unknown_4h` score `6.5033` n `127` status `ready` deltaP `18.5795` edge `0.5203` maxDD `-5.5109`
- `market_context_high->unknown_1h` score `5.8201` n `139` status `ready` deltaP `9.9535` edge `0.4828` maxDD `-2.7986`
- `market_context_high->crypto_alt_4h` score `4.9508` n `127` status `ready` deltaP `15.1779` edge `0.4713` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.6795` n `127` status `ready` deltaP `13.1205` edge `0.4484` maxDD `-14.0065`
- `market_context_high->equity_4h` score `0.9792` n `127` status `ready` deltaP `10.2998` edge `0.1768` maxDD `-7.4425`
- `market_context_high->crypto_alt_1h` score `0.9179` n `139` status `ready` deltaP `6.0817` edge `0.1321` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.9175` n `139` status `ready` deltaP `8.506` edge `0.1443` maxDD `-6.9639`
- `market_context_high->commodity_24h` score `0.7652` n `68` status `ready` deltaP `15.6862` edge `0.1168` maxDD `-5.1955`
- `market_context_high->equity_1h` score `0.7348` n `139` status `ready` deltaP `7.9115` edge `0.0678` maxDD `-2.745`
- `market_context_high->crypto_alt_24h` score `0.388` n `68` status `ready` deltaP `17.0241` edge `0.564` maxDD `-46.2794`
- `market_context_high->index_1h` score `-0.0205` n `139` status `ready` deltaP `5.1544` edge `0.0143` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.0237` n `139` status `ready` deltaP `5.4204` edge `0.0174` maxDD `-1.8592`
- `market_context_high->crypto_major_24h` score `-0.2198` n `68` status `ready` deltaP `15.3902` edge `0.563` maxDD `-48.0465`
- `market_context_high->metal_24h` score `-0.3731` n `68` status `ready` deltaP `-1.8587` edge `0.1696` maxDD `-10.0641`
- `market_context_high->index_4h` score `-0.3949` n `127` status `ready` deltaP `6.364` edge `0.0364` maxDD `-2.9391`
- `market_context_high->fx_24h` score `-0.4779` n `68` status `ready` deltaP `4.2279` edge `0.0004` maxDD `-0.8549`
- `market_context_high->fx_1h` score `-0.5561` n `139` status `ready` deltaP `-0.9004` edge `-0.0012` maxDD `-0.7944`
- `market_context_high->commodity_1h` score `-0.6191` n `139` status `ready` deltaP `-0.0312` edge `-0.0016` maxDD `-2.2056`
- `market_context_high->fx_4h` score `-0.863` n `127` status `ready` deltaP `-0.8006` edge `0.0015` maxDD `-1.8772`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
