# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T05:52:30.658788+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7862`

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

- `news_risk_high->unknown_24h` score `590.9328` n `139` status `ready` deltaP `1.2153` edge `49.2363` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `3.2697` n `139` status `ready` deltaP `16.2683` edge `0.5592` maxDD `-29.2814`
- `news_risk_high->index_24h` score `1.9352` n `139` status `ready` deltaP `20.8034` edge `0.0921` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `1.0638` n `139` status `ready` deltaP `20.3013` edge `0.1388` maxDD `-6.8392`
- `news_risk_high->equity_24h` score `0.948` n `139` status `ready` deltaP `15.1716` edge `0.2335` maxDD `-11.1179`
- `news_risk_high->equity_4h` score `0.918` n `139` status `ready` deltaP `19.3992` edge `0.1081` maxDD `-9.2079`
- `news_risk_high->crypto_major_24h` score `0.4866` n `139` status `ready` deltaP `11.6993` edge `0.406` maxDD `-26.1424`
- `news_risk_high->crypto_alt_1h` score `0.2945` n `139` status `ready` deltaP `5.6703` edge `0.0778` maxDD `-4.2849`
- `news_risk_high->index_1h` score `0.0958` n `139` status `ready` deltaP `4.7097` edge `0.0056` maxDD `-0.3214`
- `news_risk_high->equity_1h` score `0.0153` n `139` status `ready` deltaP `4.2606` edge `0.039` maxDD `-1.957`
- `news_risk_high->crypto_alt_4h` score `-0.48` n `139` status `ready` deltaP `4.8397` edge `0.1937` maxDD `-15.9436`
- `news_risk_high->metal_1h` score `-0.6107` n `139` status `ready` deltaP `0.5923` edge `0.0081` maxDD `-0.7016`
- `news_risk_high->index_4h` score `-0.7527` n `139` status `ready` deltaP `1.1702` edge `0.0148` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.9098` n `139` status `ready` deltaP `-1.9483` edge `0.0246` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.1422` n `139` status `ready` deltaP `-8.3693` edge `-0.0026` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.2103` n `139` status `ready` deltaP `10.2869` edge `-0.0024` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.6866` n `139` status `ready` deltaP `-12.5098` edge `0.0166` maxDD `-3.6214`
- `news_risk_high->commodity_1h` score `-1.9804` n `139` status `ready` deltaP `-11.1177` edge `-0.0123` maxDD `-3.3986`
- `news_risk_high->crypto_major_4h` score `-2.8079` n `139` status `ready` deltaP `-9.3591` edge `-0.0261` maxDD `-13.719`
- `news_risk_high->commodity_4h` score `-3.5712` n `139` status `ready` deltaP `-9.0356` edge `0.0045` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
