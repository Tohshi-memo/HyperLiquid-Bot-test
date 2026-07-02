# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T20:22:30.748901+00:00`
- Price records: `672`
- Market context records: `5490`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11467`

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

- `market_context_high->crypto_major_24h` score `3.318` n `190` status `ready` deltaP `16.2189` edge `0.6224` maxDD `-29.6555`
- `market_context_high->equity_4h` score `3.0177` n `193` status `ready` deltaP `13.8214` edge `0.3232` maxDD `-7.4425`
- `market_context_high->crypto_major_4h` score `2.6155` n `193` status `ready` deltaP `14.3411` edge `0.3516` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `2.2797` n `193` status `ready` deltaP `11.0182` edge `0.2806` maxDD `-9.46`
- `market_context_high->equity_24h` score `1.8981` n `190` status `ready` deltaP `10.7511` edge `0.5944` maxDD `-31.6316`
- `market_context_high->equity_1h` score `0.6238` n `193` status `ready` deltaP `9.3319` edge `0.0863` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.235` n `193` status `ready` deltaP `7.5936` edge `0.0183` maxDD `-0.9472`
- `market_context_high->fx_24h` score `0.2343` n `190` status `ready` deltaP `11.5424` edge `0.0353` maxDD `-1.0847`
- `market_context_high->crypto_alt_1h` score `-0.312` n `193` status `ready` deltaP `1.2837` edge `0.0616` maxDD `-5.0257`
- `market_context_high->fx_1h` score `-0.3463` n `193` status `ready` deltaP `0.6275` edge `0.0003` maxDD `-0.577`
- `market_context_high->metal_1h` score `-0.4421` n `193` status `ready` deltaP `2.562` edge `0.0136` maxDD `-2.0682`
- `market_context_high->crypto_major_1h` score `-0.4907` n `193` status `ready` deltaP `2.5736` edge `0.0665` maxDD `-6.9639`
- `market_context_high->index_4h` score `-0.624` n `193` status `ready` deltaP `8.7333` edge `0.0507` maxDD `-2.874`
- `market_context_high->fx_4h` score `-0.8188` n `193` status `ready` deltaP `3.5187` edge `0.0064` maxDD `-1.5143`
- `market_context_high->commodity_1h` score `-1.5602` n `193` status `ready` deltaP `-3.8744` edge `-0.0094` maxDD `-3.5831`
- `market_context_high->index_24h` score `-1.7592` n `190` status `ready` deltaP `14.2708` edge `0.078` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.7001` n `193` status `ready` deltaP `-8.7316` edge `-0.0355` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.3888` n `193` status `ready` deltaP `-7.2665` edge `-0.05` maxDD `-14.0497`
- `market_context_high->crypto_alt_24h` score `-7.1522` n `190` status `ready` deltaP `7.2442` edge `0.2254` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.2276` n `190` status `ready` deltaP `-4.2379` edge `-0.1606` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
