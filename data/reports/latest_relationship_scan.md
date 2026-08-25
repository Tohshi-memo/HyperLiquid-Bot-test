# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T18:37:30.568879+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14792`

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

- `news_risk_high->unknown_24h` score `44.5057` n `51` status `ready` deltaP `6.0764` edge `3.6683` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.5594` n `53` status `ready` deltaP `24.2176` edge `0.8951` maxDD `-0.1281`
- `news_risk_high->equity_24h` score `7.8715` n `51` status `ready` deltaP `30.862` edge `0.5433` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.125` n `51` status `ready` deltaP `41.1356` edge `0.0847` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.1742` n `53` status `ready` deltaP `16.162` edge `0.1923` maxDD `-0.8426`
- `news_risk_high->fx_4h` score `3.0392` n `53` status `ready` deltaP `36.0303` edge `0.0265` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `2.6008` n `133` status `ready` deltaP `22.3592` edge `0.1085` maxDD `-0.5994`
- `news_risk_high->equity_4h` score `1.6647` n `53` status `ready` deltaP `19.7365` edge `0.0842` maxDD `-2.164`
- `news_risk_high->fx_1h` score `1.1752` n `53` status `ready` deltaP `16.2185` edge `0.0068` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.4839` n `53` status `ready` deltaP `13.973` edge `0.0053` maxDD `-0.9128`
- `news_risk_high->commodity_1h` score `0.3828` n `53` status `ready` deltaP `10.3774` edge `-0.006` maxDD `-0.5024`
- `news_risk_high->index_4h` score `0.2292` n `53` status `ready` deltaP `7.8808` edge `0.0063` maxDD `-0.1788`
- `market_context_high->unknown_1h` score `0.1566` n `133` status `ready` deltaP `11.7216` edge `-0.0202` maxDD `-1.5916`
- `news_risk_high->crypto_alt_24h` score `0.0284` n `51` status `ready` deltaP `22.5694` edge `-0.1481` maxDD `0.0`
- `news_risk_high->metal_24h` score `0.0109` n `51` status `ready` deltaP `25.2961` edge `-0.1635` maxDD `-0.0053`
- `news_risk_high->index_1h` score `-0.048` n `53` status `ready` deltaP `4.299` edge `0.0005` maxDD `-0.1583`
- `market_context_high->fx_1h` score `-0.4273` n `133` status `ready` deltaP `2.7982` edge `-0.0002` maxDD `-0.8587`
- `news_risk_high->metal_1h` score `-0.4678` n `53` status `ready` deltaP `-0.7626` edge `-0.0113` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.584` n `53` status `ready` deltaP `4.3574` edge `-0.0246` maxDD `-0.249`
- `market_context_high->metal_4h` score `-1.0844` n `133` status `ready` deltaP `3.3502` edge `-0.049` maxDD `-2.4293`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
