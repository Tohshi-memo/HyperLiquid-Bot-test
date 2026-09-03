# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T15:15:19.105407+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11625`

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

- `risk_on_high->unknown_4h` score `33.8862` n `133` status `ready` deltaP `12.657` edge `2.8013` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `33.8862` n `133` status `ready` deltaP `12.657` edge `2.8013` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `27.1212` n `167` status `ready` deltaP `14.2553` edge `2.2346` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `18.25` n `133` status `ready` deltaP `1.3416` edge `1.5696` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `18.25` n `133` status `ready` deltaP `1.3416` edge `1.5696` maxDD `-1.95`
- `market_context_high->unknown_1h` score `13.7702` n `167` status `ready` deltaP `1.7964` edge `1.1986` maxDD `-2.0446`
- `market_context_high->equity_24h` score `3.2703` n `127` status `ready` deltaP `21.1641` edge `0.566` maxDD `-20.7654`
- `news_risk_high->crypto_alt_24h` score `3.1849` n `67` status `ready` deltaP `20.74` edge `0.5635` maxDD `-19.4761`
- `risk_on_high->equity_24h` score `2.7874` n `107` status `ready` deltaP `16.4103` edge `0.5374` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `2.7874` n `107` status `ready` deltaP `16.4103` edge `0.5374` maxDD `-19.828`
- `news_risk_high->crypto_major_24h` score `2.7034` n `67` status `ready` deltaP `17.2368` edge `0.67` maxDD `-30.7329`
- `news_risk_high->equity_24h` score `1.6105` n `67` status `ready` deltaP `8.836` edge `0.3943` maxDD `-15.4056`
- `risk_on_high->crypto_alt_24h` score `0.9321` n `107` status `ready` deltaP `16.5693` edge `0.6994` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `0.9321` n `107` status `ready` deltaP `16.5693` edge `0.6994` maxDD `-42.8959`
- `market_context_high->crypto_alt_24h` score `0.653` n `127` status `ready` deltaP `18.225` edge `0.7121` maxDD `-46.3234`
- `news_risk_high->commodity_4h` score `0.2852` n `67` status `ready` deltaP `6.2523` edge `0.0308` maxDD `-0.8733`
- `news_risk_high->fx_4h` score `0.0555` n `67` status `ready` deltaP `9.8039` edge `0.0049` maxDD `-1.2507`
- `risk_on_high->metal_1h` score `0.0361` n `133` status `ready` deltaP `11.2152` edge `0.0011` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0361` n `133` status `ready` deltaP `11.2152` edge `0.0011` maxDD `-1.699`
- `risk_on_high->crypto_alt_1h` score `-0.0423` n `133` status `ready` deltaP `5.4995` edge `0.0615` maxDD `-5.4685`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
