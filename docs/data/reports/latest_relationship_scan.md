# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T05:07:19.046329+00:00`
- Price records: `672`
- Market context records: `2110`
- Flow alert records: `7970`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9160`

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

- `market_context_high->crypto_alt_4h` score `11.6837` n `171` status `ready` deltaP `33.1408` edge `0.8505` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.0258` n `171` status `ready` deltaP `39.0913` edge `0.7112` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `5.9661` n `171` status `ready` deltaP `24.524` edge `0.4086` maxDD `-2.6599`
- `market_context_high->equity_4h` score `4.4098` n `171` status `ready` deltaP `23.0298` edge `0.3234` maxDD `-5.0894`
- `market_context_high->index_4h` score `2.6326` n `171` status `ready` deltaP `19.1913` edge `0.1598` maxDD `-1.8022`
- `market_context_high->index_24h` score `2.5532` n `170` status `ready` deltaP `12.0762` edge `0.2551` maxDD `-4.1604`
- `market_context_high->metal_4h` score `2.4401` n `171` status `ready` deltaP `18.1634` edge `0.2245` maxDD `-5.0463`
- `market_context_high->crypto_major_1h` score `2.3228` n `171` status `ready` deltaP `15.8525` edge `0.1865` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `2.163` n `171` status `ready` deltaP `12.5731` edge `0.2078` maxDD `-4.9097`
- `market_context_high->unknown_24h` score `1.9882` n `170` status `ready` deltaP `23.5986` edge `0.5404` maxDD `-35.8966`
- `market_context_high->equity_24h` score `1.8056` n `170` status `ready` deltaP `23.3564` edge `0.4846` maxDD `-33.1875`
- `market_context_high->equity_1h` score `0.8695` n `171` status `ready` deltaP `10.529` edge `0.0811` maxDD `-2.6402`
- `market_context_high->crypto_major_24h` score `0.6564` n `170` status `ready` deltaP `21.0727` edge `0.7728` maxDD `-62.3533`
- `market_context_high->metal_1h` score `0.3625` n `171` status `ready` deltaP `7.7871` edge `0.05` maxDD `-2.7367`
- `market_context_high->index_1h` score `0.1469` n `171` status `ready` deltaP `5.7569` edge `0.0329` maxDD `-1.3898`
- `market_context_high->fx_24h` score `-0.0754` n `170` status `ready` deltaP `14.8097` edge `0.0309` maxDD `-2.811`
- `market_context_high->unknown_1h` score `-0.198` n `171` status `ready` deltaP `4.344` edge `0.0265` maxDD `-3.0902`
- `market_context_high->metal_24h` score `-0.3297` n `170` status `ready` deltaP `11.211` edge `0.2879` maxDD `-23.2095`
- `market_context_high->fx_1h` score `-0.5727` n `171` status `ready` deltaP `-1.7474` edge `0.001` maxDD `-0.3548`
- `market_context_high->fx_4h` score `-1.1083` n `171` status `ready` deltaP `-7.6122` edge `-0.0032` maxDD `-1.0513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
