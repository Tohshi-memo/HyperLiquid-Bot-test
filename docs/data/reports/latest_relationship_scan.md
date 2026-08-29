# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T10:07:25.856566+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11772`

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

- `news_risk_high->unknown_24h` score `49.2112` n `56` status `ready` deltaP `13.4176` edge `4.066` maxDD `-2.3617`
- `news_risk_high->crypto_alt_24h` score `24.1396` n `56` status `ready` deltaP `36.2351` edge `1.9907` maxDD `-14.9839`
- `market_context_high->unknown_24h` score `8.2988` n `114` status `ready` deltaP `17.1144` edge `0.6507` maxDD `-3.1917`
- `news_risk_high->unknown_4h` score `6.2807` n `80` status `ready` deltaP `10.9756` edge `0.5092` maxDD `-1.7183`
- `market_context_high->metal_24h` score `3.8386` n `114` status `ready` deltaP `30.72` edge `0.217` maxDD `-3.1535`
- `market_context_high->unknown_4h` score `2.7423` n `114` status `ready` deltaP `19.3089` edge `0.1405` maxDD `-0.5894`
- `news_risk_high->unknown_1h` score `2.6967` n `80` status `ready` deltaP `5.8234` edge `0.2216` maxDD `-0.8558`
- `news_risk_high->equity_24h` score `2.4572` n `56` status `ready` deltaP `22.3958` edge `0.3549` maxDD `-12.4677`
- `news_risk_high->fx_4h` score `2.3681` n `80` status `ready` deltaP `34.5122` edge `0.0222` maxDD `-0.3953`
- `news_risk_high->crypto_major_24h` score `1.9772` n `56` status `ready` deltaP `19.2708` edge `0.3649` maxDD `-16.524`
- `news_risk_high->metal_24h` score `1.5897` n `56` status `ready` deltaP `35.7639` edge `0.0368` maxDD `-3.7137`
- `news_risk_high->index_24h` score `1.2878` n `56` status `ready` deltaP `18.6756` edge `0.0248` maxDD `-1.0255`
- `market_context_high->unknown_1h` score `1.0191` n `119` status `ready` deltaP `8.0713` edge `0.0803` maxDD `-1.6015`
- `news_risk_high->fx_1h` score `0.6992` n `80` status `ready` deltaP `13.7425` edge `0.0055` maxDD `-0.108`
- `news_risk_high->commodity_1h` score `0.4501` n `80` status `ready` deltaP `12.6497` edge `0.0054` maxDD `-0.5618`
- `market_context_high->metal_4h` score `-0.2304` n `114` status `ready` deltaP `7.9777` edge `0.009` maxDD `-3.3377`
- `news_risk_high->index_1h` score `-0.391` n `80` status `ready` deltaP `0.3069` edge `-0.0085` maxDD `-0.8275`
- `news_risk_high->index_4h` score `-0.5364` n `80` status `ready` deltaP `1.7683` edge `-0.0164` maxDD `-1.7996`
- `news_risk_high->commodity_4h` score `-0.5807` n `80` status `ready` deltaP `7.3476` edge `0.0107` maxDD `-2.0635`
- `news_risk_high->equity_1h` score `-0.6139` n `80` status `ready` deltaP `8.1587` edge `-0.0397` maxDD `-5.1385`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
