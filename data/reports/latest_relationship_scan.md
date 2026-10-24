# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-24T22:37:29.706889+00:00`
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

- `market_context_high->unknown_4h` score `20.5847` n `99` status `ready` deltaP `0.6637` edge `1.7445` maxDD `-1.016`
- `market_context_high->commodity_24h` score `1.8304` n `64` status `ready` deltaP `24.3056` edge `0.0814` maxDD `-3.6055`
- `market_context_high->commodity_4h` score `1.0427` n `99` status `ready` deltaP `13.4285` edge `0.0536` maxDD `-1.165`
- `market_context_high->commodity_1h` score `0.2549` n `107` status `ready` deltaP `8.6113` edge `0.0139` maxDD `-1.0053`
- `market_context_high->fx_1h` score `-0.3819` n `107` status `ready` deltaP `0.1721` edge `0.0025` maxDD `-0.1712`
- `market_context_high->fx_4h` score `-0.4623` n `99` status `ready` deltaP `-0.6206` edge `0.0055` maxDD `-0.5168`
- `market_context_high->index_1h` score `-1.0876` n `107` status `ready` deltaP `-2.7814` edge `-0.0069` maxDD `-1.2155`
- `market_context_high->metal_1h` score `-1.1852` n `107` status `ready` deltaP `-1.9559` edge `-0.0063` maxDD `-1.6873`
- `market_context_high->fx_24h` score `-2.4504` n `64` status `ready` deltaP `-8.3333` edge `-0.0038` maxDD `-1.9207`
- `market_context_high->crypto_major_1h` score `-3.2551` n `107` status `ready` deltaP `-4.8044` edge `-0.0593` maxDD `-11.0607`
- `market_context_high->metal_4h` score `-3.5981` n `99` status `ready` deltaP `-12.229` edge `-0.031` maxDD `-5.985`
- `market_context_high->metal_24h` score `-3.9327` n `64` status `ready` deltaP `-13.0208` edge `0.0174` maxDD `-7.6654`
- `market_context_high->equity_1h` score `-4.1195` n `107` status `ready` deltaP `-1.9195` edge `-0.0976` maxDD `-12.6316`
- `market_context_high->crypto_alt_1h` score `-4.203` n `107` status `ready` deltaP `-5.7712` edge `-0.0801` maxDD `-15.2008`
- `market_context_high->crypto_major_24h` score `-4.444` n `64` status `ready` deltaP `-7.4653` edge `-0.1664` maxDD `-22.2862`
- `market_context_high->index_4h` score `-5.1399` n `99` status `ready` deltaP `-26.3304` edge `-0.0525` maxDD `-5.3565`
- `market_context_high->index_24h` score `-8.1827` n `64` status `ready` deltaP `-37.8472` edge `-0.17` maxDD `-7.4328`
- `market_context_high->crypto_alt_24h` score `-12.5801` n `64` status `ready` deltaP `-4.5139` edge `-0.5473` maxDD `-72.5023`
- `market_context_high->crypto_major_4h` score `-15.4946` n `99` status `ready` deltaP `-28.1982` edge `-0.3863` maxDD `-47.3545`
- `market_context_high->equity_4h` score `-17.3942` n `99` status `ready` deltaP `-25.5682` edge `-0.4837` maxDD `-51.2958`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
