# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T23:37:24.349062+00:00`
- Price records: `672`
- Market context records: `8352`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5886`

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

- `news_risk_high->unknown_24h` score `6252.0434` n `52` status `ready` deltaP `35.1896` edge `520.8111` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `7.6395` n `52` status `ready` deltaP `26.5244` edge `0.5195` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.9076` n `52` status `ready` deltaP `20.8314` edge `0.1343` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.7926` n `52` status `ready` deltaP `23.1707` edge `0.0973` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.2122` n `52` status `ready` deltaP `10.5886` edge `0.2824` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.7682` n `52` status `ready` deltaP `13.3579` edge `0.1017` maxDD `-1.1388`
- `news_risk_high->crypto_alt_4h` score `1.7109` n `52` status `ready` deltaP `18.0934` edge `0.2379` maxDD `-5.8012`
- `news_risk_high->crypto_major_1h` score `1.7034` n `52` status `ready` deltaP `11.7112` edge `0.1036` maxDD `-1.1783`
- `news_risk_high->metal_4h` score `0.834` n `52` status `ready` deltaP `7.6337` edge `0.0654` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.2349` n `52` status `ready` deltaP `4.445` edge `0.0188` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.0626` n `52` status `ready` deltaP `5.0438` edge `0.0025` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.2348` n `52` status `ready` deltaP `2.0498` edge `0.0071` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.5513` n `52` status `ready` deltaP `3.1309` edge `0.0042` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.2615` n `52` status `ready` deltaP `-9.7651` edge `-0.0448` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.2537` n `52` status `ready` deltaP `-22.8633` edge `-0.0532` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-6.7026` n `52` status `ready` deltaP `-25.6811` edge `-0.1103` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-9.0775` n `52` status `ready` deltaP `-31.6956` edge `-0.2144` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-11.9104` n `52` status `ready` deltaP `-9.3082` edge `-0.3365` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.0659` n `52` status `ready` deltaP `-24.0785` edge `-0.2947` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-34.6889` n `52` status `ready` deltaP `-16.9871` edge `-1.325` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
