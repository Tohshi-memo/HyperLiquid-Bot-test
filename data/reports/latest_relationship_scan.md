# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-22T20:37:42.316956+00:00`
- Price records: `672`
- Market context records: `7599`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14551`

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

- `market_context_high->equity_24h` score `1.1445` n `143` status `ready` deltaP `18.0381` edge `0.5645` maxDD `-38.3748`
- `market_context_high->unknown_24h` score `0.6369` n `144` status `ready` deltaP `13.1944` edge `0.1211` maxDD `-5.1929`
- `market_context_high->commodity_24h` score `0.5247` n `143` status `ready` deltaP `16.3154` edge `0.0933` maxDD `-7.0012`
- `market_context_high->index_1h` score `0.0855` n `147` status `ready` deltaP `7.0448` edge `0.0119` maxDD `-0.8324`
- `market_context_high->commodity_4h` score `-0.1012` n `147` status `ready` deltaP `7.2708` edge `0.0191` maxDD `-2.4139`
- `market_context_high->crypto_major_1h` score `-0.154` n `147` status `ready` deltaP `7.9046` edge `0.0236` maxDD `-4.0162`
- `market_context_high->commodity_1h` score `-0.2006` n `147` status `ready` deltaP `4.5903` edge `0.0009` maxDD `-1.5775`
- `market_context_high->crypto_alt_1h` score `-0.23` n `147` status `ready` deltaP `2.0001` edge `0.0204` maxDD `-2.7243`
- `market_context_high->fx_24h` score `-0.2622` n `143` status `ready` deltaP `9.9169` edge `0.0208` maxDD `-3.0343`
- `market_context_high->equity_1h` score `-0.4447` n `147` status `ready` deltaP `6.5147` edge `0.0558` maxDD `-7.8324`
- `market_context_high->index_4h` score `-0.6025` n `147` status `ready` deltaP `9.5894` edge `0.0306` maxDD `-3.4082`
- `market_context_high->metal_1h` score `-0.6409` n `147` status `ready` deltaP `1.2118` edge `0.0143` maxDD `-1.0307`
- `market_context_high->fx_1h` score `-0.6495` n `147` status `ready` deltaP `-0.3585` edge `-0.0018` maxDD `-0.6615`
- `market_context_high->unknown_1h` score `-0.9919` n `147` status `ready` deltaP `-0.721` edge `-0.06` maxDD `-1.3217`
- `market_context_high->crypto_alt_4h` score `-1.0385` n `147` status `ready` deltaP `2.8383` edge `0.0536` maxDD `-9.7866`
- `market_context_high->crypto_major_4h` score `-1.145` n `147` status `ready` deltaP `8.8788` edge `0.066` maxDD `-14.7592`
- `market_context_high->equity_4h` score `-1.4572` n `147` status `ready` deltaP `3.3982` edge `0.2155` maxDD `-20.9976`
- `market_context_high->metal_4h` score `-1.6346` n `147` status `ready` deltaP `-1.373` edge `0.0459` maxDD `-4.7051`
- `market_context_high->metal_24h` score `-1.8122` n `144` status `ready` deltaP `-1.3889` edge `0.1177` maxDD `-8.2622`
- `market_context_high->fx_4h` score `-2.5601` n `147` status `ready` deltaP `-6.1318` edge `-0.004` maxDD `-2.1439`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
