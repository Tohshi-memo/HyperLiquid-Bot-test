# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T01:52:32.836025+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5368`

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

- `market_context_high->unknown_1h` score `111.8472` n `95` status `ready` deltaP `-0.23` edge `9.3636` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `65.9548` n `95` status `ready` deltaP `2.4743` edge `5.5109` maxDD `-0.4928`
- `market_context_high->crypto_major_24h` score `10.6154` n `51` status `ready` deltaP `30.5759` edge `0.6944` maxDD `-0.423`
- `market_context_high->crypto_alt_24h` score `9.9532` n `51` status `ready` deltaP `24.9898` edge `0.7248` maxDD `-2.9571`
- `news_risk_high->crypto_major_4h` score `9.5106` n `65` status `ready` deltaP `33.1614` edge `0.5918` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.454` n `65` status `ready` deltaP `21.0061` edge `0.5322` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `4.7638` n `65` status `ready` deltaP `16.5893` edge `0.2964` maxDD `-0.1344`
- `market_context_high->crypto_major_4h` score `4.4034` n `95` status `ready` deltaP `18.7484` edge `0.3123` maxDD `-3.294`
- `news_risk_high->index_24h` score `3.478` n `65` status `ready` deltaP `24.3056` edge `0.1278` maxDD `0.0`
- `news_risk_high->index_4h` score `2.9302` n `65` status `ready` deltaP `32.2186` edge `0.0556` maxDD `-0.4296`
- `news_risk_high->equity_4h` score `2.9218` n `65` status `ready` deltaP `21.644` edge `0.1602` maxDD `-2.881`
- `news_risk_high->crypto_major_1h` score `2.5995` n `65` status `ready` deltaP `10.7646` edge `0.1804` maxDD `-1.5096`
- `market_context_high->crypto_major_1h` score `2.2078` n `95` status `ready` deltaP `15.1371` edge `0.1281` maxDD `-2.2692`
- `news_risk_high->metal_4h` score `2.1197` n `65` status `ready` deltaP `19.3832` edge `0.089` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.083` n `65` status `ready` deltaP `25.7669` edge `0.0168` maxDD `-0.1997`
- `market_context_high->equity_24h` score `1.6651` n `51` status `ready` deltaP `3.1353` edge `0.1381` maxDD `-0.6196`
- `market_context_high->fx_4h` score `1.4405` n `95` status `ready` deltaP `25.1717` edge `0.0279` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.4011` n `65` status `ready` deltaP `4.5693` edge `0.1382` maxDD `-2.4854`
- `market_context_high->fx_24h` score `1.3932` n `51` status `ready` deltaP `25.4902` edge `0.1008` maxDD `-1.703`
- `market_context_high->crypto_alt_4h` score `1.3337` n `95` status `ready` deltaP `4.164` edge `0.2623` maxDD `-7.6465`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
