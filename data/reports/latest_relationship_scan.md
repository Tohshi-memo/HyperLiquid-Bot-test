# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T19:37:36.621662+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5930`

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

- `market_context_high->unknown_24h` score `45.6689` n `39` status `ready` deltaP `29.1667` edge `3.6113` maxDD `0.0`
- `market_context_high->unknown_4h` score `18.086` n `51` status `ready` deltaP `15.1692` edge `1.4366` maxDD `-0.7783`
- `market_context_high->crypto_alt_24h` score `11.1972` n `39` status `ready` deltaP `49.5994` edge `0.6198` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `11.1286` n `39` status `ready` deltaP `53.4722` edge `0.5709` maxDD `0.0`
- `news_risk_high->fx_24h` score `0.9773` n `31` status `ready` deltaP `12.192` edge `0.0654` maxDD `-1.5526`
- `news_risk_high->commodity_1h` score `0.8696` n `31` status `ready` deltaP `18.7898` edge `0.0074` maxDD `-0.6947`
- `news_risk_high->equity_4h` score `0.6664` n `31` status `ready` deltaP `-7.5826` edge `0.1745` maxDD `-2.8064`
- `market_context_high->commodity_4h` score `0.4811` n `51` status `ready` deltaP `7.9508` edge `0.0933` maxDD `-2.7703`
- `market_context_high->commodity_1h` score `0.452` n `63` status `ready` deltaP `9.7781` edge `0.0302` maxDD `-1.3282`
- `news_risk_high->fx_4h` score `0.0964` n `31` status `ready` deltaP `4.1306` edge `0.0351` maxDD `-0.356`
- `news_risk_high->index_4h` score `0.0882` n `31` status `ready` deltaP `-0.6737` edge `0.0499` maxDD `-0.3783`
- `news_risk_high->commodity_4h` score `0.0097` n `31` status `ready` deltaP `11.1133` edge `-0.0232` maxDD `-1.6728`
- `market_context_high->fx_1h` score `-0.0014` n `63` status `ready` deltaP `6.0047` edge `-0.0053` maxDD `-0.7878`
- `market_context_high->fx_4h` score `-0.0197` n `51` status `ready` deltaP `13.1755` edge `-0.0038` maxDD `-1.8545`
- `news_risk_high->index_1h` score `-0.0641` n `31` status `ready` deltaP `2.5932` edge `-0.0057` maxDD `-0.5845`
- `news_risk_high->crypto_alt_1h` score `-0.1354` n `31` status `ready` deltaP `9.7933` edge `-0.0186` maxDD `-3.1233`
- `market_context_high->crypto_alt_1h` score `-0.1835` n `63` status `ready` deltaP `4.0586` edge `0.0163` maxDD `-3.0178`
- `news_risk_high->fx_1h` score `-0.2848` n `31` status `ready` deltaP `-1.1638` edge `0.0024` maxDD `-0.1588`
- `market_context_high->crypto_alt_4h` score `-0.4334` n `51` status `ready` deltaP `2.5048` edge `0.0183` maxDD `-4.9116`
- `market_context_high->index_1h` score `-0.5429` n `63` status `ready` deltaP `0.1355` edge `-0.0171` maxDD `-1.6054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
