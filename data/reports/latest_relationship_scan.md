# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T16:07:33.672271+00:00`
- Price records: `672`
- Market context records: `7684`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14676`

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

- `market_context_high->equity_24h` score `1.1591` n `138` status `ready` deltaP `15.7728` edge `0.1899` maxDD `-11.2101`
- `market_context_high->crypto_major_4h` score `0.4457` n `139` status `ready` deltaP `12.7423` edge `0.124` maxDD `-6.7444`
- `market_context_high->crypto_major_1h` score `0.4025` n `139` status `ready` deltaP `10.4317` edge `0.0303` maxDD `-3.3042`
- `market_context_high->equity_1h` score `0.172` n `139` status `ready` deltaP `6.7157` edge `0.0714` maxDD `-4.8627`
- `market_context_high->index_1h` score `0.1278` n `139` status `ready` deltaP `6.9286` edge `0.0132` maxDD `-0.7743`
- `market_context_high->fx_24h` score `-0.0999` n `138` status `ready` deltaP `11.2129` edge `0.0212` maxDD `-3.0343`
- `market_context_high->crypto_alt_4h` score `-0.1075` n `139` status `ready` deltaP `5.853` edge `0.089` maxDD `-5.958`
- `market_context_high->crypto_alt_1h` score `-0.1851` n `139` status `ready` deltaP `2.2767` edge `0.0238` maxDD `-2.6829`
- `market_context_high->equity_4h` score `-0.1893` n `139` status `ready` deltaP `1.8613` edge `0.2389` maxDD `-11.7133`
- `market_context_high->index_4h` score `-0.3689` n `139` status `ready` deltaP `10.2788` edge `0.0389` maxDD `-2.0444`
- `market_context_high->commodity_1h` score `-0.3721` n `139` status `ready` deltaP `1.9044` edge `0.0022` maxDD `-0.6722`
- `market_context_high->commodity_4h` score `-0.47` n `139` status `ready` deltaP `1.6335` edge `0.0093` maxDD `-1.0817`
- `market_context_high->fx_1h` score `-0.4744` n `139` status `ready` deltaP `0.1534` edge `-0.0012` maxDD `-0.4821`
- `market_context_high->metal_1h` score `-0.6574` n `139` status `ready` deltaP `0.6548` edge `0.0159` maxDD `-1.0307`
- `market_context_high->metal_24h` score `-1.2608` n `139` status `ready` deltaP `-0.2073` edge `0.0952` maxDD `-4.1037`
- `market_context_high->metal_4h` score `-1.2967` n `139` status `ready` deltaP `-0.2742` edge `0.0619` maxDD `-3.1054`
- `market_context_high->unknown_1h` score `-1.3704` n `139` status `ready` deltaP `-0.8088` edge `-0.0498` maxDD `-1.054`
- `market_context_high->commodity_24h` score `-1.4685` n `138` status `ready` deltaP `6.4763` edge `-0.0072` maxDD `-7.0012`
- `market_context_high->fx_4h` score `-2.4623` n `139` status `ready` deltaP `-5.6641` edge `-0.0036` maxDD `-1.7732`
- `market_context_high->index_24h` score `-3.0441` n `138` status `ready` deltaP `-20.0677` edge `-0.0196` maxDD `-4.2839`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
