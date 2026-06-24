# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T07:52:27.427458+00:00`
- Price records: `672`
- Market context records: `4601`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9849`

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

- `market_context_high->unknown_1h` score `68.5318` n `148` status `ready` deltaP `6.4776` edge `5.7137` maxDD `-2.0052`
- `market_context_high->unknown_4h` score `4.1729` n `148` status `ready` deltaP `8.8332` edge `0.4099` maxDD `-4.6834`
- `market_context_high->commodity_1h` score `-0.5446` n `148` status `ready` deltaP `1.412` edge `0.0248` maxDD `-2.0345`
- `market_context_high->fx_1h` score `-0.5586` n `148` status `ready` deltaP `-1.8086` edge `-0.0041` maxDD `-1.1038`
- `market_context_high->fx_4h` score `-0.7312` n `148` status `ready` deltaP `2.2206` edge `-0.0003` maxDD `-1.9927`
- `market_context_high->index_4h` score `-0.9185` n `148` status `ready` deltaP `1.2031` edge `-0.0135` maxDD `-5.9823`
- `market_context_high->equity_1h` score `-0.9327` n `148` status `ready` deltaP `-2.9212` edge `-0.0014` maxDD `-5.5624`
- `market_context_high->commodity_4h` score `-1.203` n `148` status `ready` deltaP `3.3496` edge `0.0342` maxDD `-9.1941`
- `market_context_high->index_1h` score `-1.7164` n `148` status `ready` deltaP `-4.3454` edge `-0.0132` maxDD `-2.7358`
- `market_context_high->equity_4h` score `-1.7248` n `148` status `ready` deltaP `-0.9764` edge `-0.0377` maxDD `-8.8203`
- `market_context_high->unknown_24h` score `-2.485` n `146` status `ready` deltaP `2.3782` edge `-0.1306` maxDD `-4.7201`
- `market_context_high->metal_1h` score `-3.004` n `148` status `ready` deltaP `-4.661` edge `-0.0889` maxDD `-17.8795`
- `market_context_high->commodity_24h` score `-4.6436` n `146` status `ready` deltaP `11.2847` edge `0.0627` maxDD `-29.3255`
- `market_context_high->fx_24h` score `-5.3864` n `146` status `ready` deltaP `-13.0256` edge `-0.0108` maxDD `-6.0982`
- `market_context_high->crypto_alt_1h` score `-5.5212` n `148` status `ready` deltaP `-2.0958` edge `-0.1174` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.8112` n `148` status `ready` deltaP `-6.077` edge `-0.1518` maxDD `-27.356`
- `market_context_high->index_24h` score `-8.4388` n `146` status `ready` deltaP `-7.9576` edge `-0.1127` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-9.159` n `148` status `ready` deltaP `-3.572` edge `-0.2847` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-10.3392` n `148` status `ready` deltaP `-6.8474` edge `-0.3585` maxDD `-67.3775`
- `market_context_high->crypto_major_4h` score `-12.3104` n `148` status `ready` deltaP `-5.5785` edge `-0.4467` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
