# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T08:07:18.132840+00:00`
- Price records: `672`
- Market context records: `2023`
- Flow alert records: `7716`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9091`

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

- `market_context_high->crypto_major_4h` score `8.9183` n `205` status `ready` deltaP `30.7927` edge `0.5909` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `8.4186` n `205` status `ready` deltaP `24.5427` edge `0.6524` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `5.9157` n `205` status `ready` deltaP `18.689` edge `0.4433` maxDD `-2.6599`
- `market_context_high->equity_4h` score `3.0095` n `205` status `ready` deltaP `17.2561` edge `0.2452` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `1.5177` n `205` status `ready` deltaP `12.328` edge `0.1429` maxDD `-3.2225`
- `market_context_high->index_4h` score `1.4222` n `205` status `ready` deltaP `12.9269` edge `0.1007` maxDD `-1.8022`
- `market_context_high->crypto_alt_1h` score `1.2126` n `205` status `ready` deltaP `9.7831` edge `0.1472` maxDD `-4.9097`
- `market_context_high->unknown_24h` score `0.4643` n `193` status `ready` deltaP `16.3097` edge `0.462` maxDD `-35.8966`
- `market_context_high->equity_24h` score `0.2419` n `193` status `ready` deltaP `15.2557` edge `0.4083` maxDD `-33.1875`
- `market_context_high->equity_1h` score `0.2056` n `205` status `ready` deltaP `6.9104` edge `0.0499` maxDD `-2.6402`
- `market_context_high->unknown_1h` score `0.0146` n `205` status `ready` deltaP `3.5965` edge `0.0492` maxDD `-3.0902`
- `market_context_high->index_24h` score `0.0126` n `193` status `ready` deltaP `3.5986` edge `0.0999` maxDD `-4.1604`
- `market_context_high->fx_24h` score `-0.2854` n `193` status `ready` deltaP `12.4716` edge `0.0246` maxDD `-2.1887`
- `market_context_high->index_1h` score `-0.3241` n `205` status `ready` deltaP `2.2543` edge `0.017` maxDD `-1.3898`
- `market_context_high->metal_24h` score `-0.7062` n `193` status `ready` deltaP `11.1842` edge `0.1536` maxDD `-16.2941`
- `market_context_high->fx_1h` score `-0.8757` n `205` status `ready` deltaP `-1.5912` edge `0.0004` maxDD `-0.3548`
- `market_context_high->metal_1h` score `-0.9078` n `205` status `ready` deltaP `3.6585` edge `0.0187` maxDD `-5.166`
- `market_context_high->metal_4h` score `-1.3828` n `205` status `ready` deltaP `7.8049` edge `0.095` maxDD `-11.9812`
- `market_context_high->fx_4h` score `-1.5817` n `205` status `ready` deltaP `-6.2805` edge `-0.0018` maxDD `-1.0513`
- `market_context_high->commodity_1h` score `-1.8138` n `205` status `ready` deltaP `3.2043` edge `0.0019` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
