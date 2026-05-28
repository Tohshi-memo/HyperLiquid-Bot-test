# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T07:07:17.331264+00:00`
- Price records: `672`
- Market context records: `2118`
- Flow alert records: `7994`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9149`

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

- `market_context_high->crypto_alt_4h` score `13.0021` n `163` status `ready` deltaP `37.1016` edge `0.9298` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.843` n `163` status `ready` deltaP `41.5523` edge `0.7629` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `6.1226` n `163` status `ready` deltaP `24.6942` edge `0.4205` maxDD `-2.6599`
- `market_context_high->equity_4h` score `5.0379` n `163` status `ready` deltaP `26.126` edge `0.3551` maxDD `-5.0894`
- `market_context_high->metal_4h` score `3.1018` n `163` status `ready` deltaP `21.1395` edge `0.2563` maxDD `-4.7664`
- `market_context_high->index_4h` score `3.056` n `163` status `ready` deltaP `22.1439` edge `0.1754` maxDD `-1.8022`
- `market_context_high->index_24h` score `2.8084` n `162` status `ready` deltaP `12.3563` edge `0.2745` maxDD `-4.1604`
- `market_context_high->crypto_major_1h` score `2.5934` n `163` status `ready` deltaP `16.0345` edge `0.1914` maxDD `-2.9075`
- `market_context_high->crypto_alt_1h` score `2.5251` n `163` status `ready` deltaP `13.3399` edge `0.2162` maxDD `-4.9097`
- `market_context_high->equity_24h` score `1.9286` n `162` status `ready` deltaP `23.7238` edge `0.4924` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `1.6607` n `162` status `ready` deltaP `24.1403` edge `0.5095` maxDD `-35.8966`
- `market_context_high->crypto_major_24h` score `0.8871` n `162` status `ready` deltaP `20.6267` edge `0.8348` maxDD `-62.3533`
- `market_context_high->equity_1h` score `0.7073` n `163` status `ready` deltaP `9.3568` edge `0.0754` maxDD `-2.6402`
- `market_context_high->metal_1h` score `0.3967` n `163` status `ready` deltaP `7.6393` edge `0.0492` maxDD `-2.3654`
- `market_context_high->unknown_1h` score `0.0672` n `163` status `ready` deltaP `5.1091` edge `0.0435` maxDD `-3.0902`
- `market_context_high->metal_24h` score `-0.0252` n `162` status `ready` deltaP `10.9189` edge `0.3141` maxDD `-23.2095`
- `market_context_high->index_1h` score `-0.0536` n `163` status `ready` deltaP `3.7765` edge `0.0294` maxDD `-1.3898`
- `market_context_high->fx_24h` score `-0.0849` n `162` status `ready` deltaP `14.567` edge `0.0313` maxDD `-2.811`
- `market_context_high->fx_1h` score `-0.6456` n `163` status `ready` deltaP `-3.0748` edge `0.0005` maxDD `-0.3548`
- `market_context_high->fx_4h` score `-1.072` n `163` status `ready` deltaP `-7.1889` edge `-0.0025` maxDD `-0.9612`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
