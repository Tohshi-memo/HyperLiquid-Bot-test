# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T00:52:15.582722+00:00`
- Price records: `672`
- Market context records: `1685`
- Flow alert records: `6757`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8854`

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

- `market_context_high->metal_24h` score `7.9716` n `150` status `ready` deltaP `26.835` edge `0.728` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `5.4017` n `193` status `ready` deltaP `23.5136` edge `0.5598` maxDD `-16.3135`
- `market_context_high->index_24h` score `3.8872` n `150` status `ready` deltaP `18.2606` edge `0.34` maxDD `-5.3574`
- `market_context_high->crypto_major_4h` score `3.6621` n `193` status `ready` deltaP `20.6788` edge `0.4382` maxDD `-13.3376`
- `market_context_high->unknown_24h` score `3.4083` n `150` status `ready` deltaP `15.3702` edge `0.7136` maxDD `-35.8966`
- `market_context_high->equity_4h` score `2.8674` n `193` status `ready` deltaP `15.4651` edge `0.2453` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.9002` n `150` status `ready` deltaP `17.3241` edge `0.5327` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.4888` n `204` status `ready` deltaP `5.3393` edge `0.1075` maxDD `-4.1892`
- `market_context_high->crypto_alt_24h` score `0.3768` n `150` status `ready` deltaP `24.902` edge `1.0463` maxDD `-88.8062`
- `market_context_high->index_4h` score `0.1353` n `193` status `ready` deltaP `5.6813` edge `0.0823` maxDD `-3.7119`
- `market_context_high->equity_1h` score `-0.0949` n `204` status `ready` deltaP `3.6809` edge `0.0484` maxDD `-2.8014`
- `market_context_high->crypto_major_24h` score `-0.2022` n `150` status `ready` deltaP `23.5733` edge `0.6755` maxDD `-62.3533`
- `market_context_high->crypto_major_1h` score `-0.3946` n `204` status `ready` deltaP `3.2553` edge `0.0728` maxDD `-5.5244`
- `market_context_high->index_1h` score `-0.4911` n `204` status `ready` deltaP `1.0127` edge `0.0155` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.5441` n `204` status `ready` deltaP `7.0682` edge `0.0167` maxDD `-6.3532`
- `market_context_high->metal_4h` score `-0.6192` n `193` status `ready` deltaP `12.2377` edge `0.136` maxDD `-12.5349`
- `market_context_high->fx_24h` score `-0.6564` n `150` status `ready` deltaP `5.6263` edge `0.0127` maxDD `-1.3925`
- `market_context_high->fx_1h` score `-0.9696` n `204` status `ready` deltaP `-2.2455` edge `-0.0026` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-1.1932` n `193` status `ready` deltaP `-7.4229` edge `-0.0106` maxDD `-1.4313`
- `market_context_high->commodity_1h` score `-2.1051` n `204` status `ready` deltaP `0.8043` edge `-0.0298` maxDD `-14.9691`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
