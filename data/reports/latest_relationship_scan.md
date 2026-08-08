# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-08T22:37:29.641921+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8733`

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

- `market_context_high->equity_24h` score `3.0096` n `103` status `ready` deltaP `4.5729` edge `0.5263` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.4494` n `103` status `ready` deltaP `12.2118` edge `0.1803` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.716` n `113` status `ready` deltaP `16.7993` edge `0.0983` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `1.0229` n `120` status `ready` deltaP `12.2006` edge `0.0382` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.8767` n `103` status `ready` deltaP `22.2694` edge `0.0506` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.4417` n `103` status `ready` deltaP `9.1002` edge `0.1491` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.4829` n `120` status `ready` deltaP `2.1158` edge `-0.0048` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.5666` n `120` status `ready` deltaP `-4.0219` edge `-0.0069` maxDD `-0.7809`
- `market_context_high->index_4h` score `-0.6222` n `113` status `ready` deltaP `-1.0441` edge `-0.0123` maxDD `-1.1743`
- `market_context_high->metal_1h` score `-0.6393` n `120` status `ready` deltaP `-3.8523` edge `-0.0067` maxDD `-0.9664`
- `market_context_high->equity_1h` score `-0.6419` n `120` status `ready` deltaP `2.4251` edge `0.0132` maxDD `-4.6286`
- `market_context_high->fx_4h` score `-0.6774` n `113` status `ready` deltaP `3.5209` edge `-0.0046` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-1.1752` n `113` status `ready` deltaP `-5.0075` edge `-0.0164` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-2.111` n `120` status `ready` deltaP `-12.4201` edge `-0.0302` maxDD `-2.3669`
- `market_context_high->equity_4h` score `-2.2391` n `113` status `ready` deltaP `1.2802` edge `-0.0614` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-2.8618` n `120` status `ready` deltaP `-9.6607` edge `-0.0609` maxDD `-5.7207`
- `market_context_high->crypto_major_24h` score `-3.7771` n `103` status `ready` deltaP `6.2197` edge `-0.1068` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-4.3114` n `103` status `ready` deltaP `-12.4461` edge `-0.132` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-4.749` n `113` status `ready` deltaP `-13.3742` edge `-0.1414` maxDD `-6.5487`
- `market_context_high->unknown_1h` score `-8.3533` n `120` status `ready` deltaP `-5.1297` edge `-0.6172` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
