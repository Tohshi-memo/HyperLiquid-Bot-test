# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-02T10:07:29.786556+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5900`

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

- `news_risk_high->unknown_24h` score `5185.1141` n `60` status `ready` deltaP `30.1389` edge `431.934` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `17.714` n `42` status `ready` deltaP `59.3998` edge `1.1199` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `9.265` n `42` status `ready` deltaP `46.6765` edge `0.4989` maxDD `-2.0393`
- `news_risk_high->equity_4h` score `4.5469` n `68` status `ready` deltaP `16.5261` edge `0.3451` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.5914` n `68` status `ready` deltaP `15.6115` edge `0.0666` maxDD `-0.3783`
- `market_context_high->commodity_4h` score `1.127` n `42` status `ready` deltaP `15.3165` edge `0.127` maxDD `-2.7703`
- `news_risk_high->equity_1h` score `0.6504` n `68` status `ready` deltaP `9.9419` edge `0.0702` maxDD `-2.916`
- `market_context_high->fx_4h` score `0.5654` n `42` status `ready` deltaP `19.0331` edge `0.0252` maxDD `-1.3685`
- `market_context_high->commodity_1h` score `0.4451` n `42` status `ready` deltaP `8.6399` edge `0.0369` maxDD `-1.3282`
- `market_context_high->crypto_alt_4h` score `0.3393` n `42` status `ready` deltaP `4.9725` edge `0.1026` maxDD `-5.047`
- `market_context_high->fx_1h` score `0.2401` n `42` status `ready` deltaP `11.1705` edge `0.0024` maxDD `-0.6874`
- `news_risk_high->fx_4h` score `0.2198` n `68` status `ready` deltaP `13.3608` edge `0.025` maxDD `-0.6604`
- `news_risk_high->metal_4h` score `0.1355` n `68` status `ready` deltaP `5.6223` edge `0.0275` maxDD `-0.8085`
- `news_risk_high->crypto_alt_1h` score `0.0656` n `68` status `ready` deltaP `6.0321` edge `0.0364` maxDD `-3.1233`
- `news_risk_high->fx_1h` score `-0.0513` n `68` status `ready` deltaP `3.1173` edge `0.0049` maxDD `-0.2475`
- `news_risk_high->index_1h` score `-0.0614` n `68` status `ready` deltaP `2.6154` edge `0.007` maxDD `-0.5845`
- `news_risk_high->metal_1h` score `-0.1092` n `68` status `ready` deltaP `3.0645` edge `0.0059` maxDD `-0.5599`
- `news_risk_high->crypto_major_1h` score `-0.2054` n `68` status `ready` deltaP `2.5185` edge `0.0289` maxDD `-3.762`
- `market_context_high->crypto_alt_1h` score `-0.3077` n `42` status `ready` deltaP `2.5307` edge `0.0064` maxDD `-3.0178`
- `news_risk_high->commodity_1h` score `-0.6623` n `68` status `ready` deltaP `2.9676` edge `-0.0267` maxDD `-2.9058`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
