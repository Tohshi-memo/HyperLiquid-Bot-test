# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T00:37:26.000902+00:00`
- Price records: `672`
- Market context records: `5611`
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

- `market_context_high->equity_24h` score `3.2719` n `174` status `ready` deltaP `15.0084` edge `0.6805` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `1.4586` n `223` status `ready` deltaP `13.7852` edge `0.2589` maxDD `-14.0065`
- `market_context_high->fx_24h` score `1.2878` n `174` status `ready` deltaP `21.9588` edge `0.0583` maxDD `-1.457`
- `market_context_high->crypto_alt_4h` score `0.8234` n `223` status `ready` deltaP `8.7902` edge `0.1741` maxDD `-9.46`
- `market_context_high->equity_4h` score `0.4265` n `223` status `ready` deltaP `6.0907` edge `0.1588` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.3337` n `235` status `ready` deltaP `0.5912` edge `0.0009` maxDD `-0.4764`
- `market_context_high->equity_1h` score `-0.3749` n `235` status `ready` deltaP `5.4383` edge `0.0332` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.5256` n `235` status `ready` deltaP `-0.0395` edge `0.0004` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.6022` n `235` status `ready` deltaP `1.3008` edge `0.0373` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.6175` n `235` status `ready` deltaP `4.3184` edge `0.0443` maxDD `-6.9639`
- `market_context_high->index_1h` score `-0.9031` n `235` status `ready` deltaP `0.867` edge `0.0058` maxDD `-0.9472`
- `market_context_high->commodity_1h` score `-1.145` n `235` status `ready` deltaP `-1.9149` edge `-0.0061` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.3068` n `223` status `ready` deltaP `1.0589` edge `0.0071` maxDD `-1.2021`
- `market_context_high->index_4h` score `-1.6682` n `223` status `ready` deltaP `1.5162` edge `0.0118` maxDD `-2.874`
- `market_context_high->crypto_major_24h` score `-1.8015` n `174` status `ready` deltaP `9.2852` edge `0.242` maxDD `-29.6555`
- `market_context_high->index_24h` score `-2.3886` n `174` status `ready` deltaP `10.0874` edge `0.0252` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.8205` n `223` status `ready` deltaP `-10.3413` edge `-0.0543` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-4.1811` n `223` status `ready` deltaP `-5.7858` edge `-0.0423` maxDD `-14.071`
- `market_context_high->metal_24h` score `-8.2591` n `174` status `ready` deltaP `-10.5843` edge `-0.2522` maxDD `-32.8874`
- `market_context_high->crypto_alt_24h` score `-11.7816` n `174` status `ready` deltaP `-0.9279` edge `-0.1059` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
