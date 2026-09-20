# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T17:22:27.254837+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9862`

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

- `news_risk_high->crypto_major_24h` score `23.15` n `98` status `ready` deltaP `9.8392` edge `2.5494` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `20.3475` n `98` status `ready` deltaP `15.0935` edge `2.0831` maxDD `-32.7147`
- `market_context_high->unknown_4h` score `15.8141` n `47` status `ready` deltaP `0.0194` edge `1.3327` maxDD `-0.5326`
- `news_risk_high->crypto_alt_4h` score `5.7591` n `101` status `ready` deltaP `23.0349` edge `0.4473` maxDD `-7.675`
- `market_context_high->commodity_4h` score `4.4223` n `47` status `ready` deltaP `36.4718` edge `0.1387` maxDD `-0.0659`
- `news_risk_high->crypto_major_4h` score `4.3976` n `101` status `ready` deltaP `21.9678` edge `0.3458` maxDD `-8.0625`
- `market_context_high->commodity_24h` score `3.5784` n `36` status `ready` deltaP `21.5278` edge `0.2072` maxDD `-0.8682`
- `news_risk_high->crypto_alt_1h` score `2.9285` n `101` status `ready` deltaP `16.6805` edge `0.1794` maxDD `-2.058`
- `market_context_high->fx_4h` score `2.2646` n `47` status `ready` deltaP `29.3137` edge `0.0148` maxDD `-0.0543`
- `news_risk_high->crypto_major_1h` score `2.1767` n `101` status `ready` deltaP `18.4769` edge `0.1105` maxDD `-2.8494`
- `market_context_high->fx_24h` score `2.0111` n `36` status `ready` deltaP `20.8333` edge `0.0329` maxDD `-0.0027`
- `market_context_high->commodity_1h` score `1.3691` n `52` status `ready` deltaP `15.3616` edge `0.0392` maxDD `-0.2012`
- `market_context_high->fx_1h` score `1.3267` n `52` status `ready` deltaP `17.9871` edge `0.0081` maxDD `-0.063`
- `news_risk_high->commodity_24h` score `1.0651` n `98` status `ready` deltaP `22.775` edge `0.1153` maxDD `-3.4467`
- `news_risk_high->metal_4h` score `0.6628` n `101` status `ready` deltaP `17.5561` edge `0.0436` maxDD `-2.0994`
- `news_risk_high->metal_1h` score `0.6173` n `101` status `ready` deltaP `14.4483` edge `0.0153` maxDD `-0.8144`
- `news_risk_high->equity_24h` score `0.5849` n `98` status `ready` deltaP `16.571` edge `0.0792` maxDD `-4.941`
- `market_context_high->metal_1h` score `0.438` n `52` status `ready` deltaP `10.6403` edge `0.0076` maxDD `-0.4568`
- `news_risk_high->equity_1h` score `0.2197` n `101` status `ready` deltaP `5.2143` edge `0.0241` maxDD `-0.9112`
- `news_risk_high->metal_24h` score `0.1722` n `98` status `ready` deltaP `14.9837` edge `0.0066` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
