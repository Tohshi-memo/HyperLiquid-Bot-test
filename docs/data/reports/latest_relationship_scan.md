# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-14T04:52:24.565267+00:00`
- Price records: `672`
- Market context records: `6676`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11784`

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

- `market_context_high->unknown_1h` score `2.6857` n `202` status `ready` deltaP `-4.2138` edge `0.342` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `1.1926` n `202` status `ready` deltaP `12.2852` edge `0.2043` maxDD `-5.2791`
- `market_context_high->unknown_4h` score `0.9365` n `202` status `ready` deltaP `-13.4388` edge `0.4082` maxDD `-10.5788`
- `market_context_high->crypto_major_1h` score `0.0195` n `202` status `ready` deltaP `7.7133` edge `0.0454` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.1727` n `202` status `ready` deltaP `5.284` edge `0.0393` maxDD `-3.7803`
- `market_context_high->unknown_24h` score `-0.2266` n `202` status `ready` deltaP `-3.9346` edge `0.3724` maxDD `-12.3511`
- `market_context_high->fx_1h` score `-0.2489` n `202` status `ready` deltaP `2.6724` edge `0.001` maxDD `-0.7249`
- `market_context_high->index_1h` score `-0.5172` n `202` status `ready` deltaP `0.2653` edge `0.0037` maxDD `-0.7417`
- `market_context_high->commodity_1h` score `-0.6463` n `202` status `ready` deltaP `-0.7722` edge `-0.0094` maxDD `-2.1314`
- `market_context_high->index_4h` score `-0.8729` n `202` status `ready` deltaP `10.4338` edge `0.0065` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-0.9407` n `202` status `ready` deltaP `3.0162` edge `0.0042` maxDD `-3.8827`
- `market_context_high->metal_1h` score `-1.2655` n `202` status `ready` deltaP `-4.5355` edge `-0.0011` maxDD `-1.5966`
- `market_context_high->crypto_major_4h` score `-1.3837` n `202` status `ready` deltaP `9.2928` edge `0.0921` maxDD `-16.8495`
- `market_context_high->fx_4h` score `-1.3995` n `202` status `ready` deltaP `6.253` edge `0.0001` maxDD `-3.3635`
- `market_context_high->commodity_4h` score `-1.4873` n `202` status `ready` deltaP `-1.6814` edge `-0.03` maxDD `-5.6246`
- `market_context_high->crypto_alt_4h` score `-1.6751` n `202` status `ready` deltaP `6.588` edge `0.0815` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.1187` n `202` status `ready` deltaP `-1.212` edge `0.0225` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-4.8218` n `202` status `ready` deltaP `7.6944` edge `-0.0262` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-6.423` n `202` status `ready` deltaP `-12.3367` edge `-0.0131` maxDD `-10.8591`
- `market_context_high->metal_24h` score `-6.9475` n `202` status `ready` deltaP `-5.7137` edge `-0.0041` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
