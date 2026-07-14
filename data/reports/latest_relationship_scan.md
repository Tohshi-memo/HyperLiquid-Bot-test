# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-14T05:07:25.531438+00:00`
- Price records: `672`
- Market context records: `6677`
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
- `market_context_high->unknown_4h` score `1.2547` n `202` status `ready` deltaP `-13.2863` edge `0.4337` maxDD `-10.5788`
- `market_context_high->commodity_24h` score `1.189` n `202` status `ready` deltaP `12.2852` edge `0.204` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `0.0039` n `202` status `ready` deltaP `7.5636` edge `0.0444` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.1919` n `202` status `ready` deltaP `5.1343` edge `0.0387` maxDD `-3.7803`
- `market_context_high->unknown_24h` score `-0.2251` n `202` status `ready` deltaP `-3.9346` edge `0.3726` maxDD `-12.3511`
- `market_context_high->fx_1h` score `-0.2567` n `202` status `ready` deltaP `2.5227` edge `0.001` maxDD `-0.7249`
- `market_context_high->index_1h` score `-0.5273` n `202` status `ready` deltaP `0.1156` edge `0.0034` maxDD `-0.7417`
- `market_context_high->commodity_1h` score `-0.6369` n `202` status `ready` deltaP `-0.6225` edge `-0.0092` maxDD `-2.1314`
- `market_context_high->index_4h` score `-0.8753` n `202` status `ready` deltaP `10.4338` edge `0.0062` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-0.9515` n `202` status `ready` deltaP `3.0162` edge `0.0033` maxDD `-3.8827`
- `market_context_high->metal_1h` score `-1.2631` n `202` status `ready` deltaP `-4.5355` edge `-0.0009` maxDD `-1.5966`
- `market_context_high->fx_4h` score `-1.4003` n `202` status `ready` deltaP `6.253` edge `0.0` maxDD `-3.3635`
- `market_context_high->crypto_major_4h` score `-1.4143` n `202` status `ready` deltaP `9.1403` edge `0.0892` maxDD `-16.8495`
- `market_context_high->commodity_4h` score `-1.4866` n `202` status `ready` deltaP `-1.6814` edge `-0.0299` maxDD `-5.6246`
- `market_context_high->crypto_alt_4h` score `-1.6907` n `202` status `ready` deltaP `6.588` edge `0.0795` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.1321` n `202` status `ready` deltaP `-1.3644` edge `0.0218` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-4.835` n `202` status `ready` deltaP `7.6944` edge `-0.0273` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-6.423` n `202` status `ready` deltaP `-12.3367` edge `-0.0131` maxDD `-10.8591`
- `market_context_high->metal_24h` score `-6.9612` n `202` status `ready` deltaP `-5.8873` edge `-0.0047` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
