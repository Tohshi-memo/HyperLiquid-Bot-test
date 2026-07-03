# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T01:52:26.493755+00:00`
- Price records: `672`
- Market context records: `5513`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11468`

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

- `market_context_high->equity_24h` score `2.8666` n `190` status `ready` deltaP `11.9664` edge `0.667` maxDD `-31.6316`
- `market_context_high->crypto_major_24h` score `2.6544` n `190` status `ready` deltaP `16.2189` edge `0.5671` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `2.3689` n `193` status `ready` deltaP `13.8838` edge `0.3341` maxDD `-14.0065`
- `market_context_high->equity_4h` score `2.0056` n `193` status `ready` deltaP `10.6202` edge `0.2602` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `1.8227` n `193` status `ready` deltaP `9.3414` edge `0.2537` maxDD `-9.46`
- `market_context_high->fx_24h` score `0.3898` n `190` status `ready` deltaP `12.9312` edge `0.039` maxDD `-1.0847`
- `market_context_high->equity_1h` score `0.324` n `193` status `ready` deltaP `7.9846` edge `0.0703` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.0625` n `193` status `ready` deltaP `5.9469` edge `0.0149` maxDD `-0.9472`
- `market_context_high->fx_1h` score `-0.3471` n `193` status `ready` deltaP `0.6275` edge `0.0002` maxDD `-0.577`
- `market_context_high->crypto_alt_1h` score `-0.4966` n `193` status `ready` deltaP `0.5352` edge `0.0512` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.6226` n `193` status `ready` deltaP `2.1245` edge `0.0585` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.6949` n `193` status `ready` deltaP `0.4662` edge `0.0065` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-0.8516` n `193` status `ready` deltaP `3.2138` edge `0.0057` maxDD `-1.5143`
- `market_context_high->index_4h` score `-1.0517` n `193` status `ready` deltaP `5.5321` edge `0.0364` maxDD `-2.874`
- `market_context_high->commodity_1h` score `-1.5423` n `193` status `ready` deltaP `-3.575` edge `-0.0099` maxDD `-3.5831`
- `market_context_high->index_24h` score `-1.8302` n `190` status `ready` deltaP `14.2708` edge `0.0689` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-3.0132` n `193` status `ready` deltaP `-11.9329` edge `-0.0543` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.5685` n `193` status `ready` deltaP `-8.9433` edge `-0.0538` maxDD `-14.0497`
- `market_context_high->metal_24h` score `-7.3173` n `190` status `ready` deltaP `-4.2379` edge `-0.1721` maxDD `-33.021`
- `market_context_high->crypto_alt_24h` score `-7.3418` n `190` status `ready` deltaP `7.2442` edge `0.2096` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
