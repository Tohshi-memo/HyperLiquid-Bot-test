# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T06:07:26.110516+00:00`
- Price records: `672`
- Market context records: `5426`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11450`

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

- `market_context_high->crypto_major_24h` score `4.9186` n `185` status `ready` deltaP `20.7161` edge `0.7258` maxDD `-29.6555`
- `market_context_high->equity_24h` score `4.8435` n `185` status `ready` deltaP `11.8694` edge `0.6781` maxDD `-21.6219`
- `market_context_high->crypto_major_4h` score `3.951` n `196` status `ready` deltaP `17.0701` edge `0.4447` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `3.124` n `196` status `ready` deltaP `12.4378` edge `0.3415` maxDD `-9.46`
- `market_context_high->equity_4h` score `2.6282` n `196` status `ready` deltaP `12.3569` edge `0.3005` maxDD `-7.4425`
- `market_context_high->equity_1h` score `0.4853` n `196` status `ready` deltaP `8.2305` edge `0.0821` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.1605` n `196` status `ready` deltaP `6.9321` edge `0.0165` maxDD `-0.9472`
- `market_context_high->fx_24h` score `0.0304` n `185` status `ready` deltaP `8.7406` edge `0.0338` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `-0.1785` n `196` status `ready` deltaP `1.8575` edge `0.0689` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.2365` n `196` status `ready` deltaP `3.1712` edge `0.0837` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.389` n `196` status `ready` deltaP `2.8504` edge `0.0161` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.5682` n `196` status `ready` deltaP `0.2444` edge `-0.0001` maxDD `-0.577`
- `market_context_high->index_4h` score `-0.9203` n `196` status `ready` deltaP `6.6202` edge `0.0401` maxDD `-2.874`
- `market_context_high->index_24h` score `-1.0626` n `185` status `ready` deltaP `16.1627` edge `0.1023` maxDD `-12.5551`
- `market_context_high->fx_4h` score `-1.1562` n `196` status `ready` deltaP `0.5942` edge `0.0022` maxDD `-1.5345`
- `market_context_high->commodity_1h` score `-1.5296` n `196` status `ready` deltaP `-3.7822` edge `-0.0078` maxDD `-3.5563`
- `market_context_high->metal_4h` score `-2.7592` n `196` status `ready` deltaP `-9.3423` edge `-0.039` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.4251` n `196` status `ready` deltaP `-8.1943` edge `-0.0503` maxDD `-14.1062`
- `market_context_high->crypto_alt_24h` score `-5.6607` n `185` status `ready` deltaP `11.4283` edge `0.3218` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.3379` n `185` status `ready` deltaP `-5.7742` edge `-0.1645` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
