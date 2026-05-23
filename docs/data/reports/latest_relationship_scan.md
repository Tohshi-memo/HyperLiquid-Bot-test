# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T21:06:20.944913+00:00`
- Price records: `672`
- Market context records: `1668`
- Flow alert records: `6709`
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

- `market_context_high->metal_24h` score `9.7645` n `165` status `ready` deltaP `28.532` edge `0.8661` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `4.8298` n `195` status `ready` deltaP `22.8901` edge `0.5163` maxDD `-16.3135`
- `market_context_high->index_24h` score `3.8227` n `165` status `ready` deltaP `20.1394` edge `0.3221` maxDD `-5.3574`
- `market_context_high->crypto_major_4h` score `2.937` n `195` status `ready` deltaP `18.9955` edge `0.389` maxDD `-13.3376`
- `market_context_high->equity_4h` score `2.1404` n `195` status `ready` deltaP `13.2028` edge `0.1998` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.8119` n `165` status `ready` deltaP `19.4453` edge `0.5112` maxDD `-33.1875`
- `market_context_high->crypto_major_24h` score `0.7583` n `165` status `ready` deltaP `25.3308` edge `0.7529` maxDD `-62.3533`
- `market_context_high->crypto_alt_1h` score `0.7095` n `207` status `ready` deltaP `6.644` edge `0.1172` maxDD `-4.1892`
- `market_context_high->crypto_alt_24h` score `0.6406` n `165` status `ready` deltaP `26.1141` edge `1.0602` maxDD `-88.8062`
- `market_context_high->equity_1h` score `-0.1969` n `207` status `ready` deltaP `2.9015` edge `0.0451` maxDD `-2.8014`
- `market_context_high->index_4h` score `-0.3128` n `195` status `ready` deltaP `3.1544` edge `0.0618` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `-0.348` n `207` status `ready` deltaP `3.9428` edge `0.0721` maxDD `-5.5244`
- `market_context_high->fx_24h` score `-0.396` n `165` status `ready` deltaP `7.0808` edge `0.0247` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.6411` n `207` status `ready` deltaP `-0.4122` edge `0.0125` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.8085` n `207` status `ready` deltaP `-0.1873` edge `-0.0029` maxDD `-0.3914`
- `market_context_high->metal_1h` score `-1.0519` n `207` status `ready` deltaP `5.3581` edge `0.0102` maxDD `-6.3532`
- `market_context_high->metal_4h` score `-1.1027` n `195` status `ready` deltaP `10.1243` edge `0.1098` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-1.2603` n `195` status `ready` deltaP `-8.3224` edge `-0.0132` maxDD `-1.4313`
- `market_context_high->commodity_1h` score `-2.0693` n `207` status `ready` deltaP `-1.6228` edge `-0.0307` maxDD `-13.5691`
- `market_context_high->unknown_24h` score `-3.521` n `165` status `ready` deltaP `9.6634` edge `0.1992` maxDD `-35.8966`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
