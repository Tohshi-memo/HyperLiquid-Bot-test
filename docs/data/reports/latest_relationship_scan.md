# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T09:52:25.404934+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9226`

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

- `market_context_high->equity_24h` score `8.738` n `32` status `ready` deltaP `16.4931` edge `0.8555` maxDD `-16.6495`
- `market_context_high->commodity_24h` score `2.4017` n `32` status `ready` deltaP `7.8125` edge `0.2068` maxDD `-1.6995`
- `market_context_high->index_24h` score `1.3405` n `32` status `ready` deltaP `16.6667` edge `0.107` maxDD `-2.3671`
- `market_context_high->fx_24h` score `0.8598` n `32` status `ready` deltaP `12.3264` edge `-0.0017` maxDD `-0.0397`
- `market_context_high->metal_1h` score `-0.3257` n `88` status `ready` deltaP `4.0964` edge `0.0132` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.4891` n `88` status `ready` deltaP `0.592` edge `0.0016` maxDD `-1.7935`
- `market_context_high->metal_4h` score `-0.6753` n `83` status `ready` deltaP `1.8366` edge `0.0184` maxDD `-3.7107`
- `market_context_high->commodity_4h` score `-0.8092` n `83` status `ready` deltaP `-2.766` edge `0.0253` maxDD `-4.182`
- `market_context_high->index_4h` score `-0.832` n `83` status `ready` deltaP `3.3023` edge `0.0064` maxDD `-2.4866`
- `market_context_high->index_1h` score `-0.8531` n `88` status `ready` deltaP `-5.2599` edge `0.0088` maxDD `-0.9814`
- `market_context_high->equity_1h` score `-1.2088` n `88` status `ready` deltaP `-5.4096` edge `0.0647` maxDD `-8.0225`
- `market_context_high->fx_1h` score `-1.2883` n `88` status `ready` deltaP `-13.6091` edge `-0.006` maxDD `-0.8088`
- `market_context_high->crypto_alt_1h` score `-1.7628` n `88` status `ready` deltaP `1.6807` edge `-0.0393` maxDD `-10.8319`
- `market_context_high->metal_24h` score `-1.9358` n `32` status `ready` deltaP `-2.9514` edge `-0.1732` maxDD `-1.4245`
- `market_context_high->fx_4h` score `-2.3535` n `83` status `ready` deltaP `-10.5899` edge `-0.013` maxDD `-2.4506`
- `market_context_high->crypto_major_1h` score `-3.0528` n `88` status `ready` deltaP `-4.212` edge `-0.101` maxDD `-15.9848`
- `market_context_high->crypto_major_24h` score `-4.1086` n `32` status `ready` deltaP `-4.8611` edge `0.0543` maxDD `-23.1423`
- `market_context_high->equity_4h` score `-4.9367` n `83` status `ready` deltaP `1.394` edge `-0.0427` maxDD `-24.9053`
- `market_context_high->crypto_alt_4h` score `-8.8346` n `83` status `ready` deltaP `0.72` edge `-0.2292` maxDD `-34.2787`
- `market_context_high->crypto_alt_24h` score `-9.2494` n `32` status `ready` deltaP `-18.75` edge `-0.1879` maxDD `-29.9639`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
