# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T06:52:30.290545+00:00`
- Price records: `672`
- Market context records: `4803`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7530`

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

- `market_context_high->unknown_1h` score `11.0206` n `120` status `ready` deltaP `12.006` edge `0.8801` maxDD `-1.674`
- `market_context_high->unknown_4h` score `7.8084` n `119` status `ready` deltaP `18.6065` edge `0.6477` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `2.3014` n `113` status `ready` deltaP `13.1576` edge `0.1964` maxDD `-4.7201`
- `market_context_high->equity_4h` score `0.3753` n `119` status `ready` deltaP `10.1173` edge `0.126` maxDD `-6.9604`
- `market_context_high->commodity_4h` score `0.1133` n `119` status `ready` deltaP `12.3962` edge `0.0491` maxDD `-4.377`
- `market_context_high->commodity_1h` score `-0.0055` n `120` status `ready` deltaP `4.7255` edge `0.0268` maxDD `-2.0345`
- `market_context_high->index_4h` score `-0.2085` n `119` status `ready` deltaP `8.8159` edge `0.0198` maxDD `-5.4242`
- `market_context_high->fx_4h` score `-0.3236` n `119` status `ready` deltaP `4.9267` edge `0.0033` maxDD `-1.5439`
- `market_context_high->equity_1h` score `-0.5687` n `120` status `ready` deltaP `3.0988` edge `0.0087` maxDD `-4.1397`
- `market_context_high->fx_1h` score `-0.8948` n `120` status `ready` deltaP `-1.023` edge `-0.0028` maxDD `-0.8626`
- `market_context_high->index_1h` score `-1.3181` n `120` status `ready` deltaP `-0.514` edge `-0.006` maxDD `-2.6999`
- `market_context_high->commodity_24h` score `-2.1038` n `113` status `ready` deltaP `19.8992` edge `0.1085` maxDD `-27.5371`
- `market_context_high->metal_1h` score `-2.2551` n `120` status `ready` deltaP `-0.7435` edge `-0.0666` maxDD `-14.0715`
- `market_context_high->fx_24h` score `-2.842` n `113` status `ready` deltaP `-11.7226` edge `-0.0181` maxDD `-3.2466`
- `market_context_high->crypto_major_1h` score `-2.8816` n `120` status `ready` deltaP `0.9431` edge `-0.0667` maxDD `-22.0555`
- `market_context_high->crypto_alt_1h` score `-2.9566` n `120` status `ready` deltaP `1.8812` edge `-0.0385` maxDD `-14.9676`
- `market_context_high->crypto_alt_4h` score `-4.5052` n `119` status `ready` deltaP `6.5254` edge `0.0032` maxDD `-44.6097`
- `market_context_high->index_24h` score `-6.865` n `113` status `ready` deltaP `-8.0307` edge `-0.1277` maxDD `-23.2678`
- `market_context_high->crypto_major_4h` score `-8.1434` n `119` status `ready` deltaP `3.6957` edge `-0.147` maxDD `-68.4001`
- `market_context_high->metal_4h` score `-8.4196` n `119` status `ready` deltaP `6.127` edge `-0.2962` maxDD `-61.2596`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
