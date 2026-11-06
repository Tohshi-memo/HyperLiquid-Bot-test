# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T20:07:29.348997+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4184`

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

- `news_risk_high->equity_4h` score `1.8276` n `90` status `ready` deltaP `15.2066` edge `0.2235` maxDD `-4.2454`
- `news_risk_high->index_4h` score `0.8644` n `90` status `ready` deltaP `14.641` edge `0.0222` maxDD `-0.4888`
- `news_risk_high->equity_1h` score `0.4275` n `90` status `ready` deltaP `5.6188` edge `0.0723` maxDD `-1.396`
- `news_risk_high->index_1h` score `0.3059` n `90` status `ready` deltaP `11.7964` edge `0.0059` maxDD `-0.2931`
- `news_risk_high->fx_4h` score `-0.2417` n `90` status `ready` deltaP `2.2256` edge `-0.0007` maxDD `-0.2767`
- `news_risk_high->metal_1h` score `-0.3036` n `90` status `ready` deltaP `0.2129` edge `-0.0046` maxDD `-0.5256`
- `news_risk_high->fx_1h` score `-0.3998` n `90` status `ready` deltaP `-1.67` edge `-0.0003` maxDD `-0.1858`
- `news_risk_high->crypto_major_4h` score `-0.4351` n `90` status `ready` deltaP `2.1341` edge `0.0986` maxDD `-9.1553`
- `news_risk_high->index_24h` score `-0.5574` n `90` status `ready` deltaP `-0.5353` edge `0.1406` maxDD `-6.6786`
- `news_risk_high->crypto_alt_1h` score `-0.5679` n `90` status `ready` deltaP `3.2069` edge `0.0286` maxDD `-5.8225`
- `news_risk_high->crypto_major_1h` score `-0.7632` n `90` status `ready` deltaP `-2.0492` edge `0.0097` maxDD `-4.1772`
- `news_risk_high->equity_24h` score `-0.8629` n `90` status `ready` deltaP `27.4061` edge `0.8653` maxDD `-86.0244`
- `news_risk_high->fx_24h` score `-0.9379` n `90` status `ready` deltaP `-8.1012` edge `0.0203` maxDD `-0.2229`
- `news_risk_high->metal_4h` score `-0.9754` n `90` status `ready` deltaP `-0.3895` edge `-0.0319` maxDD `-1.5773`
- `news_risk_high->crypto_alt_4h` score `-1.2877` n `90` status `ready` deltaP `-1.416` edge `0.108` maxDD `-14.0916`
- `news_risk_high->metal_24h` score `-2.9248` n `90` status `ready` deltaP `4.04` edge `-0.2123` maxDD `-8.5019`
- `news_risk_high->commodity_1h` score `-3.1003` n `90` status `ready` deltaP `-18.5263` edge `-0.0106` maxDD `-2.273`
- `news_risk_high->commodity_4h` score `-4.2537` n `90` status `ready` deltaP `-26.6023` edge `-0.0049` maxDD `-5.1112`
- `news_risk_high->crypto_major_24h` score `-6.7896` n `90` status `ready` deltaP `-17.9761` edge `0.0997` maxDD `-50.6925`
- `news_risk_high->commodity_24h` score `-9.3189` n `90` status `ready` deltaP `-25.4978` edge `-0.0142` maxDD `-30.0579`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
