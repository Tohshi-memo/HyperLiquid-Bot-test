# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T01:07:24.708278+00:00`
- Price records: `672`
- Market context records: `5613`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11433`

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

- `market_context_high->equity_24h` score `3.2143` n `174` status `ready` deltaP `15.0084` edge `0.6757` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `1.3833` n `225` status `ready` deltaP `13.504` edge `0.2545` maxDD `-14.0065`
- `market_context_high->fx_24h` score `1.3076` n `174` status `ready` deltaP `22.1325` edge `0.0588` maxDD `-1.457`
- `market_context_high->crypto_alt_4h` score `0.7192` n `225` status `ready` deltaP `8.3727` edge `0.1682` maxDD `-9.46`
- `market_context_high->equity_4h` score `0.4476` n `225` status `ready` deltaP `6.4295` edge `0.1583` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.3202` n `237` status `ready` deltaP `0.8508` edge `0.0009` maxDD `-0.4764`
- `market_context_high->equity_1h` score `-0.3427` n `237` status `ready` deltaP `5.7651` edge `0.0337` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.5325` n `237` status `ready` deltaP `-0.1567` edge `0.0003` maxDD `-2.0682`
- `market_context_high->crypto_major_1h` score `-0.6397` n `237` status `ready` deltaP `4.2807` edge `0.0427` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `-0.6848` n `237` status `ready` deltaP `0.8376` edge `0.0335` maxDD `-5.0257`
- `market_context_high->index_1h` score `-0.9178` n `237` status `ready` deltaP `0.7283` edge `0.0055` maxDD `-0.9472`
- `market_context_high->commodity_1h` score `-1.1351` n `237` status `ready` deltaP `-1.7762` edge `-0.0062` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.2935` n `225` status `ready` deltaP `1.313` edge `0.0071` maxDD `-1.2021`
- `market_context_high->index_4h` score `-1.6884` n `225` status `ready` deltaP `1.3388` edge `0.0113` maxDD `-2.874`
- `market_context_high->crypto_major_24h` score `-2.0045` n `174` status `ready` deltaP `8.938` edge `0.2274` maxDD `-29.6555`
- `market_context_high->index_24h` score `-2.391` n `174` status `ready` deltaP `10.0874` edge `0.0249` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.8202` n `225` status `ready` deltaP `-10.3672` edge `-0.0541` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-4.1531` n `225` status `ready` deltaP `-5.5406` edge `-0.0416` maxDD `-14.071`
- `market_context_high->metal_24h` score `-8.2834` n `174` status `ready` deltaP `-10.9315` edge `-0.253` maxDD `-32.8874`
- `market_context_high->crypto_alt_24h` score `-11.9462` n `174` status `ready` deltaP `-1.2751` edge `-0.1173` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
