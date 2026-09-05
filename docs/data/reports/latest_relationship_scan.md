# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-05T06:07:23.319778+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10634`

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

- `risk_on_high->unknown_4h` score `19.5868` n `133` status `ready` deltaP `7.779` edge `1.6422` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `19.5868` n `133` status `ready` deltaP `7.779` edge `1.6422` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `8.1548` n `221` status `ready` deltaP `7.2585` edge `0.7042` maxDD `-2.8419`
- `news_risk_high->crypto_alt_24h` score `7.3823` n `37` status `ready` deltaP `25.1783` edge `0.4743` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `4.3352` n `37` status `ready` deltaP `25.0` edge `0.1946` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.8026` n `37` status `ready` deltaP `17.4852` edge `0.2416` maxDD `-0.9693`
- `news_risk_high->metal_4h` score `2.1664` n `37` status `ready` deltaP `21.7123` edge `0.0579` maxDD `-0.7692`
- `news_risk_high->commodity_4h` score `1.8009` n `37` status `ready` deltaP `10.2093` edge `0.1021` maxDD `-0.2737`
- `news_risk_high->equity_1h` score `1.6386` n `37` status `ready` deltaP `13.6835` edge `0.0844` maxDD `-0.7924`
- `news_risk_high->crypto_major_1h` score `1.3417` n `37` status `ready` deltaP `7.3637` edge `0.081` maxDD `-0.4628`
- `news_risk_high->index_1h` score `1.2245` n `37` status `ready` deltaP `15.3221` edge `0.0133` maxDD `-0.0724`
- `news_risk_high->metal_1h` score `1.17` n `37` status `ready` deltaP `13.9667` edge `0.0237` maxDD `-0.2118`
- `news_risk_high->crypto_alt_1h` score `1.0065` n `37` status `ready` deltaP `9.1763` edge `0.0492` maxDD `-0.7867`
- `news_risk_high->crypto_alt_4h` score `0.8846` n `37` status `ready` deltaP `7.6179` edge `0.0558` maxDD `-1.296`
- `news_risk_high->fx_24h` score `0.1738` n `37` status `ready` deltaP `11.7961` edge `0.0374` maxDD `-3.1244`
- `risk_on_high->metal_1h` score `0.0916` n `141` status `ready` deltaP `12.2224` edge `0.0015` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0916` n `141` status `ready` deltaP `12.2224` edge `0.0015` maxDD `-1.699`
- `news_risk_high->crypto_major_24h` score `0.0808` n `37` status `ready` deltaP `12.2373` edge `0.2064` maxDD `-18.2098`
- `news_risk_high->commodity_1h` score `-0.0247` n `37` status `ready` deltaP `5.7251` edge `0.0033` maxDD `-0.9036`
- `risk_on_high->index_1h` score `-0.1393` n `141` status `ready` deltaP `4.4921` edge `-0.0031` maxDD `-0.5764`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
