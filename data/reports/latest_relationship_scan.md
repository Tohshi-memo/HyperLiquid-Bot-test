# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T20:52:28.830648+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11613`

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

- `risk_on_high->unknown_4h` score `27.7142` n `133` status `ready` deltaP `11.4375` edge `2.2951` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `27.7142` n `133` status `ready` deltaP `11.4375` edge `2.2951` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `20.9492` n `167` status `ready` deltaP `13.0358` edge `1.7284` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `15.3521` n `133` status `ready` deltaP `0.7428` edge `1.3321` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `15.3521` n `133` status `ready` deltaP `0.7428` edge `1.3321` maxDD `-1.95`
- `market_context_high->unknown_1h` score `10.8723` n `167` status `ready` deltaP `1.1976` edge `0.9611` maxDD `-2.0446`
- `market_context_high->equity_24h` score `1.2596` n `127` status `ready` deltaP `17.3447` edge `0.4239` maxDD `-20.7654`
- `risk_on_high->equity_24h` score `0.7767` n `107` status `ready` deltaP `12.5909` edge `0.3953` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `0.7767` n `107` status `ready` deltaP `12.5909` edge `0.3953` maxDD `-19.828`
- `news_risk_high->crypto_alt_24h` score `0.6954` n `67` status `ready` deltaP `16.9206` edge `0.2698` maxDD `-19.4761`
- `news_risk_high->commodity_4h` score `0.3944` n `67` status `ready` deltaP `7.1669` edge `0.0387` maxDD `-0.8733`
- `news_risk_high->equity_24h` score `0.3035` n `67` status `ready` deltaP `5.0166` edge `0.2522` maxDD `-15.4056`
- `risk_on_high->metal_1h` score `0.0782` n `133` status `ready` deltaP `11.9637` edge `0.0015` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0782` n `133` status `ready` deltaP `11.9637` edge `0.0015` maxDD `-1.699`
- `news_risk_high->fx_4h` score `0.0337` n `67` status `ready` deltaP `9.6514` edge `0.0041` maxDD `-1.2507`
- `news_risk_high->index_1h` score `-0.0344` n `67` status `ready` deltaP `5.0742` edge `-0.0029` maxDD `-0.8275`
- `risk_on_high->index_1h` score `-0.0726` n `133` status `ready` deltaP `5.4894` edge `-0.0014` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.0726` n `133` status `ready` deltaP `5.4894` edge `-0.0014` maxDD `-0.5605`
- `news_risk_high->crypto_major_24h` score `-0.0778` n `67` status `ready` deltaP `13.4173` edge `0.3389` maxDD `-30.7329`
- `risk_on_high->fx_24h` score `-0.1408` n `107` status `ready` deltaP `25.7075` edge `0.0803` maxDD `-4.2453`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
