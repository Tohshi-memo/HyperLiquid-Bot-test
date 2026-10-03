# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T12:52:23.986125+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4834`

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

- `market_context_high->unknown_1h` score `366.5565` n `50` status `ready` deltaP `11.1737` edge `30.4768` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `294.6968` n `50` status `ready` deltaP `12.0244` edge `24.4779` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `13.7908` n `50` status `ready` deltaP `28.766` edge `1.1278` maxDD `-11.6271`
- `market_context_high->crypto_major_24h` score `11.2653` n `50` status `ready` deltaP `36.4194` edge `0.8376` maxDD `-9.3299`
- `news_risk_high->crypto_major_4h` score `11.1419` n `62` status `ready` deltaP `39.2424` edge `0.6872` maxDD `-0.6258`
- `news_risk_high->equity_24h` score `10.3455` n `62` status `ready` deltaP `28.0511` edge `0.7236` maxDD `-2.8784`
- `news_risk_high->crypto_alt_4h` score `7.6964` n `62` status `ready` deltaP `27.2819` edge `0.5939` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.4833` n `50` status `ready` deltaP `18.5327` edge `0.5704` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `6.3642` n `50` status `ready` deltaP `18.2496` edge `0.5376` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.5215` n `62` status `ready` deltaP `32.7696` edge `0.1742` maxDD `-0.2696`
- `news_risk_high->equity_4h` score `4.0138` n `62` status `ready` deltaP `27.007` edge `0.2157` maxDD `-2.9013`
- `market_context_high->crypto_alt_1h` score `3.289` n `50` status `ready` deltaP `14.8024` edge `0.2417` maxDD `-3.6376`
- `news_risk_high->crypto_major_1h` score `3.2148` n `63` status `ready` deltaP `14.3309` edge `0.2079` maxDD `-1.5096`
- `news_risk_high->index_4h` score `3.1184` n `62` status `ready` deltaP `33.6108` edge `0.062` maxDD `-0.4296`
- `market_context_high->fx_4h` score `3.065` n `50` status `ready` deltaP `34.4262` edge `0.0394` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `2.9581` n `50` status `ready` deltaP `13.2515` edge `0.2032` maxDD `-2.2692`
- `news_risk_high->metal_4h` score `2.3716` n `62` status `ready` deltaP `19.097` edge `0.1119` maxDD `-0.993`
- `news_risk_high->index_1h` score `1.9193` n `63` status `ready` deltaP `23.4959` edge `0.0183` maxDD `-0.1997`
- `news_risk_high->crypto_alt_1h` score `1.6084` n `63` status `ready` deltaP `5.9453` edge `0.1463` maxDD `-2.4854`
- `market_context_high->fx_1h` score `1.5585` n `50` status `ready` deltaP `21.6886` edge `0.0117` maxDD `-0.113`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
