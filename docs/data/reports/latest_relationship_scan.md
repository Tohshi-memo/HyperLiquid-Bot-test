# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T20:41:13.662724+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5931`

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

- `market_context_high->unknown_24h` score `44.3056` n `40` status `ready` deltaP `28.8194` edge `3.5` maxDD `0.0`
- `market_context_high->unknown_4h` score `15.9346` n `55` status `ready` deltaP `13.2538` edge `1.284` maxDD `-1.2244`
- `market_context_high->crypto_alt_24h` score `11.0226` n `40` status `ready` deltaP `49.0972` edge `0.6086` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `10.5744` n `40` status `ready` deltaP `50.9722` edge `0.5474` maxDD `-0.1479`
- `news_risk_high->fx_24h` score `0.9917` n `31` status `ready` deltaP `12.192` edge `0.0666` maxDD `-1.5526`
- `news_risk_high->commodity_1h` score `0.8875` n `31` status `ready` deltaP `19.0892` edge `0.0077` maxDD `-0.6947`
- `market_context_high->commodity_4h` score `0.7835` n `55` status `ready` deltaP `9.1075` edge `0.0892` maxDD `-2.7703`
- `news_risk_high->equity_4h` score `0.5156` n `31` status `ready` deltaP `-8.1924` edge `0.166` maxDD `-2.8064`
- `market_context_high->commodity_1h` score `0.3789` n `67` status `ready` deltaP `6.5712` edge `0.0252` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.181` n `67` status `ready` deltaP `8.0593` edge `-0.0038` maxDD `-0.7878`
- `news_risk_high->fx_4h` score `0.1059` n `31` status `ready` deltaP `4.2831` edge `0.0353` maxDD `-0.356`
- `news_risk_high->index_4h` score `0.0202` n `31` status `ready` deltaP `-1.2834` edge `0.0483` maxDD `-0.3783`
- `news_risk_high->commodity_4h` score `-0.0182` n `31` status `ready` deltaP `10.8084` edge `-0.0235` maxDD `-1.6728`
- `news_risk_high->index_1h` score `-0.0812` n `31` status `ready` deltaP `2.2938` edge `-0.0059` maxDD `-0.5845`
- `news_risk_high->crypto_alt_1h` score `-0.0941` n `31` status `ready` deltaP `10.3921` edge `-0.0173` maxDD `-3.1233`
- `market_context_high->fx_4h` score `-0.1457` n `55` status `ready` deltaP `11.4385` edge `-0.0024` maxDD `-1.8797`
- `market_context_high->crypto_alt_4h` score `-0.2204` n `55` status `ready` deltaP `5.4601` edge `0.0259` maxDD `-4.9116`
- `news_risk_high->fx_1h` score `-0.3175` n `31` status `ready` deltaP `-1.7626` edge `0.0022` maxDD `-0.1588`
- `market_context_high->crypto_alt_1h` score `-0.3483` n `67` status `ready` deltaP `1.3406` edge `0.0133` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.3888` n `67` status `ready` deltaP `2.679` edge `-0.0143` maxDD `-1.6054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
