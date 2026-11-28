# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T14:52:44.158051+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7456`

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

- `news_risk_high->unknown_1h` score `3422.6424` n `31` status `ready` deltaP `2.231` edge `285.2229` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3248.6769` n `31` status `ready` deltaP `3.634` edge `270.7045` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `24.5076` n `31` status `ready` deltaP `36.9151` edge `1.7962` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `18.3568` n `31` status `ready` deltaP `34.8354` edge `1.2975` maxDD `0.0`
- `news_risk_high->equity_24h` score `13.052` n `31` status `ready` deltaP `29.2894` edge `0.8924` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `9.3144` n `31` status `ready` deltaP `24.1689` edge `0.7021` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `5.9069` n `31` status `ready` deltaP `18.3025` edge `0.777` maxDD `-7.6714`
- `news_risk_high->equity_4h` score `5.8366` n `31` status `ready` deltaP `32.3466` edge `0.3188` maxDD `-2.178`
- `news_risk_high->fx_24h` score `5.09` n `31` status `ready` deltaP `41.969` edge `0.1572` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.9578` n `31` status `ready` deltaP `17.0403` edge `0.2437` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.6024` n `31` status `ready` deltaP `31.7369` edge `0.0313` maxDD `-0.4146`
- `news_risk_high->index_24h` score `2.4549` n `31` status `ready` deltaP `26.5165` edge `0.0278` maxDD `0.0`
- `news_risk_high->index_1h` score `2.3559` n `31` status `ready` deltaP `28.8488` edge `0.0125` maxDD `-0.0136`
- `news_risk_high->equity_1h` score `2.2671` n `31` status `ready` deltaP `14.8976` edge `0.1083` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `2.1025` n `31` status `ready` deltaP `7.1663` edge `0.2679` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.9665` n `31` status `ready` deltaP `10.7591` edge `0.2161` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1535` n `31` status `ready` deltaP `24.942` edge `0.0095` maxDD `-0.2315`
- `market_context_high->metal_4h` score `0.5957` n `52` status `ready` deltaP `10.3776` edge `0.0216` maxDD `-0.2914`
- `news_risk_high->commodity_4h` score `0.4584` n `31` status `ready` deltaP `10.656` edge `0.0275` maxDD `-0.5151`
- `market_context_high->fx_1h` score `0.4234` n `64` status `ready` deltaP `11.2369` edge `0.0015` maxDD `-0.1042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
