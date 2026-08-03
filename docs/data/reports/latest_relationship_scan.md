# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T12:52:26.655355+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5897`

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

- `market_context_high->crypto_alt_24h` score `11.7435` n `40` status `ready` deltaP `51.4583` edge `0.6753` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `10.8347` n `40` status `ready` deltaP `51.1458` edge `0.5747` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `1.5184` n `31` status `ready` deltaP `-6.668` edge `0.2394` maxDD `-2.8064`
- `news_risk_high->commodity_1h` score `1.0004` n `31` status `ready` deltaP `20.7359` edge `0.0112` maxDD `-0.6947`
- `news_risk_high->fx_24h` score `0.9329` n `31` status `ready` deltaP `12.192` edge `0.0617` maxDD `-1.5526`
- `market_context_high->commodity_1h` score `0.3985` n `47` status `ready` deltaP `8.3131` edge `0.0331` maxDD `-1.3282`
- `news_risk_high->commodity_4h` score `0.3784` n `31` status `ready` deltaP `14.1621` edge `-0.0128` maxDD `-1.6728`
- `market_context_high->commodity_4h` score `0.3232` n `47` status `ready` deltaP `5.0338` edge `0.0925` maxDD `-2.7703`
- `news_risk_high->index_4h` score `0.2489` n `31` status `ready` deltaP `0.2409` edge `0.0572` maxDD `-0.3783`
- `news_risk_high->fx_4h` score `0.1415` n `31` status `ready` deltaP `4.8928` edge `0.0358` maxDD `-0.356`
- `news_risk_high->crypto_alt_1h` score `0.086` n `31` status `ready` deltaP `11.7394` edge `-0.0032` maxDD `-3.1233`
- `news_risk_high->index_1h` score `0.0488` n `31` status `ready` deltaP `4.0902` edge `-0.0012` maxDD `-0.5845`
- `market_context_high->fx_1h` score `-0.017` n `47` status `ready` deltaP `6.8161` edge `-0.0087` maxDD `-0.7804`
- `market_context_high->fx_4h` score `-0.1461` n `47` status `ready` deltaP `11.8935` edge `-0.0058` maxDD `-1.8531`
- `news_risk_high->fx_1h` score `-0.2279` n `31` status `ready` deltaP `-0.1159` edge `0.0027` maxDD `-0.1588`
- `market_context_high->crypto_alt_4h` score `-0.5101` n `47` status `ready` deltaP `0.9244` edge `0.019` maxDD `-4.9116`
- `news_risk_high->metal_1h` score `-0.5792` n `31` status `ready` deltaP `-2.2117` edge `-0.0016` maxDD `-0.5538`
- `market_context_high->fx_24h` score `-0.6791` n `40` status `ready` deltaP `0.6597` edge `0.037` maxDD `-2.506`
- `news_risk_high->crypto_major_1h` score `-0.7425` n `31` status `ready` deltaP `3.559` edge `-0.0469` maxDD `-3.762`
- `news_risk_high->equity_1h` score `-0.9214` n `31` status `ready` deltaP `-9.5615` edge `0.0279` maxDD `-2.916`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
