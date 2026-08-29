# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T05:52:27.390946+00:00`
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

- `news_risk_high->unknown_24h` score `58.0447` n `50` status `ready` deltaP `21.3542` edge `4.6947` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `33.3326` n `50` status `ready` deltaP `46.5208` edge `2.5117` maxDD `-2.8629`
- `news_risk_high->crypto_major_24h` score `9.742` n `50` status `ready` deltaP `27.9236` edge `0.675` maxDD `-2.6128`
- `news_risk_high->equity_24h` score `7.414` n `50` status `ready` deltaP `30.0069` edge `0.5106` maxDD `-4.7584`
- `market_context_high->unknown_24h` score `7.3534` n `120` status `ready` deltaP `14.6875` edge `0.5881` maxDD `-3.1917`
- `news_risk_high->unknown_4h` score `6.7835` n `78` status `ready` deltaP `11.8316` edge `0.5351` maxDD `-1.5617`
- `news_risk_high->metal_24h` score `4.5422` n `50` status `ready` deltaP `43.3125` edge `0.094` maxDD `-0.0053`
- `market_context_high->metal_24h` score `3.3594` n `120` status `ready` deltaP `28.6458` edge `0.1909` maxDD `-3.1535`
- `news_risk_high->unknown_1h` score `2.674` n `80` status `ready` deltaP `5.3743` edge `0.2227` maxDD `-0.8558`
- `news_risk_high->index_24h` score `2.4934` n `50` status `ready` deltaP `26.8889` edge `0.0436` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.4788` n `120` status `ready` deltaP `19.0752` edge `0.1201` maxDD `-0.5894`
- `news_risk_high->fx_4h` score `2.2841` n `78` status `ready` deltaP `33.478` edge `0.0221` maxDD `-0.3953`
- `market_context_high->unknown_1h` score `1.2479` n `120` status `ready` deltaP `9.541` edge `0.0854` maxDD `-1.6015`
- `news_risk_high->fx_1h` score `0.6393` n `80` status `ready` deltaP `12.994` edge `0.0055` maxDD `-0.108`
- `news_risk_high->commodity_1h` score `0.4906` n `80` status `ready` deltaP `13.3982` edge `0.0056` maxDD `-0.5618`
- `market_context_high->metal_4h` score `-0.147` n `120` status `ready` deltaP `9.4918` edge `0.0096` maxDD `-3.3377`
- `market_context_high->fx_1h` score `-0.332` n `120` status `ready` deltaP `4.6607` edge `-0.0004` maxDD `-0.8587`
- `news_risk_high->index_1h` score `-0.4144` n `80` status `ready` deltaP `-0.1422` edge `-0.0085` maxDD `-0.8275`
- `news_risk_high->commodity_4h` score `-0.5577` n `78` status `ready` deltaP `7.6845` edge `0.0114` maxDD `-2.0635`
- `news_risk_high->index_4h` score `-0.5624` n `78` status `ready` deltaP `1.3446` edge `-0.0169` maxDD `-1.7996`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
