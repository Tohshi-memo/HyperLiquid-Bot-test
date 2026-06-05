# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T06:22:22.726987+00:00`
- Price records: `672`
- Market context records: `2943`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6954`

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

- `market_context_high->crypto_alt_24h` score `16.5742` n `138` status `ready` deltaP `15.5193` edge `1.6694` maxDD `-22.6673`
- `market_context_high->equity_24h` score `7.9352` n `138` status `ready` deltaP `18.3651` edge `0.7392` maxDD `-12.6963`
- `market_context_high->unknown_24h` score `7.0936` n `138` status `ready` deltaP `16.4704` edge `0.5278` maxDD `-1.7175`
- `market_context_high->index_24h` score `2.9111` n `138` status `ready` deltaP `14.3946` edge `0.2447` maxDD `-2.5127`
- `market_context_high->commodity_24h` score `2.5821` n `138` status `ready` deltaP `17.3988` edge `0.3789` maxDD `-11.3773`
- `market_context_high->equity_4h` score `1.1143` n `139` status `ready` deltaP `9.1321` edge `0.1572` maxDD `-5.3509`
- `market_context_high->index_4h` score `0.7855` n `139` status `ready` deltaP `15.5773` edge `0.081` maxDD `-2.3986`
- `market_context_high->unknown_4h` score `0.2495` n `139` status `ready` deltaP `4.0237` edge `0.0993` maxDD `-3.7602`
- `market_context_high->crypto_alt_4h` score `0.2404` n `139` status `ready` deltaP `16.5051` edge `0.3703` maxDD `-30.8239`
- `market_context_high->index_1h` score `0.0459` n `139` status `ready` deltaP `5.3375` edge `0.0197` maxDD `-1.2855`
- `market_context_high->equity_1h` score `-0.452` n `139` status `ready` deltaP `0.2143` edge `0.0442` maxDD `-2.6634`
- `market_context_high->crypto_alt_1h` score `-0.4526` n `139` status `ready` deltaP `5.246` edge `0.083` maxDD `-10.747`
- `market_context_high->unknown_1h` score `-0.5242` n `139` status `ready` deltaP `2.3101` edge `0.014` maxDD `-3.1801`
- `market_context_high->crypto_major_1h` score `-0.5974` n `139` status `ready` deltaP `5.3623` edge `0.0746` maxDD `-9.622`
- `market_context_high->fx_1h` score `-0.6042` n `139` status `ready` deltaP `-1.287` edge `0.0026` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.6498` n `139` status `ready` deltaP `-0.9251` edge `-0.0018` maxDD `-4.3601`
- `market_context_high->metal_1h` score `-0.6542` n `139` status `ready` deltaP `0.056` edge `0.0045` maxDD `-3.4325`
- `market_context_high->fx_4h` score `-0.9156` n `139` status `ready` deltaP `-0.8598` edge `0.0073` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.2439` n `139` status `ready` deltaP `2.0902` edge `0.0186` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.3895` n `138` status `ready` deltaP `-2.3852` edge `-0.0127` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
