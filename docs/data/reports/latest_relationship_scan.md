# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T23:07:25.071901+00:00`
- Price records: `672`
- Market context records: `5713`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8874`

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

- `market_context_high->crypto_major_4h` score `1.7128` n `269` status `ready` deltaP `10.8543` edge `0.2075` maxDD `-6.6368`
- `market_context_high->equity_24h` score `1.0122` n `219` status `ready` deltaP `17.0496` edge `0.524` maxDD `-31.6316`
- `market_context_high->crypto_alt_4h` score `0.5832` n `269` status `ready` deltaP `8.2816` edge `0.1543` maxDD `-7.5392`
- `market_context_high->equity_4h` score `0.1686` n `269` status `ready` deltaP `6.8428` edge `0.1323` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2071` n `281` status `ready` deltaP `3.0814` edge `0.001` maxDD `-0.5144`
- `market_context_high->crypto_major_1h` score `-0.4095` n `281` status `ready` deltaP `3.5502` edge `0.0378` maxDD `-3.9811`
- `market_context_high->metal_1h` score `-0.4482` n `281` status `ready` deltaP `1.5844` edge `-0.0005` maxDD `-2.0682`
- `market_context_high->equity_1h` score `-0.5594` n `281` status `ready` deltaP `3.9114` edge `0.028` maxDD `-5.0555`
- `market_context_high->crypto_alt_1h` score `-0.5818` n `281` status `ready` deltaP `1.8103` edge `0.0338` maxDD `-3.8812`
- `market_context_high->index_1h` score `-0.6095` n `281` status `ready` deltaP `0.6297` edge `0.0045` maxDD `-0.9472`
- `market_context_high->commodity_1h` score `-1.0807` n `281` status `ready` deltaP `-0.8162` edge `-0.0039` maxDD `-3.7906`
- `market_context_high->fx_24h` score `-1.1482` n `219` status `ready` deltaP `10.4856` edge `0.0409` maxDD `-3.6407`
- `market_context_high->index_4h` score `-1.2125` n `269` status `ready` deltaP `0.3117` edge `0.0112` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.3097` n `269` status `ready` deltaP `1.6729` edge `0.0053` maxDD `-1.4156`
- `market_context_high->metal_4h` score `-2.6111` n `269` status `ready` deltaP `-7.1233` edge `-0.0497` maxDD `-11.6719`
- `market_context_high->index_24h` score `-2.8503` n `219` status `ready` deltaP `2.6018` edge `0.0317` maxDD `-18.1572`
- `market_context_high->commodity_4h` score `-3.855` n `269` status `ready` deltaP `-3.794` edge `-0.0284` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.6101` n `219` status `ready` deltaP `5.9574` edge `0.0218` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.8579` n `219` status `ready` deltaP `-6.7161` edge `-0.2401` maxDD `-32.4704`
- `market_context_high->commodity_24h` score `-11.9369` n `219` status `ready` deltaP `-10.3715` edge `-0.07` maxDD `-45.7814`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
