# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T15:07:30.062039+00:00`
- Price records: `672`
- Market context records: `5258`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9598`

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

- `market_context_high->unknown_24h` score `26.2035` n `146` status `ready` deltaP `29.8896` edge `1.9937` maxDD `-0.4141`
- `market_context_high->crypto_major_24h` score `10.6555` n `146` status `ready` deltaP `28.9003` edge `1.0557` maxDD `-22.166`
- `market_context_high->crypto_alt_4h` score `3.99` n `159` status `ready` deltaP `13.6927` edge `0.4053` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.7393` n `159` status `ready` deltaP `13.8835` edge `0.4483` maxDD `-14.0065`
- `market_context_high->equity_24h` score `3.3404` n `146` status `ready` deltaP `19.4326` edge `0.7117` maxDD `-40.0306`
- `market_context_high->unknown_4h` score `1.7925` n `159` status `ready` deltaP `16.6494` edge `0.1406` maxDD `-5.5109`
- `market_context_high->crypto_alt_24h` score `0.8355` n `146` status `ready` deltaP `15.7605` edge `0.5506` maxDD `-35.8838`
- `market_context_high->crypto_alt_1h` score `0.5854` n `168` status `ready` deltaP `4.9259` edge `0.1121` maxDD `-5.0257`
- `market_context_high->equity_4h` score `0.5657` n `159` status `ready` deltaP `8.4915` edge `0.1544` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.506` n `146` status `ready` deltaP `12.5547` edge `0.048` maxDD `-0.8294`
- `market_context_high->crypto_major_1h` score `0.3474` n `168` status `ready` deltaP `5.8347` edge `0.1146` maxDD `-6.9639`
- `market_context_high->index_24h` score `0.2027` n `146` status `ready` deltaP `20.8476` edge `0.0505` maxDD `-7.413`
- `market_context_high->equity_1h` score `0.0637` n `168` status `ready` deltaP `6.3801` edge `0.0593` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.0642` n `168` status `ready` deltaP `5.0435` edge `0.0114` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.0657` n `168` status `ready` deltaP `5.2217` edge `0.0189` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.273` n `168` status `ready` deltaP `1.4721` edge `0.0001` maxDD `-0.5936`
- `market_context_high->unknown_1h` score `-0.423` n `168` status `ready` deltaP `7.8593` edge `-0.0235` maxDD `-2.7986`
- `market_context_high->index_4h` score `-0.7237` n `159` status `ready` deltaP `4.7745` edge `0.0196` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.8016` n `159` status `ready` deltaP `-0.0268` edge `0.0005` maxDD `-1.5809`
- `market_context_high->commodity_1h` score `-1.2447` n `168` status `ready` deltaP `-2.0887` edge `-0.0057` maxDD `-2.728`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
