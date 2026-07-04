# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T00:07:33.369782+00:00`
- Price records: `672`
- Market context records: `5609`
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

- `market_context_high->equity_24h` score `3.3319` n `174` status `ready` deltaP `15.0084` edge `0.6855` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `1.482` n `221` status `ready` deltaP `13.7767` edge `0.2609` maxDD `-14.0065`
- `market_context_high->fx_24h` score `1.2528` n `174` status `ready` deltaP `21.6116` edge `0.0577` maxDD `-1.457`
- `market_context_high->crypto_alt_4h` score `0.8695` n `221` status `ready` deltaP `9.0657` edge `0.1761` maxDD `-9.46`
- `market_context_high->equity_4h` score `0.4337` n `221` status `ready` deltaP `6.0459` edge `0.1597` maxDD `-7.4425`
- `market_context_high->equity_1h` score `-0.3424` n `233` status `ready` deltaP `5.8146` edge `0.0334` maxDD `-5.0555`
- `market_context_high->fx_1h` score `-0.3483` n `233` status `ready` deltaP `0.3245` edge `0.0008` maxDD `-0.4764`
- `market_context_high->metal_1h` score `-0.5098` n `233` status `ready` deltaP `0.2345` edge `0.0006` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.6164` n `233` status `ready` deltaP `1.0633` edge `0.0377` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.6344` n `233` status `ready` deltaP `4.0773` edge `0.0445` maxDD `-6.9639`
- `market_context_high->index_1h` score `-0.8902` n `233` status `ready` deltaP `1.0132` edge `0.0059` maxDD `-0.9472`
- `market_context_high->commodity_1h` score `-1.1723` n `233` status `ready` deltaP `-2.2108` edge `-0.0064` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.2786` n `221` status `ready` deltaP `0.9449` edge `0.0072` maxDD `-1.1943`
- `market_context_high->crypto_major_24h` score `-1.5973` n `174` status `ready` deltaP `9.6325` edge `0.2567` maxDD `-29.6555`
- `market_context_high->index_4h` score `-1.6497` n `221` status `ready` deltaP `1.7023` edge `0.0121` maxDD `-2.874`
- `market_context_high->index_24h` score `-2.3863` n `174` status `ready` deltaP `10.0874` edge `0.0255` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.8375` n `221` status `ready` deltaP `-10.6093` edge `-0.0547` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-4.2087` n `221` status `ready` deltaP `-6.041` edge `-0.0429` maxDD `-14.071`
- `market_context_high->metal_24h` score `-8.2301` n `174` status `ready` deltaP `-10.2371` edge `-0.2508` maxDD `-32.8874`
- `market_context_high->crypto_alt_24h` score `-11.6026` n `174` status `ready` deltaP `-0.5807` edge `-0.0933` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
