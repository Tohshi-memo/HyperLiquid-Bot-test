# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T07:37:26.521329+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5234`

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

- `market_context_high->unknown_1h` score `17449.955` n `78` status `ready` deltaP `2.0382` edge `1454.1655` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `11468.7203` n `78` status `ready` deltaP `3.6233` edge `955.7164` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1315.4651` n `31` status `ready` deltaP `3.2789` edge `109.6178` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1168.6876` n `31` status `ready` deltaP `4.2437` edge `97.368` maxDD `-0.119`
- `news_risk_high->equity_4h` score `11.0554` n `31` status `ready` deltaP `35.7003` edge `0.7315` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `10.4404` n `31` status `ready` deltaP `23.5592` edge `0.8` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `6.3249` n `31` status `ready` deltaP `12.6623` edge `0.8682` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.7795` n `31` status `ready` deltaP `18.9395` edge `0.2074` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.4882` n `31` status `ready` deltaP `36.6149` edge `0.0726` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6651` n `31` status `ready` deltaP `31.244` edge `0.0223` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.3963` n `31` status `ready` deltaP `9.4118` edge `0.2906` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.9731` n `31` status `ready` deltaP `7.7651` edge `0.2369` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.4994` n `31` status `ready` deltaP `28.6845` edge `0.0289` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.408` n `31` status `ready` deltaP `19.522` edge `0.1061` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.8359` n `31` status `ready` deltaP `18.1255` edge `0.0261` maxDD `-0.5151`
- `market_context_high->fx_4h` score `0.4067` n `78` status `ready` deltaP `14.3723` edge `0.0153` maxDD `-0.3845`
- `news_risk_high->commodity_1h` score `-0.0166` n `31` status `ready` deltaP `1.6805` edge `0.0136` maxDD `-0.0947`
- `market_context_high->metal_1h` score `-0.15` n `78` status `ready` deltaP `3.2089` edge `0.0112` maxDD `-1.4794`
- `market_context_high->index_1h` score `-0.2313` n `78` status `ready` deltaP `1.8809` edge `0.0034` maxDD `-0.9806`
- `market_context_high->metal_4h` score `-0.8574` n `78` status `ready` deltaP `8.2317` edge `0.0141` maxDD `-6.9009`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
