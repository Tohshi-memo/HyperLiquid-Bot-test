# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-24T22:52:26.052411+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7158`

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

- `market_context_high->unknown_4h` score `20.7505` n `99` status `ready` deltaP `1.5213` edge `1.7526` maxDD `-1.016`
- `market_context_high->commodity_24h` score `1.8129` n `63` status `ready` deltaP `24.132` edge `0.0811` maxDD `-3.6055`
- `market_context_high->commodity_4h` score `0.9693` n `99` status `ready` deltaP `12.5709` edge `0.0532` maxDD `-1.165`
- `market_context_high->commodity_1h` score `0.1837` n `107` status `ready` deltaP `7.8264` edge `0.0132` maxDD `-1.0053`
- `market_context_high->fx_1h` score `-0.3819` n `107` status `ready` deltaP `0.1721` edge `0.0025` maxDD `-0.1712`
- `market_context_high->fx_4h` score `-0.4638` n `99` status `ready` deltaP `-0.6206` edge `0.0053` maxDD `-0.5168`
- `market_context_high->index_1h` score `-1.0876` n `107` status `ready` deltaP `-2.7814` edge `-0.0069` maxDD `-1.2155`
- `market_context_high->metal_1h` score `-1.12` n `107` status `ready` deltaP `-1.171` edge `-0.0061` maxDD `-1.6873`
- `market_context_high->fx_24h` score `-2.3619` n `63` status `ready` deltaP `-7.9861` edge `-0.0035` maxDD `-1.8734`
- `market_context_high->crypto_major_1h` score `-3.1261` n `107` status `ready` deltaP `-4.0195` edge `-0.0557` maxDD `-10.9075`
- `market_context_high->metal_4h` score `-3.5957` n `99` status `ready` deltaP `-12.229` edge `-0.0308` maxDD `-5.985`
- `market_context_high->metal_24h` score `-3.8675` n `63` status `ready` deltaP `-12.8224` edge `0.0165` maxDD `-7.5978`
- `market_context_high->equity_1h` score `-4.0471` n `107` status `ready` deltaP `-1.1347` edge `-0.0968` maxDD `-12.6316`
- `market_context_high->crypto_alt_1h` score `-4.0768` n `107` status `ready` deltaP `-4.9863` edge `-0.0771` maxDD `-15.0178`
- `market_context_high->crypto_major_24h` score `-4.1437` n `63` status `ready` deltaP `-6.7461` edge `-0.1507` maxDD `-21.1792`
- `market_context_high->index_4h` score `-5.1399` n `99` status `ready` deltaP `-26.3304` edge `-0.0525` maxDD `-5.3565`
- `market_context_high->index_24h` score `-8.1231` n `63` status `ready` deltaP `-37.8472` edge `-0.1704` maxDD `-7.3365`
- `market_context_high->crypto_alt_24h` score `-12.0025` n `63` status `ready` deltaP `-3.8195` edge `-0.5171` maxDD `-69.6972`
- `market_context_high->crypto_major_4h` score `-15.2407` n `99` status `ready` deltaP `-27.3405` edge `-0.3792` maxDD `-47.0206`
- `market_context_high->equity_4h` score `-17.3786` n `99` status `ready` deltaP `-25.5682` edge `-0.4824` maxDD `-51.2958`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
