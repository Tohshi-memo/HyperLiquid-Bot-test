# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T21:52:35.356183+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5932`

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

- `market_context_high->unknown_24h` score `41.6374` n `42` status `ready` deltaP `26.6121` edge `3.2967` maxDD `-0.0128`
- `market_context_high->unknown_4h` score `14.0662` n `60` status `ready` deltaP `9.1667` edge `1.1583` maxDD `-1.4448`
- `market_context_high->crypto_alt_24h` score `10.6974` n `42` status `ready` deltaP `48.5863` edge `0.5849` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `9.8952` n `42` status `ready` deltaP `48.5367` edge `0.5131` maxDD `-0.2995`
- `news_risk_high->fx_24h` score `1.0121` n `31` status `ready` deltaP `12.192` edge `0.0683` maxDD `-1.5526`
- `market_context_high->commodity_4h` score `0.9812` n `60` status `ready` deltaP `12.1341` edge `0.0855` maxDD `-2.7703`
- `news_risk_high->commodity_1h` score `0.8789` n `31` status `ready` deltaP `18.9395` edge `0.0076` maxDD `-0.6947`
- `market_context_high->commodity_1h` score `0.4461` n `72` status `ready` deltaP `8.142` edge `0.0245` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.394` n `72` status `ready` deltaP `10.5123` edge `-0.0024` maxDD `-0.7878`
- `news_risk_high->equity_4h` score `0.2711` n `31` status `ready` deltaP `-8.9546` edge `0.1507` maxDD `-2.8064`
- `market_context_high->fx_4h` score `0.2333` n `60` status `ready` deltaP `15.6809` edge `0.0009` maxDD `-1.8797`
- `news_risk_high->fx_4h` score `0.1082` n `31` status `ready` deltaP `4.2831` edge `0.0356` maxDD `-0.356`
- `news_risk_high->index_4h` score `-0.0756` n `31` status `ready` deltaP `-2.0456` edge `0.0454` maxDD `-0.3783`
- `news_risk_high->commodity_4h` score `-0.0766` n `31` status `ready` deltaP `10.1986` edge `-0.0243` maxDD `-1.6728`
- `market_context_high->crypto_alt_4h` score `-0.0771` n `60` status `ready` deltaP `8.4857` edge `0.0241` maxDD `-4.9116`
- `news_risk_high->index_1h` score `-0.0906` n `31` status `ready` deltaP `2.1441` edge `-0.0061` maxDD `-0.5845`
- `news_risk_high->crypto_alt_1h` score `-0.1494` n `31` status `ready` deltaP `9.7933` edge `-0.0204` maxDD `-3.1233`
- `market_context_high->crypto_alt_1h` score `-0.269` n `72` status `ready` deltaP `2.6697` edge `0.0146` maxDD `-3.0178`
- `news_risk_high->fx_1h` score `-0.3416` n `31` status `ready` deltaP `-2.2117` edge `0.0021` maxDD `-0.1588`
- `market_context_high->index_1h` score `-0.4414` n `72` status `ready` deltaP `1.4721` edge `-0.013` maxDD `-1.6054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
