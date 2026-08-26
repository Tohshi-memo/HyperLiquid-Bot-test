# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-26T06:37:28.435715+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14760`

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

- `news_risk_high->unknown_24h` score `46.5738` n `51` status `ready` deltaP `11.6319` edge `3.8036` maxDD `0.0`
- `news_risk_high->unknown_4h` score `11.7476` n `53` status `ready` deltaP `22.8457` edge `0.8366` maxDD `-0.1281`
- `news_risk_high->crypto_alt_24h` score `7.9778` n `51` status `ready` deltaP `30.9028` edge `0.4588` maxDD `0.0`
- `news_risk_high->equity_24h` score `7.0677` n `51` status `ready` deltaP `29.9939` edge `0.4821` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.046` n `51` status `ready` deltaP `40.2676` edge `0.0839` maxDD `-0.2147`
- `news_risk_high->fx_4h` score `2.7779` n `53` status `ready` deltaP `33.4388` edge `0.022` maxDD `-0.0746`
- `news_risk_high->unknown_1h` score `2.7435` n `53` status `ready` deltaP `15.4135` edge `0.1614` maxDD `-0.8426`
- `market_context_high->unknown_4h` score `2.4728` n `134` status `ready` deltaP `21.0434` edge `0.1066` maxDD `-0.5994`
- `news_risk_high->equity_4h` score `1.7351` n `53` status `ready` deltaP `19.4317` edge `0.0921` maxDD `-2.164`
- `news_risk_high->metal_24h` score `1.3953` n `51` status `ready` deltaP `29.1156` edge `-0.0736` maxDD `-0.0053`
- `news_risk_high->fx_1h` score `1.0698` n `53` status `ready` deltaP `15.0209` edge `0.006` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `1.0618` n `136` status `ready` deltaP `11.4873` edge `0.0568` maxDD `-1.5916`
- `news_risk_high->commodity_1h` score `0.4511` n `53` status `ready` deltaP `10.9762` edge `-0.0043` maxDD `-0.5024`
- `news_risk_high->equity_1h` score `0.4326` n `53` status `ready` deltaP `12.9251` edge `0.0057` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.0293` n `53` status `ready` deltaP `5.4418` edge `0.0059` maxDD `-0.1788`
- `news_risk_high->index_1h` score `-0.0752` n `53` status `ready` deltaP `3.8499` edge `0.0` maxDD `-0.1583`
- `market_context_high->fx_1h` score `-0.4434` n `136` status `ready` deltaP `2.5625` edge `-0.0007` maxDD `-0.8587`
- `news_risk_high->metal_1h` score `-0.5169` n `53` status `ready` deltaP `-1.2117` edge `-0.0124` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.7577` n `53` status `ready` deltaP `2.6806` edge `-0.0279` maxDD `-0.249`
- `news_risk_high->commodity_4h` score `-1.0466` n `53` status `ready` deltaP `-2.1255` edge `0.0033` maxDD `-1.1986`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
