# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T20:07:32.673871+00:00`
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

- `market_context_high->unknown_24h` score `45.6196` n `39` status `ready` deltaP `28.8194` edge `3.6095` maxDD `0.0`
- `market_context_high->unknown_4h` score `16.6529` n `53` status `ready` deltaP `12.3619` edge `1.3498` maxDD `-1.2244`
- `market_context_high->commodity_24h` score `11.0926` n `39` status `ready` deltaP `53.4722` edge `0.5679` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `11.0782` n `39` status `ready` deltaP `49.2521` edge `0.6122` maxDD `-0.3889`
- `news_risk_high->fx_24h` score `0.9845` n `31` status `ready` deltaP `12.192` edge `0.066` maxDD `-1.5526`
- `news_risk_high->commodity_1h` score `0.8696` n `31` status `ready` deltaP `18.7898` edge `0.0074` maxDD `-0.6947`
- `news_risk_high->equity_4h` score `0.5964` n `31` status `ready` deltaP `-7.8875` edge `0.1707` maxDD `-2.8064`
- `market_context_high->commodity_4h` score `0.5492` n `53` status `ready` deltaP `9.5001` edge `0.0917` maxDD `-2.7703`
- `market_context_high->commodity_1h` score `0.3393` n `65` status `ready` deltaP `7.971` edge `0.0278` maxDD `-1.3282`
- `news_risk_high->fx_4h` score `0.0964` n `31` status `ready` deltaP `4.1306` edge `0.0351` maxDD `-0.356`
- `market_context_high->fx_1h` score `0.0925` n `65` status `ready` deltaP `7.0728` edge `-0.0046` maxDD `-0.7878`
- `news_risk_high->index_4h` score `0.0566` n `31` status `ready` deltaP `-0.9786` edge `0.0493` maxDD `-0.3783`
- `news_risk_high->commodity_4h` score `-0.0037` n `31` status `ready` deltaP `10.9608` edge `-0.0233` maxDD `-1.6728`
- `news_risk_high->index_1h` score `-0.0649` n `31` status `ready` deltaP `2.5932` edge `-0.0058` maxDD `-0.5845`
- `news_risk_high->crypto_alt_1h` score `-0.1128` n `31` status `ready` deltaP `10.0927` edge `-0.0177` maxDD `-3.1233`
- `market_context_high->fx_4h` score `-0.1748` n `53` status `ready` deltaP `11.2517` edge `-0.0036` maxDD `-1.8781`
- `market_context_high->crypto_alt_1h` score `-0.2834` n `65` status `ready` deltaP `2.6486` edge `0.0129` maxDD `-3.0178`
- `news_risk_high->fx_1h` score `-0.3011` n `31` status `ready` deltaP `-1.4632` edge `0.0023` maxDD `-0.1588`
- `market_context_high->crypto_alt_4h` score `-0.3336` n `53` status `ready` deltaP `4.0497` edge `0.0208` maxDD `-4.9116`
- `market_context_high->index_1h` score `-0.4581` n `65` status `ready` deltaP `1.6007` edge `-0.016` maxDD `-1.6054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
