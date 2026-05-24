# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T04:37:20.306422+00:00`
- Price records: `672`
- Market context records: `1700`
- Flow alert records: `6803`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8854`

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

- `market_context_high->unknown_24h` score `8.7021` n `139` status `ready` deltaP `18.9478` edge `1.1309` maxDD `-35.8966`
- `market_context_high->metal_24h` score `6.3438` n `139` status `ready` deltaP `25.3578` edge `0.6022` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `4.9538` n `195` status `ready` deltaP `21.1851` edge `0.538` maxDD `-16.3135`
- `market_context_high->crypto_major_4h` score `3.9301` n `195` status `ready` deltaP `22.5437` edge `0.4481` maxDD `-13.3376`
- `market_context_high->index_24h` score `3.8008` n `139` status `ready` deltaP `16.6251` edge `0.3437` maxDD `-5.3574`
- `market_context_high->equity_4h` score `3.0047` n `195` status `ready` deltaP `16.0858` edge `0.2526` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.7393` n `139` status `ready` deltaP `15.4775` edge `0.5316` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.7746` n `197` status `ready` deltaP `7.1127` edge `0.1195` maxDD `-4.1892`
- `market_context_high->index_4h` score `0.4376` n `195` status `ready` deltaP `7.8392` edge `0.0931` maxDD `-3.7119`
- `market_context_high->crypto_alt_24h` score `0.3944` n `139` status `ready` deltaP `23.8468` edge `1.0548` maxDD `-88.8062`
- `market_context_high->crypto_major_1h` score `0.1306` n `197` status `ready` deltaP `4.9067` edge `0.0858` maxDD `-3.9439`
- `market_context_high->equity_1h` score `-0.0148` n `197` status `ready` deltaP `4.203` edge `0.0516` maxDD `-2.8014`
- `market_context_high->metal_4h` score `-0.4896` n `195` status `ready` deltaP `12.6469` edge `0.1221` maxDD `-12.5349`
- `market_context_high->index_1h` score `-0.5323` n `197` status `ready` deltaP `0.3177` edge `0.0167` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.634` n `197` status `ready` deltaP `5.3558` edge `0.0166` maxDD `-6.3532`
- `market_context_high->fx_1h` score `-0.6527` n `197` status `ready` deltaP `-2.7075` edge `-0.0024` maxDD `-0.3914`
- `market_context_high->crypto_major_24h` score `-0.8574` n `139` status `ready` deltaP `22.0433` edge `0.6017` maxDD `-62.3533`
- `market_context_high->fx_24h` score `-0.8669` n `139` status `ready` deltaP `4.3601` edge `0.0036` maxDD `-1.3925`
- `market_context_high->fx_4h` score `-1.8812` n `195` status `ready` deltaP `-7.6016` edge `-0.0132` maxDD `-1.4313`
- `market_context_high->commodity_1h` score `-2.1316` n `197` status `ready` deltaP `0.1299` edge `-0.0287` maxDD `-14.9691`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
