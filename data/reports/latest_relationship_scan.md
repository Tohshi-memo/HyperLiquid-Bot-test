# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T11:07:24.005567+00:00`
- Price records: `672`
- Market context records: `2036`
- Flow alert records: `7753`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9105`

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

- `market_context_high->crypto_major_4h` score `8.8787` n `205` status `ready` deltaP `30.7927` edge `0.5876` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `8.3802` n `205` status `ready` deltaP `24.5427` edge `0.6492` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `5.9101` n `205` status `ready` deltaP `18.9939` edge `0.4408` maxDD `-2.6599`
- `market_context_high->equity_4h` score `2.9831` n `205` status `ready` deltaP `17.2561` edge `0.243` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `1.5356` n `205` status `ready` deltaP `12.4777` edge `0.1434` maxDD `-3.2225`
- `market_context_high->index_4h` score `1.4486` n `205` status `ready` deltaP `12.9269` edge `0.1029` maxDD `-1.8022`
- `market_context_high->unknown_24h` score `1.3385` n `203` status `ready` deltaP `17.1576` edge `0.5292` maxDD `-35.8966`
- `market_context_high->crypto_alt_1h` score `1.2677` n `205` status `ready` deltaP `10.0825` edge `0.1498` maxDD `-4.9097`
- `market_context_high->equity_24h` score `0.547` n `203` status `ready` deltaP `16.2638` edge `0.427` maxDD `-33.1875`
- `market_context_high->index_24h` score `0.4242` n `203` status `ready` deltaP `4.6485` edge `0.1272` maxDD `-4.1604`
- `market_context_high->equity_1h` score `0.2104` n `205` status `ready` deltaP `6.9104` edge `0.0503` maxDD `-2.6402`
- `market_context_high->unknown_1h` score `0.0421` n `205` status `ready` deltaP `3.8959` edge `0.0495` maxDD `-3.0902`
- `market_context_high->index_1h` score `-0.281` n `205` status `ready` deltaP `2.7034` edge `0.0176` maxDD `-1.3898`
- `market_context_high->fx_24h` score `-0.5575` n `203` status `ready` deltaP `10.5353` edge `0.0216` maxDD `-2.7303`
- `market_context_high->metal_1h` score `-0.8299` n `205` status `ready` deltaP `4.1076` edge `0.0222` maxDD `-5.166`
- `market_context_high->fx_1h` score `-0.8398` n `205` status `ready` deltaP `-1.1421` edge `0.0004` maxDD `-0.3548`
- `market_context_high->metal_4h` score `-1.1002` n `205` status `ready` deltaP `9.1769` edge `0.1094` maxDD `-11.9812`
- `market_context_high->fx_4h` score `-1.5416` n `205` status `ready` deltaP `-5.8232` edge `-0.0015` maxDD `-1.0513`
- `market_context_high->metal_24h` score `-1.7984` n `203` status `ready` deltaP `9.7896` edge `0.1334` maxDD `-20.5491`
- `market_context_high->commodity_1h` score `-1.8761` n `205` status `ready` deltaP `2.3061` edge `-0.0001` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
