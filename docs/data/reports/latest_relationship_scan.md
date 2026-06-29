# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T06:52:31.665665+00:00`
- Price records: `672`
- Market context records: `5120`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5560`

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

- `market_context_high->unknown_24h` score `25.5173` n `68` status `ready` deltaP `28.8603` edge `1.9683` maxDD `-1.4072`
- `market_context_high->unknown_1h` score `8.1417` n `127` status `ready` deltaP `7.6689` edge `0.6915` maxDD `-2.7986`
- `market_context_high->unknown_4h` score `7.3613` n `115` status `ready` deltaP `20.5593` edge `0.5786` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `5.5438` n `115` status `ready` deltaP `15.9001` edge `0.5159` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.9551` n `115` status `ready` deltaP `13.5963` edge `0.4682` maxDD `-14.0065`
- `market_context_high->crypto_alt_1h` score `0.9533` n `127` status `ready` deltaP `6.9145` edge `0.1295` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.7327` n `127` status `ready` deltaP `7.8457` edge `0.1333` maxDD `-6.9639`
- `market_context_high->equity_1h` score `0.7103` n `127` status `ready` deltaP `7.8905` edge `0.0659` maxDD `-2.745`
- `market_context_high->equity_4h` score `0.2177` n `115` status `ready` deltaP `6.6119` edge `0.1477` maxDD `-7.4425`
- `market_context_high->commodity_24h` score `0.1991` n `68` status `ready` deltaP `15.6862` edge `0.0961` maxDD `-9.0118`
- `market_context_high->metal_1h` score `0.1951` n `127` status `ready` deltaP `7.5852` edge `0.0259` maxDD `-1.4501`
- `market_context_high->index_1h` score `0.0066` n `127` status `ready` deltaP `5.4175` edge `0.0148` maxDD `-1.0296`
- `market_context_high->index_4h` score `-0.4784` n `115` status `ready` deltaP `3.4663` edge `0.0273` maxDD `-2.9391`
- `market_context_high->metal_4h` score `-0.488` n `115` status `ready` deltaP `3.1442` edge `0.0575` maxDD `-4.6157`
- `market_context_high->fx_1h` score `-0.6598` n `127` status `ready` deltaP `-2.8337` edge `-0.0016` maxDD `-0.7944`
- `market_context_high->commodity_1h` score `-0.9028` n `127` status `ready` deltaP `0.4656` edge `-0.0014` maxDD `-2.155`
- `market_context_high->fx_4h` score `-1.0444` n `115` status `ready` deltaP `-4.0654` edge `0.0005` maxDD `-1.9169`
- `market_context_high->fx_24h` score `-1.5677` n `68` status `ready` deltaP `-3.5437` edge `-0.0096` maxDD `-1.4601`
- `market_context_high->metal_24h` score `-2.168` n `68` status `ready` deltaP `-1.8587` edge `0.0951` maxDD `-21.8529`
- `market_context_high->commodity_4h` score `-2.5111` n `115` status `ready` deltaP `-0.8537` edge `-0.0303` maxDD `-7.5281`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
