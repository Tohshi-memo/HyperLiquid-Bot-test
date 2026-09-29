# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T14:22:30.347447+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7522`

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

- `news_risk_high->unknown_24h` score `2584.0512` n `139` status `ready` deltaP `1.2153` edge `215.3295` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.9227` n `139` status `ready` deltaP `32.7613` edge `1.587` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `10.499` n `139` status `ready` deltaP `35.4841` edge `0.894` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `8.5889` n `139` status `ready` deltaP `25.5882` edge `0.9886` maxDD `-26.1424`
- `news_risk_high->index_24h` score `4.3275` n `139` status `ready` deltaP `39.727` edge `0.1653` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `3.8724` n `139` status `ready` deltaP `31.9332` edge `0.2953` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.7312` n `142` status `ready` deltaP `27.9801` edge `0.202` maxDD `-9.2079`
- `news_risk_high->crypto_alt_4h` score `1.0259` n `142` status `ready` deltaP `8.6332` edge `0.2939` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.7177` n `142` status `ready` deltaP `6.8209` edge `0.1054` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.6338` n `142` status `ready` deltaP `7.7022` edge `0.0676` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4934` n `142` status `ready` deltaP `8.8998` edge `0.0108` maxDD `-0.3214`
- `news_risk_high->index_4h` score `0.0235` n `142` status `ready` deltaP `8.6826` edge `0.0294` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.4188` n `142` status `ready` deltaP `1.9904` edge `0.0613` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.5241` n `142` status `ready` deltaP `1.0141` edge `0.0125` maxDD `-0.7016`
- `news_risk_high->fx_4h` score `-1.319` n `142` status `ready` deltaP `8.8265` edge `-0.0066` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.3642` n `142` status `ready` deltaP `-8.1544` edge `0.0289` maxDD `-3.6214`
- `news_risk_high->crypto_major_4h` score `-1.7943` n `142` status `ready` deltaP `-4.9876` edge `0.0747` maxDD `-13.719`
- `news_risk_high->fx_1h` score `-1.8325` n `142` status `ready` deltaP `-9.1444` edge `-0.0037` maxDD `-1.0436`
- `news_risk_high->commodity_1h` score `-1.9219` n `142` status `ready` deltaP `-10.2028` edge `-0.0109` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-2.3955` n `142` status `ready` deltaP `-10.222` edge `0.0029` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
