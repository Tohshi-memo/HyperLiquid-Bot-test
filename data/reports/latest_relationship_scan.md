# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T17:37:31.304267+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11744`

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

- `news_risk_high->unknown_24h` score `4427.6724` n `85` status `ready` deltaP `1.2153` edge `368.9646` maxDD `0.0`
- `market_context_high->unknown_1h` score `68.989` n `47` status `ready` deltaP `8.3196` edge `5.7007` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `46.3714` n `47` status `ready` deltaP `20.8739` edge `3.7644` maxDD `-2.4756`
- `market_context_high->equity_24h` score `25.4883` n `47` status `ready` deltaP `32.1587` edge `1.9452` maxDD `-2.1786`
- `market_context_high->crypto_alt_24h` score `25.4282` n `47` status `ready` deltaP `15.0598` edge `2.0566` maxDD `-2.7051`
- `market_context_high->index_24h` score `6.7627` n `47` status `ready` deltaP `25.9087` edge `0.4038` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.2485` n `47` status `ready` deltaP `27.2459` edge `0.1129` maxDD `-0.2401`
- `market_context_high->index_4h` score `2.7577` n `47` status `ready` deltaP `31.8922` edge `0.0326` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.7363` n `47` status `ready` deltaP `17.4494` edge `0.1535` maxDD `-1.3444`
- `news_risk_high->index_24h` score `2.0574` n `85` status `ready` deltaP `24.0564` edge `0.0681` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `1.4154` n `85` status `ready` deltaP `30.4249` edge `0.1434` maxDD `-6.8481`
- `news_risk_high->crypto_alt_24h` score `1.1892` n `85` status `ready` deltaP `8.9522` edge `0.4346` maxDD `-29.2814`
- `market_context_high->equity_1h` score `1.0218` n `47` status `ready` deltaP `11.7658` edge `0.047` maxDD `-1.5564`
- `market_context_high->crypto_alt_4h` score `0.9168` n `47` status `ready` deltaP `9.5355` edge `0.0796` maxDD `-3.3417`
- `market_context_high->index_1h` score `0.8074` n `47` status `ready` deltaP `12.8137` edge `0.0097` maxDD `-0.2275`
- `market_context_high->crypto_major_4h` score `0.5144` n `47` status `ready` deltaP `5.1472` edge `0.099` maxDD `-5.2359`
- `market_context_high->fx_1h` score `0.4578` n `47` status `ready` deltaP `9.9598` edge `0.0074` maxDD `-0.1854`
- `market_context_high->crypto_major_1h` score `0.4189` n `47` status `ready` deltaP `5.9498` edge `0.077` maxDD `-4.5405`
- `market_context_high->metal_1h` score `0.0289` n `47` status `ready` deltaP `3.7266` edge `0.0105` maxDD `-0.1976`
- `news_risk_high->index_1h` score `-0.0711` n `139` status `ready` deltaP `2.9714` edge `0.0034` maxDD `-0.3305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
