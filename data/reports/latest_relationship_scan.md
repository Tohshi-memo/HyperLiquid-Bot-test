# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T18:22:34.466206+00:00`
- Price records: `672`
- Market context records: `4542`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9932`

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

- `market_context_high->unknown_1h` score `55.7472` n `172` status `ready` deltaP `7.4468` edge `4.646` maxDD `-2.3371`
- `market_context_high->unknown_4h` score `30.1771` n `170` status `ready` deltaP `8.3483` edge `2.6157` maxDD `-7.5275`
- `market_context_high->fx_4h` score `-0.4738` n `170` status `ready` deltaP `6.7952` edge `0.0022` maxDD `-1.9927`
- `market_context_high->commodity_1h` score `-0.6129` n `172` status `ready` deltaP `0.0069` edge `0.0133` maxDD `-3.0206`
- `market_context_high->fx_1h` score `-0.7125` n `172` status `ready` deltaP `-0.0279` edge `-0.0033` maxDD `-1.1377`
- `market_context_high->equity_4h` score `-0.9875` n `170` status `ready` deltaP `3.8594` edge `0.0689` maxDD `-8.8203`
- `market_context_high->index_1h` score `-1.0529` n `172` status `ready` deltaP `-3.4083` edge `-0.0114` maxDD `-2.7358`
- `market_context_high->equity_1h` score `-1.0661` n `172` status `ready` deltaP `-1.7163` edge `0.0213` maxDD `-5.5624`
- `market_context_high->index_4h` score `-1.103` n `170` status `ready` deltaP `0.2852` edge `-0.0102` maxDD `-5.9823`
- `market_context_high->commodity_4h` score `-1.4382` n `170` status `ready` deltaP `1.6087` edge `0.0206` maxDD `-9.5902`
- `market_context_high->unknown_24h` score `-2.7093` n `170` status `ready` deltaP `2.4244` edge `-0.1496` maxDD `-4.7201`
- `market_context_high->metal_1h` score `-4.5046` n `172` status `ready` deltaP `-4.4667` edge `-0.0777` maxDD `-18.0993`
- `market_context_high->crypto_alt_1h` score `-5.2999` n `172` status `ready` deltaP `-2.8095` edge `-0.0942` maxDD `-22.2982`
- `market_context_high->fx_24h` score `-5.4623` n `170` status `ready` deltaP `-13.2394` edge `-0.0157` maxDD `-6.0982`
- `market_context_high->index_24h` score `-5.6889` n `170` status `ready` deltaP `-8.7684` edge `-0.1334` maxDD `-29.3321`
- `market_context_high->crypto_major_1h` score `-6.2741` n `172` status `ready` deltaP `-4.404` edge `-0.1182` maxDD `-27.356`
- `market_context_high->commodity_24h` score `-8.4016` n `170` status `ready` deltaP `4.2259` edge `0.0116` maxDD `-46.5259`
- `market_context_high->crypto_alt_4h` score `-13.3053` n `170` status `ready` deltaP `-1.8077` edge `-0.231` maxDD `-63.9243`
- `market_context_high->equity_24h` score `-13.4576` n `170` status `ready` deltaP `-0.8517` edge `-0.2517` maxDD `-102.1031`
- `market_context_high->metal_4h` score `-15.5618` n `170` status `ready` deltaP `-7.0373` edge `-0.315` maxDD `-68.4587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
