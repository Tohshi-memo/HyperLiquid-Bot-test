# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T18:52:35.340941+00:00`
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

- `market_context_high->unknown_24h` score `45.7418` n `39` status `ready` deltaP `29.6875` edge `3.6139` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `11.3865` n `39` status `ready` deltaP `50.1202` edge `0.6321` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `11.2025` n `39` status `ready` deltaP `53.6458` edge `0.5759` maxDD `0.0`
- `news_risk_high->fx_24h` score `0.9689` n `31` status `ready` deltaP `12.192` edge `0.0647` maxDD `-1.5526`
- `news_risk_high->commodity_1h` score `0.8906` n `31` status `ready` deltaP `19.0892` edge `0.0081` maxDD `-0.6947`
- `news_risk_high->equity_4h` score `0.7544` n `31` status `ready` deltaP `-7.2777` edge `0.1798` maxDD `-2.8064`
- `market_context_high->commodity_1h` score `0.4353` n `60` status `ready` deltaP `9.6806` edge `0.0287` maxDD `-1.3282`
- `market_context_high->commodity_4h` score `0.3474` n `48` status `ready` deltaP `5.5894` edge `0.0919` maxDD `-2.7703`
- `news_risk_high->index_4h` score `0.121` n `31` status `ready` deltaP `-0.3688` edge `0.0506` maxDD `-0.3783`
- `news_risk_high->fx_4h` score `0.1051` n `31` status `ready` deltaP `4.2831` edge `0.0352` maxDD `-0.356`
- `market_context_high->fx_4h` score `0.0689` n `48` status `ready` deltaP `14.4309` edge `-0.0048` maxDD `-1.8531`
- `news_risk_high->commodity_4h` score `0.0571` n `31` status `ready` deltaP `11.5706` edge `-0.0223` maxDD `-1.6728`
- `market_context_high->fx_1h` score `-0.0268` n `60` status `ready` deltaP `5.7485` edge `-0.0058` maxDD `-0.7804`
- `news_risk_high->index_1h` score `-0.0734` n `31` status `ready` deltaP `2.4435` edge `-0.0059` maxDD `-0.5845`
- `market_context_high->crypto_alt_1h` score `-0.1452` n `60` status `ready` deltaP `4.8703` edge `0.0158` maxDD `-3.0178`
- `news_risk_high->crypto_alt_1h` score `-0.1587` n `31` status `ready` deltaP `9.4939` edge `-0.0196` maxDD `-3.1233`
- `news_risk_high->fx_1h` score `-0.2692` n `31` status `ready` deltaP `-0.8644` edge `0.0024` maxDD `-0.1588`
- `market_context_high->index_1h` score `-0.5089` n `60` status `ready` deltaP `0.9381` edge `-0.0181` maxDD `-1.6054`
- `market_context_high->fx_24h` score `-0.5679` n `39` status `ready` deltaP `1.1084` edge `0.0417` maxDD `-2.3798`
- `news_risk_high->metal_1h` score `-0.6139` n `31` status `ready` deltaP `-2.6608` edge `-0.0015` maxDD `-0.5538`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
