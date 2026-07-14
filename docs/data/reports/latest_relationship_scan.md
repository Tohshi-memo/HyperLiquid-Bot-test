# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-14T05:37:24.350744+00:00`
- Price records: `672`
- Market context records: `6679`
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

- `market_context_high->unknown_1h` score `2.7025` n `202` status `ready` deltaP `-4.2138` edge `0.3434` maxDD `-3.2083`
- `market_context_high->unknown_4h` score `1.9367` n `202` status `ready` deltaP `-12.9814` edge `0.4885` maxDD `-10.5788`
- `market_context_high->commodity_24h` score `1.1854` n `202` status `ready` deltaP `12.2852` edge `0.2037` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.0335` n `202` status `ready` deltaP `7.2642` edge `0.0416` maxDD `-4.2122`
- `market_context_high->unknown_24h` score `-0.2282` n `202` status `ready` deltaP `-3.9346` edge `0.3722` maxDD `-12.3511`
- `market_context_high->crypto_alt_1h` score `-0.2423` n `202` status `ready` deltaP `4.8349` edge `0.0365` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.2738` n `202` status `ready` deltaP `2.2233` edge `0.0008` maxDD `-0.7249`
- `market_context_high->index_1h` score `-0.5499` n `202` status `ready` deltaP `-0.1838` edge `0.0025` maxDD `-0.7417`
- `market_context_high->commodity_1h` score `-0.6346` n `202` status `ready` deltaP `-0.6225` edge `-0.0089` maxDD `-2.1314`
- `market_context_high->index_4h` score `-0.8974` n `202` status `ready` deltaP `10.1289` edge `0.0054` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-1.0019` n `202` status `ready` deltaP `2.8665` edge `0.0001` maxDD `-3.8827`
- `market_context_high->metal_1h` score `-1.2799` n `202` status `ready` deltaP `-4.6852` edge `-0.0013` maxDD `-1.5966`
- `market_context_high->fx_4h` score `-1.4177` n `202` status `ready` deltaP `5.9481` edge `-0.0002` maxDD `-3.3635`
- `market_context_high->crypto_major_4h` score `-1.4621` n `202` status `ready` deltaP `8.8354` edge `0.0851` maxDD `-16.8495`
- `market_context_high->commodity_4h` score `-1.4778` n `202` status `ready` deltaP `-1.5289` edge `-0.0298` maxDD `-5.6246`
- `market_context_high->crypto_alt_4h` score `-1.7284` n `202` status `ready` deltaP `6.2832` edge `0.0767` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.1651` n `202` status `ready` deltaP `-1.6693` edge `0.0196` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-4.8918` n `202` status `ready` deltaP `7.3895` edge `-0.03` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-6.4254` n `202` status `ready` deltaP `-12.3367` edge `-0.0133` maxDD `-10.8591`
- `market_context_high->metal_24h` score `-6.9957` n `202` status `ready` deltaP `-6.2345` edge `-0.0068` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
