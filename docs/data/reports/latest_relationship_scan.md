# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-22T21:52:24.666982+00:00`
- Price records: `672`
- Market context records: `7605`
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

- `market_context_high->unknown_24h` score `0.983` n `147` status `ready` deltaP `12.7091` edge `0.1246` maxDD `-5.1929`
- `market_context_high->equity_24h` score `0.6575` n `146` status `ready` deltaP `16.4575` edge `0.5126` maxDD `-38.3748`
- `market_context_high->commodity_24h` score `0.4333` n `146` status `ready` deltaP `15.8035` edge `0.0891` maxDD `-7.0012`
- `market_context_high->index_1h` score `0.0847` n `147` status `ready` deltaP `7.0448` edge `0.0118` maxDD `-0.8324`
- `market_context_high->crypto_major_1h` score `-0.154` n `147` status `ready` deltaP `7.9046` edge `0.0236` maxDD `-4.0162`
- `market_context_high->commodity_4h` score `-0.1768` n `147` status `ready` deltaP `6.5063` edge `0.0179` maxDD `-2.4139`
- `market_context_high->commodity_1h` score `-0.2373` n `147` status `ready` deltaP `3.9897` edge `0.0002` maxDD `-1.5775`
- `market_context_high->crypto_alt_1h` score `-0.2487` n `147` status `ready` deltaP `1.7007` edge `0.02` maxDD `-2.7243`
- `market_context_high->fx_24h` score `-0.3597` n `146` status `ready` deltaP `8.9686` edge `0.019` maxDD `-3.0343`
- `market_context_high->equity_1h` score `-0.4852` n `147` status `ready` deltaP `6.0642` edge `0.0536` maxDD `-7.8324`
- `market_context_high->index_4h` score `-0.5858` n `147` status `ready` deltaP `9.8952` edge `0.0307` maxDD `-3.4082`
- `market_context_high->metal_1h` score `-0.6316` n `147` status `ready` deltaP `1.3615` edge `0.0145` maxDD `-1.0307`
- `market_context_high->fx_1h` score `-0.6363` n `147` status `ready` deltaP `-0.2083` edge `-0.0017` maxDD `-0.6615`
- `market_context_high->crypto_alt_4h` score `-0.9945` n `147` status `ready` deltaP `3.2956` edge `0.0562` maxDD `-9.7866`
- `market_context_high->unknown_1h` score `-1.0215` n `147` status `ready` deltaP `-1.1701` edge `-0.0608` maxDD `-1.3217`
- `market_context_high->crypto_major_4h` score `-1.1088` n `147` status `ready` deltaP `9.3361` edge `0.0676` maxDD `-14.7592`
- `market_context_high->equity_4h` score `-1.4626` n `147` status `ready` deltaP `3.3982` edge `0.2148` maxDD `-20.9976`
- `market_context_high->metal_4h` score `-1.6236` n `147` status `ready` deltaP `-1.2206` edge `0.0463` maxDD `-4.7051`
- `market_context_high->metal_24h` score `-1.8809` n `147` status `ready` deltaP `-1.435` edge `0.1092` maxDD `-8.2622`
- `market_context_high->fx_4h` score `-2.5968` n `147` status `ready` deltaP `-6.5905` edge `-0.004` maxDD `-2.1439`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
