# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-10T06:52:30.349051+00:00`
- Price records: `672`
- Market context records: `6259`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11082`

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

- `news_risk_high->crypto_alt_24h` score `14.5971` n `32` status `ready` deltaP `42.5514` edge `0.9475` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `5.9825` n `32` status `ready` deltaP `50.8562` edge `0.1595` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1853` n `32` status `ready` deltaP `43.8262` edge `0.0612` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `3.5778` n `32` status `ready` deltaP `15.9675` edge `0.4302` maxDD `-4.2368`
- `news_risk_high->commodity_24h` score `2.4423` n `32` status `ready` deltaP `26.1558` edge `0.0497` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.3452` n `32` status `ready` deltaP `28.1437` edge `0.0217` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `2.2879` n `192` status `ready` deltaP `2.5605` edge `0.2744` maxDD `-3.7317`
- `market_context_high->unknown_4h` score `1.4193` n `192` status `ready` deltaP `-1.0798` edge `0.3787` maxDD `-11.925`
- `news_risk_high->crypto_major_1h` score `1.3197` n `32` status `ready` deltaP `13.6789` edge `0.1247` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.7756` n `32` status `ready` deltaP `10.4229` edge `0.0761` maxDD `-1.6923`
- `news_risk_high->index_24h` score `-0.1629` n `32` status `ready` deltaP `9.161` edge `0.0052` maxDD `-2.3058`
- `market_context_high->metal_24h` score `-0.271` n `192` status `ready` deltaP `18.3148` edge `0.1` maxDD `-11.8809`
- `market_context_high->fx_1h` score `-0.2925` n `192` status `ready` deltaP `1.0604` edge `0.0` maxDD `-0.5659`
- `market_context_high->equity_4h` score `-0.3411` n `192` status `ready` deltaP `3.7348` edge `0.0384` maxDD `-2.671`
- `market_context_high->metal_4h` score `-0.5554` n `192` status `ready` deltaP `3.3664` edge `0.0251` maxDD `-3.4996`
- `market_context_high->commodity_1h` score `-0.5571` n `192` status `ready` deltaP `-0.7485` edge `0.0032` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.7192` n `32` status `ready` deltaP `-2.6946` edge `-0.0245` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.7658` n `192` status `ready` deltaP `2.5137` edge `-0.0007` maxDD `-2.0564`
- `market_context_high->crypto_alt_1h` score `-0.8881` n `192` status `ready` deltaP `4.6937` edge `0.0301` maxDD `-9.3536`
- `market_context_high->equity_1h` score `-0.9769` n `192` status `ready` deltaP `-2.1145` edge `0.0004` maxDD `-4.2573`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
