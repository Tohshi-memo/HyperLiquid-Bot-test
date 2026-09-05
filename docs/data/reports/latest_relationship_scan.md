# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-05T16:37:24.488268+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10537`

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

- `risk_on_high->unknown_4h` score `22.0432` n `139` status `ready` deltaP `1.9488` edge `1.9362` maxDD `-3.3137`
- `risk_on_and_context->unknown_4h` score `22.0432` n `139` status `ready` deltaP `1.9488` edge `1.9362` maxDD `-3.3137`
- `market_context_high->unknown_4h` score `9.6791` n `228` status `ready` deltaP `4.0944` edge `0.9185` maxDD `-4.1365`
- `news_risk_high->crypto_alt_24h` score `7.1243` n `37` status `ready` deltaP `25.1783` edge `0.4528` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `3.7745` n `37` status `ready` deltaP `19.7917` edge `0.1826` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.5562` n `37` status `ready` deltaP `17.1803` edge `0.2231` maxDD `-0.9693`
- `news_risk_high->metal_4h` score `2.3807` n `37` status `ready` deltaP `24.1513` edge `0.0595` maxDD `-0.7692`
- `news_risk_high->commodity_4h` score `1.8193` n `37` status `ready` deltaP `10.5142` edge `0.1016` maxDD `-0.2737`
- `news_risk_high->equity_1h` score `1.5715` n `37` status `ready` deltaP `12.935` edge `0.0838` maxDD `-0.7924`
- `news_risk_high->metal_1h` score `1.2598` n `37` status `ready` deltaP `15.0146` edge `0.0242` maxDD `-0.2118`
- `news_risk_high->crypto_major_1h` score `1.1787` n `37` status `ready` deltaP `6.1661` edge `0.0754` maxDD `-0.4628`
- `news_risk_high->index_1h` score `1.1503` n `37` status `ready` deltaP `14.4239` edge `0.0131` maxDD `-0.0724`
- `news_risk_high->crypto_alt_1h` score `0.9825` n `37` status `ready` deltaP `9.326` edge `0.0462` maxDD `-0.7867`
- `news_risk_high->crypto_major_24h` score `0.9001` n `37` status `ready` deltaP `16.5776` edge `0.2825` maxDD `-18.2098`
- `news_risk_high->fx_24h` score `0.6009` n `37` status `ready` deltaP `16.31` edge `0.0429` maxDD `-3.1244`
- `news_risk_high->crypto_alt_4h` score `0.5789` n `37` status `ready` deltaP `5.941` edge `0.0415` maxDD `-1.296`
- `market_context_high->equity_24h` score `0.4961` n `180` status `ready` deltaP `14.2361` edge `0.381` maxDD `-20.7654`
- `risk_on_high->index_1h` score `-0.0039` n `148` status `ready` deltaP `6.9914` edge `-0.0024` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `-0.0039` n `148` status `ready` deltaP `6.9914` edge `-0.0024` maxDD `-0.5764`
- `news_risk_high->commodity_1h` score `-0.0332` n `37` status `ready` deltaP `5.5754` edge `0.0032` maxDD `-0.9036`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
