# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T09:07:24.322297+00:00`
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

- `news_risk_high->unknown_24h` score `49.5447` n `51` status `ready` deltaP `17.0139` edge `4.0153` maxDD `0.0`
- `news_risk_high->equity_24h` score `14.1691` n `51` status `ready` deltaP `40.237` edge `1.0056` maxDD `-4.7801`
- `news_risk_high->unknown_4h` score `13.0131` n `51` status `ready` deltaP `24.2587` edge `0.9273` maxDD `-0.0348`
- `news_risk_high->index_24h` score `5.7076` n `51` status `ready` deltaP `48.9481` edge `0.1645` maxDD `-0.2147`
- `news_risk_high->equity_4h` score `3.768` n `51` status `ready` deltaP `27.2328` edge `0.2095` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `3.6293` n `51` status `ready` deltaP `16.9337` edge `0.22` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.209` n `51` status `ready` deltaP `37.778` edge `0.029` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `1.9754` n `141` status `ready` deltaP `19.8365` edge `0.0732` maxDD `-0.5994`
- `news_risk_high->metal_24h` score `1.5779` n `51` status `ready` deltaP `33.1086` edge `-0.085` maxDD `-0.0053`
- `market_context_high->unknown_24h` score `1.4518` n `85` status `ready` deltaP `4.0727` edge `0.1445` maxDD `-1.0533`
- `news_risk_high->fx_1h` score `1.2182` n `51` status `ready` deltaP `16.696` edge `0.0072` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.9755` n `51` status `ready` deltaP `18.7918` edge `0.0362` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.9727` n `51` status `ready` deltaP `14.1589` edge `0.0264` maxDD `-0.1788`
- `news_risk_high->index_1h` score `0.2582` n `51` status `ready` deltaP `9.572` edge `0.0046` maxDD `-0.1583`
- `news_risk_high->commodity_1h` score `0.2195` n `51` status `ready` deltaP `8.8382` edge `-0.0098` maxDD `-0.4666`
- `market_context_high->metal_4h` score `0.1321` n `141` status `ready` deltaP `10.3043` edge `-0.0118` maxDD `-1.3378`
- `market_context_high->unknown_1h` score `0.0494` n `141` status `ready` deltaP `11.1765` edge `-0.0255` maxDD `-1.5916`
- `news_risk_high->metal_1h` score `-0.1138` n `51` status `ready` deltaP `2.1927` edge `-0.0069` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.2191` n `51` status `ready` deltaP `6.7582` edge `-0.0102` maxDD `-0.249`
- `news_risk_high->crypto_alt_24h` score `-0.2794` n `51` status `ready` deltaP `22.7431` edge `-0.1749` maxDD `0.0`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
