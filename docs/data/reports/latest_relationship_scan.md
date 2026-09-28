# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T04:52:27.711343+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7786`

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

- `news_risk_high->unknown_24h` score `590.634` n `139` status `ready` deltaP `1.2153` edge `49.2114` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `2.8229` n `139` status `ready` deltaP `15.5738` edge `0.5266` maxDD `-29.2814`
- `news_risk_high->index_24h` score `1.834` n `139` status `ready` deltaP `20.1089` edge `0.0883` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `1.005` n `139` status `ready` deltaP `20.3013` edge `0.1339` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `0.742` n `139` status `ready` deltaP `18.7895` edge `0.0975` maxDD `-9.2079`
- `news_risk_high->equity_24h` score `0.6189` n `139` status `ready` deltaP `14.4771` edge `0.2107` maxDD `-11.1179`
- `news_risk_high->crypto_alt_1h` score `0.1878` n `139` status `ready` deltaP `5.2212` edge `0.0719` maxDD `-4.2849`
- `news_risk_high->index_1h` score `0.0562` n `139` status `ready` deltaP `4.2606` edge `0.0053` maxDD `-0.3214`
- `news_risk_high->equity_1h` score `-0.041` n `139` status `ready` deltaP `3.8115` edge `0.0373` maxDD `-1.957`
- `news_risk_high->crypto_major_24h` score `-0.055` n `139` status `ready` deltaP `11.0049` edge `0.3655` maxDD `-26.1424`
- `news_risk_high->metal_1h` score `-0.6286` n `139` status `ready` deltaP `0.4426` edge `0.0076` maxDD `-0.7016`
- `news_risk_high->index_4h` score `-0.8171` n `139` status `ready` deltaP `0.5604` edge `0.0135` maxDD `-1.493`
- `news_risk_high->crypto_alt_4h` score `-0.8467` n `139` status `ready` deltaP `4.2299` edge `0.1672` maxDD `-15.9436`
- `news_risk_high->crypto_major_1h` score `-0.9691` n `139` status `ready` deltaP `-2.3974` edge `0.02` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.1072` n `139` status `ready` deltaP `-7.7705` edge `-0.0021` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.1906` n `139` status `ready` deltaP `10.5918` edge `-0.0019` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.7316` n `139` status `ready` deltaP `-13.1196` edge `0.0149` maxDD `-3.6214`
- `news_risk_high->commodity_1h` score `-1.9524` n `139` status `ready` deltaP `-10.6686` edge `-0.0117` maxDD `-3.3986`
- `news_risk_high->crypto_major_4h` score `-3.0314` n `139` status `ready` deltaP `-9.9689` edge `-0.0507` maxDD `-13.719`
- `news_risk_high->commodity_4h` score `-3.53` n `139` status `ready` deltaP `-8.7307` edge `0.0059` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
