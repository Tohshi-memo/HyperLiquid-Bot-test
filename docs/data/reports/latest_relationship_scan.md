# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T09:22:31.243688+00:00`
- Price records: `672`
- Market context records: `4710`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7424`

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

- `market_context_high->unknown_1h` score `76.9292` n `144` status `ready` deltaP `13.864` edge `6.3601` maxDD `-1.674`
- `market_context_high->unknown_4h` score `5.1309` n `141` status `ready` deltaP `13.0082` edge `0.4619` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `2.7986` n `135` status `ready` deltaP `14.6181` edge `0.2281` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.2976` n `144` status `ready` deltaP `2.5574` edge `0.0244` maxDD `-2.0345`
- `market_context_high->index_4h` score `-0.6774` n `141` status `ready` deltaP `5.0142` edge `-0.008` maxDD `-5.9823`
- `market_context_high->fx_4h` score `-0.9886` n `141` status `ready` deltaP `-2.3699` edge `-0.0027` maxDD `-1.9927`
- `market_context_high->commodity_4h` score `-1.0178` n `141` status `ready` deltaP `8.036` edge `0.0267` maxDD `-9.1941`
- `market_context_high->equity_1h` score `-1.1834` n `144` status `ready` deltaP `-1.5926` edge `0.0107` maxDD `-5.5624`
- `market_context_high->equity_4h` score `-1.198` n `141` status `ready` deltaP `1.8195` edge `0.0112` maxDD `-8.8203`
- `market_context_high->fx_1h` score `-1.308` n `144` status `ready` deltaP `-5.2853` edge `-0.0058` maxDD `-1.1038`
- `market_context_high->index_1h` score `-1.6445` n `144` status `ready` deltaP `-3.9338` edge `-0.0104` maxDD `-2.6999`
- `market_context_high->crypto_alt_1h` score `-3.2416` n `144` status `ready` deltaP `-1.3889` edge `-0.0776` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-3.7504` n `144` status `ready` deltaP `-1.5802` edge `-0.095` maxDD `-27.356`
- `market_context_high->commodity_24h` score `-4.401` n `135` status `ready` deltaP `16.9328` edge `0.0708` maxDD `-30.7016`
- `market_context_high->metal_1h` score `-4.4725` n `144` status `ready` deltaP `-5.776` edge `-0.0774` maxDD `-17.2107`
- `market_context_high->fx_24h` score `-4.7949` n `135` status `ready` deltaP `-13.044` edge `-0.0166` maxDD `-5.3476`
- `market_context_high->crypto_alt_4h` score `-8.1032` n `141` status `ready` deltaP `-1.972` edge `-0.16` maxDD `-63.9243`
- `market_context_high->index_24h` score `-8.3999` n `135` status `ready` deltaP `-10.6366` edge `-0.0916` maxDD `-29.3321`
- `market_context_high->metal_4h` score `-8.7188` n `141` status `ready` deltaP `2.7666` edge `-0.2509` maxDD `-64.494`
- `market_context_high->crypto_major_4h` score `-10.9307` n `141` status `ready` deltaP `-2.3763` edge `-0.2955` maxDD `-81.8692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
