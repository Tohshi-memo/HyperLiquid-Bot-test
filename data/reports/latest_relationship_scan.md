# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T10:07:14.981369+00:00`
- Price records: `672`
- Market context records: `1725`
- Flow alert records: `6871`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8838`

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

- `market_context_high->metal_24h` score `6.7035` n `144` status `ready` deltaP `25.7137` edge `0.6298` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `5.9305` n `196` status `ready` deltaP `21.1237` edge `0.53` maxDD `-9.1295`
- `market_context_high->unknown_24h` score `5.8637` n `144` status `ready` deltaP `16.9021` edge `0.908` maxDD `-35.8966`
- `market_context_high->crypto_major_4h` score `4.4586` n `196` status `ready` deltaP `23.1769` edge `0.4576` maxDD `-10.9117`
- `market_context_high->index_24h` score `3.9813` n `144` status `ready` deltaP `17.402` edge `0.3386` maxDD `-4.1604`
- `market_context_high->unknown_4h` score `3.0593` n `196` status `ready` deltaP `13.7941` edge `0.3901` maxDD `-11.1695`
- `market_context_high->equity_4h` score `3.0225` n `196` status `ready` deltaP `16.2643` edge `0.2529` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.7656` n `144` status `ready` deltaP `16.1813` edge `0.5291` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.7525` n `196` status `ready` deltaP `7.5706` edge `0.1146` maxDD `-4.1892`
- `market_context_high->index_4h` score `0.5505` n `196` status `ready` deltaP `8.8166` edge `0.096` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.1849` n `196` status `ready` deltaP `4.7477` edge `0.0911` maxDD `-3.9211`
- `market_context_high->crypto_alt_24h` score `0.0442` n `144` status `ready` deltaP `22.6187` edge `1.0338` maxDD `-88.8062`
- `market_context_high->equity_1h` score `0.0251` n `196` status `ready` deltaP `4.6713` edge `0.0518` maxDD `-2.8014`
- `market_context_high->metal_4h` score `-0.3377` n `196` status `ready` deltaP `11.8343` edge `0.147` maxDD `-12.5349`
- `market_context_high->index_1h` score `-0.4096` n `196` status `ready` deltaP `1.6712` edge `0.0179` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.5526` n `196` status `ready` deltaP `5.4962` edge `0.0261` maxDD `-6.3532`
- `market_context_high->fx_1h` score `-0.6638` n `196` status `ready` deltaP `-3.1162` edge `-0.0011` maxDD `-0.3914`
- `market_context_high->crypto_major_24h` score `-0.6655` n `144` status `ready` deltaP `21.04` edge `0.633` maxDD `-62.3533`
- `market_context_high->fx_24h` score `-0.7803` n `144` status `ready` deltaP `4.9621` edge `0.0068` maxDD `-1.3925`
- `market_context_high->unknown_1h` score `-1.4425` n `196` status `ready` deltaP `1.9858` edge `0.0135` maxDD `-7.7558`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
