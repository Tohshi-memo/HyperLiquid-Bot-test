# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T01:07:20.658377+00:00`
- Price records: `672`
- Market context records: `1686`
- Flow alert records: `6760`
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

- `market_context_high->metal_24h` score `7.826` n `149` status `ready` deltaP `26.7098` edge `0.7167` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `5.4896` n `192` status `ready` deltaP `23.9076` edge `0.5645` maxDD `-16.3135`
- `market_context_high->index_24h` score `3.8845` n `149` status `ready` deltaP `18.1219` edge `0.3407` maxDD `-5.3574`
- `market_context_high->unknown_24h` score `3.8708` n `149` status `ready` deltaP `15.7207` edge `0.7498` maxDD `-35.8966`
- `market_context_high->crypto_major_4h` score `3.7419` n `192` status `ready` deltaP `21.062` edge `0.4423` maxDD `-13.3376`
- `market_context_high->equity_4h` score `2.8688` n `192` status `ready` deltaP `15.3329` edge `0.2463` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.8985` n `149` status `ready` deltaP `17.1675` edge `0.5336` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.4972` n `204` status `ready` deltaP `5.3393` edge `0.1082` maxDD `-4.1892`
- `market_context_high->crypto_alt_24h` score `0.3685` n `149` status `ready` deltaP `24.8125` edge `1.0462` maxDD `-88.8062`
- `market_context_high->index_4h` score `0.1527` n `192` status `ready` deltaP `5.8689` edge `0.0825` maxDD `-3.7119`
- `market_context_high->equity_1h` score `-0.0617` n `204` status `ready` deltaP `4.0214` edge `0.0489` maxDD `-2.8014`
- `market_context_high->crypto_major_24h` score `-0.2558` n `149` status `ready` deltaP `23.4435` edge `0.6695` maxDD `-62.3533`
- `market_context_high->crypto_major_1h` score `-0.3754` n `204` status `ready` deltaP `3.2553` edge `0.0744` maxDD `-5.5244`
- `market_context_high->index_1h` score `-0.4887` n `204` status `ready` deltaP `1.0127` edge `0.0157` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.5441` n `204` status `ready` deltaP `7.0682` edge `0.0167` maxDD `-6.3532`
- `market_context_high->metal_4h` score `-0.6322` n `192` status `ready` deltaP `12.0299` edge `0.1363` maxDD `-12.5349`
- `market_context_high->fx_24h` score `-0.6758` n `149` status `ready` deltaP `5.5189` edge `0.0118` maxDD `-1.3925`
- `market_context_high->fx_1h` score `-0.9956` n `204` status `ready` deltaP `-2.586` edge `-0.0025` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-1.1884` n `192` status `ready` deltaP `-7.3298` edge `-0.0106` maxDD `-1.4313`
- `market_context_high->commodity_1h` score `-2.0773` n `204` status `ready` deltaP `1.1448` edge `-0.0285` maxDD `-14.9691`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
