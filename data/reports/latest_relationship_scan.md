# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T03:52:25.566270+00:00`
- Price records: `672`
- Market context records: `3141`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7124`

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

- `market_context_high->commodity_24h` score `14.3345` n `107` status `ready` deltaP `47.425` edge `0.9212` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `11.9654` n `107` status `ready` deltaP `21.7078` edge `0.9012` maxDD `-1.9039`
- `market_context_high->crypto_alt_24h` score `10.9388` n `107` status `ready` deltaP `10.7428` edge `2.3284` maxDD `-71.142`
- `market_context_high->index_24h` score `6.4804` n `107` status `ready` deltaP `30.7762` edge `0.8811` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.3925` n `107` status `ready` deltaP `11.3935` edge `1.3288` maxDD `-53.663`
- `market_context_high->commodity_4h` score `2.8256` n `144` status `ready` deltaP `18.4451` edge `0.1583` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `0.151` n `146` status `ready` deltaP `4.1322` edge `0.0273` maxDD `-1.7142`
- `market_context_high->crypto_alt_1h` score `-0.3852` n `146` status `ready` deltaP `6.2054` edge `0.1222` maxDD `-14.7034`
- `market_context_high->fx_24h` score `-0.4426` n `107` status `ready` deltaP `5.562` edge `-0.0012` maxDD `-0.4876`
- `market_context_high->index_1h` score `-0.5156` n `146` status `ready` deltaP `3.5518` edge `0.0165` maxDD `-4.5023`
- `market_context_high->equity_1h` score `-0.8161` n `146` status `ready` deltaP `3.4882` edge `0.0207` maxDD `-8.8863`
- `market_context_high->crypto_major_1h` score `-0.9601` n `146` status `ready` deltaP `3.3754` edge `0.0807` maxDD `-15.1032`
- `market_context_high->fx_1h` score `-1.1197` n `146` status `ready` deltaP `-10.4688` edge `-0.0055` maxDD `-0.7941`
- `market_context_high->index_4h` score `-1.1536` n `144` status `ready` deltaP `11.8056` edge `0.0643` maxDD `-17.6057`
- `market_context_high->fx_4h` score `-1.5217` n `144` status `ready` deltaP `-14.7019` edge `-0.0086` maxDD `-1.4115`
- `market_context_high->unknown_4h` score `-1.726` n `144` status `ready` deltaP `5.4878` edge `0.0418` maxDD `-14.7778`
- `market_context_high->metal_1h` score `-2.0684` n `146` status `ready` deltaP `-4.3044` edge `-0.0043` maxDD `-7.4828`
- `market_context_high->equity_4h` score `-2.8527` n `144` status `ready` deltaP `13.4146` edge `0.0754` maxDD `-36.7784`
- `market_context_high->crypto_alt_4h` score `-2.9154` n `144` status `ready` deltaP `19.4444` edge `0.4319` maxDD `-58.6918`
- `market_context_high->unknown_1h` score `-3.1453` n `146` status `ready` deltaP `1.7595` edge `-0.0712` maxDD `-14.2111`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
