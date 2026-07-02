# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T13:52:35.855268+00:00`
- Price records: `672`
- Market context records: `5460`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11444`

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

- `market_context_high->crypto_major_24h` score `3.884` n `196` status `ready` deltaP `17.0245` edge `0.6642` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `2.4935` n `199` status `ready` deltaP `14.7506` edge `0.3387` maxDD `-14.0065`
- `market_context_high->equity_4h` score `2.0285` n `199` status `ready` deltaP `11.8205` edge `0.2541` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `1.8905` n `199` status `ready` deltaP `9.8442` edge `0.256` maxDD `-9.46`
- `market_context_high->equity_1h` score `0.2124` n `199` status `ready` deltaP `7.564` edge `0.0638` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.0767` n `199` status `ready` deltaP `6.1851` edge `0.0145` maxDD `-0.9472`
- `market_context_high->fx_24h` score `0.0185` n `196` status `ready` deltaP `9.5805` edge `0.0304` maxDD `-1.0847`
- `market_context_high->equity_24h` score `-0.064` n `196` status `ready` deltaP `8.064` edge `0.4488` maxDD `-31.6316`
- `market_context_high->metal_1h` score `-0.3408` n `199` status `ready` deltaP `3.5123` edge `0.0157` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.5429` n `199` status `ready` deltaP `0.5612` edge `-0.0001` maxDD `-0.577`
- `market_context_high->crypto_alt_1h` score `-0.5948` n `199` status `ready` deltaP `0.2084` edge `0.0452` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.7722` n `199` status `ready` deltaP `1.3954` edge `0.0509` maxDD `-6.9639`
- `market_context_high->index_4h` score `-0.9153` n `199` status `ready` deltaP `6.8629` edge `0.0389` maxDD `-2.874`
- `market_context_high->fx_4h` score `-1.019` n `199` status `ready` deltaP `1.9342` edge `0.0047` maxDD `-1.5345`
- `market_context_high->commodity_1h` score `-1.3732` n `199` status `ready` deltaP `-2.1221` edge `-0.0055` maxDD `-3.5831`
- `market_context_high->index_24h` score `-2.0142` n `196` status `ready` deltaP `12.1279` edge `0.0596` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.5642` n `199` status `ready` deltaP `-7.5124` edge `-0.0262` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.1356` n `199` status `ready` deltaP `-5.1132` edge `-0.0391` maxDD `-14.3822`
- `market_context_high->crypto_alt_24h` score `-6.9154` n `196` status `ready` deltaP `8.4042` edge `0.2374` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-6.9562` n `196` status `ready` deltaP `-2.4978` edge `-0.1374` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
