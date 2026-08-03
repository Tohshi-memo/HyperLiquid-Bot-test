# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T19:07:25.661663+00:00`
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

- `market_context_high->unknown_24h` score `45.7171` n `39` status `ready` deltaP `29.5139` edge `3.613` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `11.327` n `39` status `ready` deltaP `49.9466` edge `0.6283` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `11.1821` n `39` status `ready` deltaP `53.6458` edge `0.5742` maxDD `0.0`
- `news_risk_high->fx_24h` score `0.9713` n `31` status `ready` deltaP `12.192` edge `0.0649` maxDD `-1.5526`
- `news_risk_high->commodity_1h` score `0.8805` n `31` status `ready` deltaP `18.9395` edge `0.0078` maxDD `-0.6947`
- `news_risk_high->equity_4h` score `0.7472` n `31` status `ready` deltaP `-7.2777` edge `0.1792` maxDD `-2.8064`
- `market_context_high->commodity_1h` score `0.4739` n `61` status `ready` deltaP `10.214` edge `0.0301` maxDD `-1.3282`
- `market_context_high->commodity_4h` score `0.3958` n `49` status `ready` deltaP `6.4149` edge `0.0926` maxDD `-2.7703`
- `news_risk_high->index_4h` score `0.1198` n `31` status `ready` deltaP `-0.3688` edge `0.0505` maxDD `-0.3783`
- `news_risk_high->fx_4h` score `0.1051` n `31` status `ready` deltaP `4.2831` edge `0.0352` maxDD `-0.356`
- `news_risk_high->commodity_4h` score `0.0401` n `31` status `ready` deltaP `11.4182` edge `-0.0227` maxDD `-1.6728`
- `market_context_high->fx_4h` score `-0.0125` n `49` status `ready` deltaP `13.368` edge `-0.0045` maxDD `-1.8531`
- `news_risk_high->index_1h` score `-0.0641` n `31` status `ready` deltaP `2.5932` edge `-0.0057` maxDD `-0.5845`
- `market_context_high->crypto_alt_1h` score `-0.095` n `61` status `ready` deltaP `5.5806` edge `0.0175` maxDD `-3.0178`
- `market_context_high->fx_1h` score `-0.1` n `61` status `ready` deltaP `4.8469` edge `-0.0058` maxDD `-0.7878`
- `news_risk_high->crypto_alt_1h` score `-0.1548` n `31` status `ready` deltaP `9.4939` edge `-0.0191` maxDD `-3.1233`
- `news_risk_high->fx_1h` score `-0.2692` n `31` status `ready` deltaP `-0.8644` edge `0.0024` maxDD `-0.1588`
- `market_context_high->index_1h` score `-0.5466` n `61` status `ready` deltaP `0.2135` edge `-0.0181` maxDD `-1.6054`
- `market_context_high->fx_24h` score `-0.5655` n `39` status `ready` deltaP `1.1084` edge `0.0419` maxDD `-2.3798`
- `news_risk_high->metal_1h` score `-0.6139` n `31` status `ready` deltaP `-2.6608` edge `-0.0015` maxDD `-0.5538`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
