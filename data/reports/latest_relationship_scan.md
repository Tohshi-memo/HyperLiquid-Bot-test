# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T11:37:27.029034+00:00`
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

- `market_context_high->crypto_alt_24h` score `12.0387` n `40` status `ready` deltaP `51.4583` edge `0.6999` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `10.8527` n `40` status `ready` deltaP `51.1458` edge `0.5762` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `1.6552` n `31` status `ready` deltaP `-6.668` edge `0.2508` maxDD `-2.8064`
- `news_risk_high->commodity_1h` score `0.9692` n `31` status `ready` deltaP `20.2868` edge `0.0102` maxDD `-0.6947`
- `news_risk_high->fx_24h` score `0.9293` n `31` status `ready` deltaP `12.192` edge `0.0614` maxDD `-1.5526`
- `market_context_high->commodity_1h` score `0.3673` n `47` status `ready` deltaP `7.864` edge `0.0321` maxDD `-1.3282`
- `news_risk_high->commodity_4h` score `0.3433` n `31` status `ready` deltaP `13.8572` edge `-0.0137` maxDD `-1.6728`
- `market_context_high->commodity_4h` score `0.3003` n `47` status `ready` deltaP `4.7289` edge `0.0916` maxDD `-2.7703`
- `news_risk_high->index_4h` score `0.2837` n `31` status `ready` deltaP `0.2409` edge `0.0601` maxDD `-0.3783`
- `news_risk_high->fx_4h` score `0.1438` n `31` status `ready` deltaP `4.8928` edge `0.0361` maxDD `-0.356`
- `news_risk_high->crypto_alt_1h` score `0.1163` n `31` status `ready` deltaP `12.1885` edge `-0.0023` maxDD `-3.1233`
- `news_risk_high->index_1h` score `0.0379` n `31` status `ready` deltaP `3.9405` edge `-0.0016` maxDD `-0.5845`
- `market_context_high->fx_1h` score `-0.0248` n `47` status `ready` deltaP `6.6664` edge `-0.0087` maxDD `-0.7804`
- `market_context_high->fx_4h` score `-0.1425` n `47` status `ready` deltaP `11.8935` edge `-0.0055` maxDD `-1.8531`
- `news_risk_high->fx_1h` score `-0.2357` n `31` status `ready` deltaP `-0.2656` edge `0.0027` maxDD `-0.1588`
- `market_context_high->crypto_alt_4h` score `-0.3558` n `47` status `ready` deltaP `1.6865` edge `0.0337` maxDD `-4.9116`
- `news_risk_high->metal_1h` score `-0.584` n `31` status `ready` deltaP `-2.2117` edge `-0.002` maxDD `-0.5538`
- `market_context_high->fx_24h` score `-0.6827` n `40` status `ready` deltaP `0.6597` edge `0.0367` maxDD `-2.506`
- `news_risk_high->crypto_major_1h` score `-0.7496` n `31` status `ready` deltaP `3.559` edge `-0.0478` maxDD `-3.762`
- `news_risk_high->equity_1h` score `-0.9393` n `31` status `ready` deltaP `-9.7112` edge `0.0266` maxDD `-2.916`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
