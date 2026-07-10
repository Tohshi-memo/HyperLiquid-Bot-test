# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-10T14:37:28.045140+00:00`
- Price records: `672`
- Market context records: `6292`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11116`

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

- `news_risk_high->crypto_alt_24h` score `15.2178` n `32` status `ready` deltaP `43.2292` edge `0.9947` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `5.9677` n `32` status `ready` deltaP `50.5208` edge `0.1605` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1889` n `32` status `ready` deltaP `43.8262` edge `0.0615` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `4.1204` n `32` status `ready` deltaP `16.6667` edge `0.4951` maxDD `-4.2368`
- `news_risk_high->commodity_24h` score `2.9125` n `32` status `ready` deltaP `27.0833` edge `0.0827` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.4003` n `32` status `ready` deltaP `28.8922` edge `0.0213` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.4187` n `32` status `ready` deltaP `14.2777` edge `0.1334` maxDD `-2.0691`
- `market_context_high->unknown_1h` score `1.2856` n `207` status `ready` deltaP `-0.6979` edge `0.2126` maxDD `-3.7317`
- `news_risk_high->crypto_alt_1h` score `0.9104` n `32` status `ready` deltaP `11.7702` edge `0.0844` maxDD `-1.6923`
- `market_context_high->equity_4h` score `0.3162` n `195` status `ready` deltaP `7.2702` edge `0.0696` maxDD `-2.671`
- `market_context_high->unknown_4h` score `0.0692` n `195` status `ready` deltaP `-4.2753` edge `0.2875` maxDD `-11.925`
- `market_context_high->metal_4h` score `-0.1752` n `195` status `ready` deltaP `7.1733` edge `0.0339` maxDD `-2.7056`
- `market_context_high->metal_24h` score `-0.1837` n `178` status `ready` deltaP `19.9789` edge `0.1001` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.3301` n `32` status `ready` deltaP `6.7708` edge `-0.0003` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.4169` n `207` status `ready` deltaP `3.5277` edge `0.0008` maxDD `-1.8877`
- `market_context_high->commodity_1h` score `-0.5046` n `207` status `ready` deltaP `-0.1736` edge `-0.0003` maxDD `-1.7253`
- `market_context_high->fx_1h` score `-0.7294` n `207` status `ready` deltaP `-1.1803` edge `-0.0019` maxDD `-0.748`
- `news_risk_high->metal_1h` score `-0.734` n `32` status `ready` deltaP `-2.994` edge `-0.0244` maxDD `-1.6464`
- `market_context_high->commodity_4h` score `-0.8555` n `195` status `ready` deltaP `-3.3193` edge `0.0043` maxDD `-1.3482`
- `market_context_high->index_1h` score `-0.8628` n `207` status `ready` deltaP `-3.7049` edge `0.001` maxDD `-0.9531`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
