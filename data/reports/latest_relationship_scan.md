# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T04:52:28.229591+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11666`

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

- `news_risk_high->unknown_24h` score `57.843` n `50` status `ready` deltaP `20.7972` edge `4.6816` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `33.9479` n `50` status `ready` deltaP `46.6066` edge `2.5624` maxDD `-2.8629`
- `news_risk_high->crypto_major_24h` score `10.0065` n `50` status `ready` deltaP `28.0208` edge `0.6964` maxDD `-2.6128`
- `news_risk_high->equity_24h` score `7.3495` n `50` status `ready` deltaP `30.1005` edge `0.5046` maxDD `-4.7584`
- `market_context_high->unknown_24h` score `7.1517` n `120` status `ready` deltaP `14.1305` edge `0.575` maxDD `-3.1917`
- `news_risk_high->unknown_4h` score `7.0981` n `77` status `ready` deltaP `12.6782` edge `0.5505` maxDD `-1.4812`
- `news_risk_high->metal_24h` score `4.539` n `50` status `ready` deltaP `43.4073` edge `0.0931` maxDD `-0.0053`
- `market_context_high->metal_24h` score `3.3562` n `120` status `ready` deltaP `28.7406` edge `0.19` maxDD `-3.1535`
- `news_risk_high->index_24h` score `2.497` n `50` status `ready` deltaP `26.9948` edge `0.0432` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.4558` n `120` status `ready` deltaP `18.9228` edge `0.1192` maxDD `-0.5894`
- `news_risk_high->unknown_1h` score `2.4004` n `80` status `ready` deltaP `5.2246` edge `0.2009` maxDD `-0.8558`
- `news_risk_high->fx_4h` score `2.3113` n `77` status `ready` deltaP `33.788` edge `0.0223` maxDD `-0.3953`
- `market_context_high->unknown_1h` score `0.9743` n `120` status `ready` deltaP `9.3913` edge `0.0636` maxDD `-1.6015`
- `news_risk_high->fx_1h` score `0.6393` n `80` status `ready` deltaP `12.994` edge `0.0055` maxDD `-0.108`
- `news_risk_high->commodity_1h` score `0.4556` n `80` status `ready` deltaP `12.7994` edge `0.0051` maxDD `-0.5618`
- `market_context_high->metal_4h` score `-0.1098` n `120` status `ready` deltaP `10.1016` edge `0.0103` maxDD `-3.3377`
- `market_context_high->fx_1h` score `-0.332` n `120` status `ready` deltaP `4.6607` edge `-0.0004` maxDD `-0.8587`
- `news_risk_high->index_1h` score `-0.3809` n `80` status `ready` deltaP `0.4566` edge `-0.0082` maxDD `-0.8275`
- `news_risk_high->commodity_4h` score `-0.5547` n `77` status `ready` deltaP `7.7408` edge `0.0114` maxDD `-2.0635`
- `news_risk_high->equity_1h` score `-0.5594` n `80` status `ready` deltaP `8.7575` edge `-0.0367` maxDD `-5.1385`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
