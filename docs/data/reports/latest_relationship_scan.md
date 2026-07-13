# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T15:22:27.608077+00:00`
- Price records: `672`
- Market context records: `6615`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9810`

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

- `market_context_high->unknown_24h` score `3.3739` n `173` status `ready` deltaP `1.4491` edge `0.5447` maxDD `-12.5228`
- `market_context_high->unknown_1h` score `2.1106` n `204` status `ready` deltaP `-6.3168` edge `0.3081` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `0.1666` n `173` status `ready` deltaP `7.2455` edge `0.1524` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.171` n `204` status `ready` deltaP `7.3265` edge `0.0297` maxDD `-4.704`
- `market_context_high->fx_1h` score `-0.2723` n `204` status `ready` deltaP `2.2983` edge `0.0005` maxDD `-0.7249`
- `market_context_high->commodity_1h` score `-0.5638` n `204` status `ready` deltaP `-0.0117` edge `-0.0039` maxDD `-2.1314`
- `market_context_high->crypto_alt_1h` score `-0.5813` n `204` status `ready` deltaP `4.4264` edge `0.0193` maxDD `-3.7803`
- `market_context_high->index_1h` score `-0.5845` n `204` status `ready` deltaP `-0.9129` edge `0.0031` maxDD `-0.7564`
- `market_context_high->index_4h` score `-0.8874` n `204` status `ready` deltaP `9.7501` edge `0.0092` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-1.0965` n `204` status `ready` deltaP `2.043` edge `-0.0011` maxDD `-3.978`
- `market_context_high->metal_1h` score `-1.2116` n `204` status `ready` deltaP `-3.719` edge `-0.0006` maxDD `-1.7126`
- `market_context_high->commodity_4h` score `-1.234` n `204` status `ready` deltaP `-0.3348` edge `-0.0065` maxDD `-5.6246`
- `market_context_high->unknown_4h` score `-1.4622` n `204` status `ready` deltaP `-17.8324` edge `0.2376` maxDD `-10.5788`
- `market_context_high->fx_4h` score `-1.6271` n `204` status `ready` deltaP `2.0564` edge `-0.0011` maxDD `-3.3635`
- `market_context_high->crypto_major_4h` score `-1.6437` n `204` status `ready` deltaP `8.0284` edge `0.0672` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-2.058` n `204` status `ready` deltaP `4.881` edge `0.0438` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.1157` n `204` status `ready` deltaP `-0.81` edge `0.0202` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-3.0559` n `204` status `ready` deltaP `7.9837` edge `-0.0181` maxDD `-27.1529`
- `market_context_high->metal_24h` score `-3.8465` n `173` status `ready` deltaP `-1.0721` edge `0.0498` maxDD `-13.5305`
- `market_context_high->fx_24h` score `-5.7002` n `173` status `ready` deltaP `-7.1274` edge `-0.0007` maxDD `-9.1439`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
