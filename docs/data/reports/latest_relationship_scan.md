# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-11T04:36:10.183586+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11808`

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

- `market_context_high->unknown_24h` score `28.0643` n `137` status `ready` deltaP `-16.335` edge `2.693` maxDD `-9.6329`
- `market_context_high->commodity_4h` score `0.7733` n `169` status `ready` deltaP `11.2057` edge `0.0612` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.6429` n `180` status `ready` deltaP `8.9055` edge `0.0285` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.6107` n `137` status `ready` deltaP `18.8783` edge `0.0332` maxDD `-1.4613`
- `market_context_high->fx_4h` score `-0.2201` n `169` status `ready` deltaP `4.2077` edge `0.0042` maxDD `-0.504`
- `market_context_high->fx_1h` score `-0.2302` n `180` status `ready` deltaP `2.4983` edge `-0.001` maxDD `-0.613`
- `market_context_high->commodity_24h` score `-0.6263` n `137` status `ready` deltaP `10.4766` edge `0.132` maxDD `-15.9044`
- `market_context_high->index_1h` score `-0.8397` n `180` status `ready` deltaP `-6.67` edge `-0.0044` maxDD `-1.0359`
- `market_context_high->index_4h` score `-1.0348` n `169` status `ready` deltaP `-4.8202` edge `-0.0111` maxDD `-1.4875`
- `market_context_high->metal_1h` score `-1.2996` n `180` status `ready` deltaP `-5.2195` edge `-0.0099` maxDD `-2.0884`
- `market_context_high->equity_1h` score `-1.4778` n `180` status `ready` deltaP `-6.4604` edge `-0.0187` maxDD `-6.8818`
- `market_context_high->metal_24h` score `-2.1465` n `137` status `ready` deltaP `1.1341` edge `-0.054` maxDD `-2.9283`
- `market_context_high->index_24h` score `-2.5147` n `137` status `ready` deltaP `-11.9946` edge `-0.0329` maxDD `-6.7627`
- `market_context_high->crypto_alt_1h` score `-2.5804` n `180` status `ready` deltaP `-8.7026` edge `-0.0385` maxDD `-6.4812`
- `market_context_high->metal_4h` score `-3.1963` n `169` status `ready` deltaP `-7.9004` edge `-0.0373` maxDD `-6.1111`
- `market_context_high->crypto_major_1h` score `-3.377` n `180` status `ready` deltaP `-6.9893` edge `-0.0444` maxDD `-11.9002`
- `market_context_high->equity_4h` score `-4.1673` n `169` status `ready` deltaP `-14.3048` edge `-0.128` maxDD `-15.8728`
- `market_context_high->crypto_alt_4h` score `-6.4095` n `169` status `ready` deltaP `-10.6536` edge `-0.1283` maxDD `-20.1177`
- `market_context_high->crypto_major_24h` score `-6.8862` n `137` status `ready` deltaP `-14.298` edge `-0.2104` maxDD `-33.5037`
- `market_context_high->crypto_alt_24h` score `-9.1412` n `137` status `ready` deltaP `-11.0474` edge `-0.2083` maxDD `-27.3857`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
