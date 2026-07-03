# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T05:07:31.342423+00:00`
- Price records: `672`
- Market context records: `5526`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11432`

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

- `market_context_high->equity_24h` score `3.7728` n `189` status `ready` deltaP `14.1287` edge `0.7281` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `2.6431` n `192` status `ready` deltaP `13.6814` edge `0.3583` maxDD `-14.0065`
- `market_context_high->crypto_major_24h` score `2.6037` n `189` status `ready` deltaP `16.0797` edge `0.5638` maxDD `-29.6555`
- `market_context_high->crypto_alt_4h` score `1.9751` n `192` status `ready` deltaP `8.9812` edge `0.2688` maxDD `-9.46`
- `market_context_high->equity_4h` score `1.8146` n `192` status `ready` deltaP `10.1372` edge `0.2475` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.437` n `189` status `ready` deltaP `13.3267` edge `0.0403` maxDD `-1.0847`
- `market_context_high->equity_1h` score `0.1824` n `192` status `ready` deltaP `7.0391` edge `0.0648` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.0345` n `192` status `ready` deltaP `4.9744` edge `0.0133` maxDD `-0.9472`
- `market_context_high->crypto_alt_1h` score `-0.3393` n `192` status `ready` deltaP `1.2569` edge `0.0595` maxDD `-5.0257`
- `market_context_high->fx_1h` score `-0.359` n `192` status `ready` deltaP `0.4429` edge `-0.0001` maxDD `-0.577`
- `market_context_high->crypto_major_1h` score `-0.4479` n `192` status `ready` deltaP `2.8381` edge `0.0683` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.703` n `192` status `ready` deltaP `0.3649` edge `0.0065` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-0.9011` n `192` status `ready` deltaP `2.1469` edge `0.004` maxDD `-1.4726`
- `market_context_high->index_4h` score `-1.1464` n `192` status `ready` deltaP `4.9034` edge `0.0327` maxDD `-2.874`
- `market_context_high->commodity_1h` score `-1.6838` n `192` status `ready` deltaP `-5.0586` edge `-0.0118` maxDD `-3.5831`
- `market_context_high->index_24h` score `-1.8259` n `189` status `ready` deltaP `14.294` edge `0.0693` maxDD `-16.8946`
- `market_context_high->commodity_4h` score `-4.6561` n `192` status `ready` deltaP `-9.6799` edge `-0.0573` maxDD `-13.9606`
- `market_context_high->metal_4h` score `-4.7185` n `192` status `ready` deltaP `-12.3984` edge `-0.0581` maxDD `-12.8631`
- `market_context_high->crypto_alt_24h` score `-7.1575` n `189` status `ready` deltaP `7.0437` edge `0.2263` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.3774` n `189` status `ready` deltaP `-4.5387` edge `-0.1778` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
