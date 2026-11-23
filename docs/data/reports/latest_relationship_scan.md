# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T01:37:29.982393+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5282`

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

- `market_context_high->unknown_1h` score `14555.6346` n `91` status `ready` deltaP `0.7386` edge `1212.9808` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `9358.2633` n `91` status `ready` deltaP `-1.1692` edge `779.8936` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1360.6509` n `31` status `ready` deltaP `4.1771` edge `113.3773` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1195.5738` n `31` status `ready` deltaP `4.3962` edge `99.6075` maxDD `-0.119`
- `news_risk_high->equity_4h` score `11.8335` n `31` status `ready` deltaP `38.9015` edge `0.775` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `11.0311` n `31` status `ready` deltaP `25.6933` edge `0.835` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `6.6555` n `31` status `ready` deltaP `14.3391` edge `0.8994` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.9966` n `31` status `ready` deltaP `19.8377` edge `0.2195` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.533` n `31` status `ready` deltaP `36.9198` edge `0.0743` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.719` n `31` status `ready` deltaP `31.8428` edge `0.0228` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4727` n `31` status `ready` deltaP `9.8609` edge `0.2974` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.0744` n `31` status `ready` deltaP `8.5136` edge `0.2449` maxDD `-1.5232`
- `news_risk_high->metal_4h` score `1.5696` n `31` status `ready` deltaP `21.5037` edge `0.1136` maxDD `-0.7918`
- `news_risk_high->metal_1h` score `1.568` n `31` status `ready` deltaP `29.5827` edge `0.0317` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.7904` n `31` status `ready` deltaP `17.8206` edge `0.0223` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.0645` n `31` status `ready` deltaP `1.3811` edge `0.0116` maxDD `-0.0947`
- `market_context_high->fx_4h` score `-0.4486` n `91` status `ready` deltaP `7.2249` edge `0.0104` maxDD `-0.9531`
- `market_context_high->index_1h` score `-0.5072` n `91` status `ready` deltaP `0.6481` edge `-0.001` maxDD `-0.9806`
- `market_context_high->metal_1h` score `-0.5564` n `91` status `ready` deltaP `1.543` edge `-0.0008` maxDD `-1.8013`
- `market_context_high->fx_1h` score `-1.2781` n `91` status `ready` deltaP `-9.5924` edge `-0.001` maxDD `-0.325`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
