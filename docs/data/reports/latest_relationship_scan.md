# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T10:27:00.559132+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9250`

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

- `market_context_high->equity_24h` score `8.5904` n `32` status `ready` deltaP `16.4931` edge `0.8432` maxDD `-16.6495`
- `market_context_high->commodity_24h` score `2.3806` n `32` status `ready` deltaP `7.6389` edge `0.2062` maxDD `-1.6995`
- `market_context_high->index_24h` score `1.3335` n `32` status `ready` deltaP `16.6667` edge `0.1061` maxDD `-2.3671`
- `market_context_high->fx_24h` score `0.8634` n `32` status `ready` deltaP `12.3264` edge `-0.0014` maxDD `-0.0397`
- `market_context_high->metal_1h` score `-0.3401` n `88` status `ready` deltaP `3.9467` edge `0.013` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.4813` n `88` status `ready` deltaP `0.7417` edge `0.0016` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.7386` n `85` status `ready` deltaP `-1.632` edge `0.0268` maxDD `-4.182`
- `market_context_high->index_4h` score `-0.8438` n `85` status `ready` deltaP `3.0505` edge `0.0071` maxDD `-2.4871`
- `market_context_high->metal_4h` score `-0.856` n `85` status `ready` deltaP `0.6743` edge `0.0144` maxDD `-3.9577`
- `market_context_high->index_1h` score `-0.8702` n `88` status `ready` deltaP `-5.5593` edge `0.0086` maxDD `-0.9814`
- `market_context_high->equity_1h` score `-1.2275` n `88` status `ready` deltaP `-5.5593` edge `0.0633` maxDD `-8.0225`
- `market_context_high->fx_1h` score `-1.2805` n `88` status `ready` deltaP `-13.4594` edge `-0.006` maxDD `-0.8088`
- `market_context_high->crypto_alt_1h` score `-1.7854` n `88` status `ready` deltaP `1.531` edge `-0.0412` maxDD `-10.8319`
- `market_context_high->metal_24h` score `-1.9765` n `32` status `ready` deltaP `-3.2986` edge `-0.1761` maxDD `-1.4245`
- `market_context_high->fx_4h` score `-2.2805` n `85` status `ready` deltaP `-9.41` edge `-0.0115` maxDD `-2.4506`
- `market_context_high->crypto_major_1h` score `-3.0513` n `88` status `ready` deltaP `-4.212` edge `-0.1008` maxDD `-15.9848`
- `market_context_high->crypto_major_24h` score `-4.027` n `32` status `ready` deltaP `-4.8611` edge `0.0611` maxDD `-23.1423`
- `market_context_high->equity_4h` score `-4.8459` n `85` status `ready` deltaP `1.2841` edge `-0.0344` maxDD `-24.9053`
- `market_context_high->crypto_alt_4h` score `-8.5475` n `85` status `ready` deltaP `1.8041` edge `-0.2125` maxDD `-34.2787`
- `market_context_high->crypto_alt_24h` score `-9.2722` n `32` status `ready` deltaP `-18.75` edge `-0.1898` maxDD `-29.9639`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
