# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T22:52:25.611453+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4102`

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

- `news_risk_high->equity_4h` score `1.182` n `79` status `ready` deltaP `10.5608` edge `0.1717` maxDD `-4.2454`
- `news_risk_high->index_4h` score `0.328` n `79` status `ready` deltaP `10.7595` edge `0.0181` maxDD `-0.4888`
- `news_risk_high->equity_1h` score `0.2406` n `79` status `ready` deltaP `4.4986` edge `0.0558` maxDD `-1.396`
- `news_risk_high->index_1h` score `0.223` n `79` status `ready` deltaP `10.4733` edge `0.0041` maxDD `-0.2931`
- `news_risk_high->fx_4h` score `0.1045` n `79` status `ready` deltaP `8.2471` edge `0.003` maxDD `-0.2336`
- `news_risk_high->index_24h` score `-0.0781` n `79` status `ready` deltaP `2.49` edge `0.1402` maxDD `-6.6786`
- `news_risk_high->fx_24h` score `-0.1846` n `79` status `ready` deltaP `-1.1583` edge `0.0366` maxDD `-0.2073`
- `news_risk_high->fx_1h` score `-0.3357` n `79` status `ready` deltaP `1.3549` edge `0.0016` maxDD `-0.0888`
- `news_risk_high->metal_1h` score `-0.4803` n `79` status `ready` deltaP `-2.9466` edge `-0.0062` maxDD `-0.5256`
- `news_risk_high->crypto_major_1h` score `-0.8248` n `79` status `ready` deltaP `-2.1849` edge `0.0027` maxDD `-4.1772`
- `news_risk_high->crypto_alt_1h` score `-1.0555` n `79` status `ready` deltaP `-0.47` edge `-0.0094` maxDD `-5.8225`
- `news_risk_high->metal_4h` score `-1.2709` n `79` status `ready` deltaP `-5.0073` edge `-0.039` maxDD `-1.5773`
- `news_risk_high->crypto_major_4h` score `-1.3408` n `79` status `ready` deltaP `-3.9132` edge `0.0228` maxDD `-9.1553`
- `news_risk_high->equity_24h` score `-2.3984` n `79` status `ready` deltaP `23.6931` edge `0.6932` maxDD `-86.0244`
- `news_risk_high->commodity_1h` score `-2.9452` n `79` status `ready` deltaP `-18.1365` edge `-0.0072` maxDD `-1.7189`
- `news_risk_high->metal_24h` score `-3.1475` n `79` status `ready` deltaP `1.9766` edge `-0.2271` maxDD `-8.5019`
- `news_risk_high->commodity_4h` score `-3.9483` n `79` status `ready` deltaP `-25.3396` edge `-0.0003` maxDD `-4.1171`
- `news_risk_high->crypto_alt_4h` score `-4.3694` n `79` status `ready` deltaP `-7.4656` edge `-0.0507` maxDD `-14.0916`
- `news_risk_high->commodity_24h` score `-9.4592` n `79` status `ready` deltaP `-26.3212` edge `-0.0426` maxDD `-28.2817`
- `news_risk_high->crypto_major_24h` score `-12.2978` n `79` status `ready` deltaP `-26.8192` edge `0.0043` maxDD `-50.6925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
