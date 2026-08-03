# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T18:37:28.009369+00:00`
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

- `market_context_high->unknown_24h` score `45.7653` n `39` status `ready` deltaP `29.8611` edge `3.6147` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `11.4472` n `39` status `ready` deltaP `50.2938` edge `0.636` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `11.2229` n `39` status `ready` deltaP `53.6458` edge `0.5776` maxDD `0.0`
- `news_risk_high->fx_24h` score `0.9665` n `31` status `ready` deltaP `12.192` edge `0.0645` maxDD `-1.5526`
- `news_risk_high->commodity_1h` score `0.9007` n `31` status `ready` deltaP `19.2389` edge `0.0084` maxDD `-0.6947`
- `news_risk_high->equity_4h` score `0.7532` n `31` status `ready` deltaP `-7.2777` edge `0.1797` maxDD `-2.8064`
- `market_context_high->commodity_1h` score `0.4016` n `59` status `ready` deltaP `9.1241` edge `0.0281` maxDD `-1.3282`
- `market_context_high->commodity_4h` score `0.2992` n `47` status `ready` deltaP `4.7223` edge `0.0915` maxDD `-2.7703`
- `news_risk_high->index_4h` score `0.121` n `31` status `ready` deltaP `-0.3688` edge `0.0506` maxDD `-0.3783`
- `news_risk_high->fx_4h` score `0.113` n `31` status `ready` deltaP `4.4355` edge `0.0352` maxDD `-0.356`
- `news_risk_high->commodity_4h` score `0.0753` n `31` status `ready` deltaP `11.723` edge `-0.0218` maxDD `-1.6728`
- `market_context_high->fx_1h` score `0.0478` n `59` status `ready` deltaP `6.6807` edge `-0.0058` maxDD `-0.7804`
- `market_context_high->fx_4h` score `-0.0077` n `47` status `ready` deltaP `13.5638` edge `-0.0054` maxDD `-1.8531`
- `news_risk_high->index_1h` score `-0.0828` n `31` status `ready` deltaP `2.2938` edge `-0.0061` maxDD `-0.5845`
- `news_risk_high->crypto_alt_1h` score `-0.1595` n `31` status `ready` deltaP `9.4939` edge `-0.0197` maxDD `-3.1233`
- `market_context_high->crypto_alt_1h` score `-0.2076` n `59` status `ready` deltaP `4.1358` edge `0.0127` maxDD `-3.0178`
- `news_risk_high->fx_1h` score `-0.2692` n `31` status `ready` deltaP `-0.8644` edge `0.0024` maxDD `-0.1588`
- `market_context_high->index_1h` score `-0.4713` n `59` status `ready` deltaP `1.6924` edge `-0.0183` maxDD `-1.6054`
- `market_context_high->fx_24h` score `-0.5703` n `39` status `ready` deltaP `1.1084` edge `0.0415` maxDD `-2.3798`
- `news_risk_high->metal_1h` score `-0.6151` n `31` status `ready` deltaP `-2.6608` edge `-0.0016` maxDD `-0.5538`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
