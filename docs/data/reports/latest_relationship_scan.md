# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-02T10:37:30.734416+00:00`
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

- `news_risk_high->unknown_24h` score `5185.0731` n `60` status `ready` deltaP `29.7916` edge `431.9329` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `17.7212` n `42` status `ready` deltaP `59.3998` edge `1.1205` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `9.2734` n `42` status `ready` deltaP `46.6765` edge `0.4996` maxDD `-2.0393`
- `news_risk_high->equity_4h` score `4.5517` n `68` status `ready` deltaP `16.5261` edge `0.3455` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.6182` n `68` status `ready` deltaP `15.9164` edge `0.0668` maxDD `-0.3783`
- `market_context_high->commodity_4h` score `1.1167` n `42` status `ready` deltaP `15.164` edge `0.1267` maxDD `-2.7703`
- `news_risk_high->equity_1h` score `0.6528` n `68` status `ready` deltaP `9.9419` edge `0.0704` maxDD `-2.916`
- `market_context_high->fx_4h` score `0.582` n `42` status `ready` deltaP `19.338` edge `0.0253` maxDD `-1.3685`
- `market_context_high->commodity_1h` score `0.4311` n `42` status `ready` deltaP `8.4902` edge `0.0361` maxDD `-1.3282`
- `market_context_high->crypto_alt_4h` score `0.3416` n `42` status `ready` deltaP `4.9725` edge `0.1029` maxDD `-5.047`
- `market_context_high->fx_1h` score `0.2478` n `42` status `ready` deltaP `11.3202` edge `0.0024` maxDD `-0.6874`
- `news_risk_high->fx_4h` score `0.2454` n `68` status `ready` deltaP `13.6657` edge `0.0251` maxDD `-0.6604`
- `news_risk_high->metal_4h` score `0.1379` n `68` status `ready` deltaP `5.6223` edge `0.0278` maxDD `-0.8085`
- `news_risk_high->crypto_alt_1h` score `0.0858` n `68` status `ready` deltaP `6.3315` edge `0.037` maxDD `-3.1233`
- `news_risk_high->fx_1h` score `-0.0435` n `68` status `ready` deltaP `3.267` edge `0.0049` maxDD `-0.2475`
- `news_risk_high->index_1h` score `-0.0528` n `68` status `ready` deltaP `2.7651` edge `0.0071` maxDD `-0.5845`
- `news_risk_high->metal_1h` score `-0.1077` n `68` status `ready` deltaP `3.0645` edge `0.0061` maxDD `-0.5599`
- `news_risk_high->crypto_major_1h` score `-0.1844` n `68` status `ready` deltaP `2.8179` edge `0.0296` maxDD `-3.762`
- `market_context_high->crypto_alt_1h` score `-0.2875` n `42` status `ready` deltaP `2.8301` edge `0.007` maxDD `-3.0178`
- `news_risk_high->commodity_1h` score `-0.6763` n `68` status `ready` deltaP `2.8179` edge `-0.0275` maxDD `-2.9058`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
