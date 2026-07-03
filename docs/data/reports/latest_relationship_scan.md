# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T05:22:26.453629+00:00`
- Price records: `672`
- Market context records: `5527`
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

- `market_context_high->equity_24h` score `3.8394` n `189` status `ready` deltaP `14.3023` edge `0.7325` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `2.6611` n `192` status `ready` deltaP `13.6814` edge `0.3598` maxDD `-14.0065`
- `market_context_high->crypto_major_24h` score `2.5929` n `189` status `ready` deltaP `16.0797` edge `0.5629` maxDD `-29.6555`
- `market_context_high->crypto_alt_4h` score `2.0089` n `192` status `ready` deltaP `9.1336` edge `0.2706` maxDD `-9.46`
- `market_context_high->equity_4h` score `1.8038` n `192` status `ready` deltaP `10.1372` edge `0.2466` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.437` n `189` status `ready` deltaP `13.3267` edge `0.0403` maxDD `-1.0847`
- `market_context_high->equity_1h` score `0.1848` n `192` status `ready` deltaP `7.0391` edge `0.065` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.0345` n `192` status `ready` deltaP `4.9744` edge `0.0133` maxDD `-0.9472`
- `market_context_high->crypto_alt_1h` score `-0.3177` n `192` status `ready` deltaP `1.4066` edge `0.0603` maxDD `-5.0257`
- `market_context_high->fx_1h` score `-0.3684` n `192` status `ready` deltaP `0.2932` edge `-0.0003` maxDD `-0.577`
- `market_context_high->crypto_major_1h` score `-0.4395` n `192` status `ready` deltaP `2.8381` edge `0.069` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.6839` n `192` status `ready` deltaP `0.5146` edge `0.0071` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-0.9157` n `192` status `ready` deltaP `1.9944` edge `0.0038` maxDD `-1.4726`
- `market_context_high->index_4h` score `-1.1682` n `192` status `ready` deltaP `4.751` edge `0.0319` maxDD `-2.874`
- `market_context_high->commodity_1h` score `-1.6814` n `192` status `ready` deltaP `-5.0586` edge `-0.0116` maxDD `-3.5831`
- `market_context_high->index_24h` score `-1.8282` n `189` status `ready` deltaP `14.294` edge `0.069` maxDD `-16.8946`
- `market_context_high->commodity_4h` score `-4.6755` n `192` status `ready` deltaP `-9.8323` edge `-0.0579` maxDD `-13.9606`
- `market_context_high->metal_4h` score `-4.6919` n `192` status `ready` deltaP `-12.246` edge `-0.0569` maxDD `-12.8631`
- `market_context_high->crypto_alt_24h` score `-7.1407` n `189` status `ready` deltaP `7.0437` edge `0.2277` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.3774` n `189` status `ready` deltaP `-4.5387` edge `-0.1778` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
