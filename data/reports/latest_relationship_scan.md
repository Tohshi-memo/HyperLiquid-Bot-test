# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T08:52:31.302570+00:00`
- Price records: `672`
- Market context records: `5542`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11399`

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

- `market_context_high->equity_24h` score `4.2084` n `190` status `ready` deltaP `14.7442` edge `0.7603` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `2.1346` n `192` status `ready` deltaP `12.0046` edge `0.3271` maxDD `-14.0065`
- `market_context_high->crypto_major_24h` score `2.0136` n `190` status `ready` deltaP `16.2189` edge `0.5137` maxDD `-29.6555`
- `market_context_high->crypto_alt_4h` score `1.6325` n `192` status `ready` deltaP `7.6092` edge `0.2494` maxDD `-9.46`
- `market_context_high->equity_4h` score `1.4667` n `192` status `ready` deltaP `8.3079` edge `0.2307` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.5959` n `190` status `ready` deltaP `15.1882` edge `0.0433` maxDD `-1.2585`
- `market_context_high->equity_1h` score `0.1148` n `193` status `ready` deltaP `6.2688` edge `0.0643` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.0933` n `193` status `ready` deltaP `4.5996` edge `0.0109` maxDD `-0.9472`
- `market_context_high->fx_1h` score `-0.3326` n `193` status `ready` deltaP `0.8462` edge `0.0006` maxDD `-0.577`
- `market_context_high->crypto_alt_1h` score `-0.3603` n `193` status `ready` deltaP `0.7539` edge `0.0611` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.4444` n `193` status `ready` deltaP `2.7923` edge `0.0689` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.5931` n `193` status `ready` deltaP `1.2147` edge `0.01` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-0.7882` n `192` status `ready` deltaP `3.214` edge `0.0063` maxDD `-1.4726`
- `market_context_high->index_4h` score `-1.459` n `192` status `ready` deltaP `2.6168` edge `0.0219` maxDD `-2.874`
- `market_context_high->commodity_1h` score `-1.7874` n `193` status `ready` deltaP `-6.0392` edge `-0.0137` maxDD `-3.5988`
- `market_context_high->index_24h` score `-1.9943` n `190` status `ready` deltaP `12.5402` edge `0.0594` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-4.5264` n `192` status `ready` deltaP `-11.3313` edge `-0.0492` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.7857` n `192` status `ready` deltaP `-10.5945` edge `-0.062` maxDD `-13.9606`
- `market_context_high->crypto_alt_24h` score `-7.3178` n `190` status `ready` deltaP `7.2442` edge `0.2116` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.393` n `190` status `ready` deltaP `-4.2379` edge `-0.1818` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
