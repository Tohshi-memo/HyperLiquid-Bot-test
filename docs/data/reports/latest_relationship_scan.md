# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T04:07:30.114350+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9932`

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

- `market_context_high->unknown_24h` score `37.3899` n `46` status `ready` deltaP `26.2983` edge `2.9448` maxDD `-0.0103`
- `market_context_high->crypto_alt_24h` score `9.7934` n `46` status `ready` deltaP `46.2561` edge `0.5251` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `8.305` n `46` status `ready` deltaP `38.9568` edge `0.4503` maxDD `-0.434`
- `market_context_high->unknown_4h` score `4.2584` n `85` status `ready` deltaP `2.3583` edge `0.6217` maxDD `-3.3176`
- `market_context_high->commodity_4h` score `1.2491` n `85` status `ready` deltaP `15.2726` edge `0.0869` maxDD `-2.7703`
- `market_context_high->fx_4h` score `0.5487` n `85` status `ready` deltaP `18.3178` edge `0.0096` maxDD `-1.8797`
- `market_context_high->commodity_1h` score `0.2888` n `88` status `ready` deltaP `6.1309` edge `0.0248` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.273` n `88` status `ready` deltaP `9.0297` edge `-0.0026` maxDD `-0.7878`
- `market_context_high->index_1h` score `-0.411` n `88` status `ready` deltaP `2.4769` edge `-0.0158` maxDD `-1.6054`
- `market_context_high->metal_1h` score `-0.5089` n `88` status `ready` deltaP `-1.1704` edge `-0.008` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.5536` n `85` status `ready` deltaP `4.8601` edge `0.0201` maxDD `-3.211`
- `market_context_high->crypto_alt_1h` score `-1.2875` n `88` status `ready` deltaP `-3.62` edge `-0.0121` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.4396` n `88` status `ready` deltaP `6.6617` edge `-0.0754` maxDD `-10.619`
- `market_context_high->fx_24h` score `-1.5136` n `46` status `ready` deltaP `-2.6645` edge `0.0122` maxDD `-4.3126`
- `market_context_high->crypto_alt_4h` score `-1.7433` n `85` status `ready` deltaP `2.222` edge `-0.0211` maxDD `-5.7857`
- `market_context_high->index_4h` score `-1.8053` n `85` status `ready` deltaP `-9.3005` edge `-0.044` maxDD `-4.7021`
- `market_context_high->unknown_1h` score `-3.0585` n `88` status `ready` deltaP `3.1982` edge `-0.2315` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.6079` n `88` status `ready` deltaP `-12.7994` edge `-0.078` maxDD `-7.6533`
- `market_context_high->metal_24h` score `-4.7878` n `46` status `ready` deltaP `-23.4677` edge `-0.1257` maxDD `-2.6802`
- `market_context_high->equity_4h` score `-6.5851` n `85` status `ready` deltaP `0.8304` edge `-0.3167` maxDD `-35.3129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
