# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-02T21:22:33.159131+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11521`

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

- `risk_on_high->equity_24h` score `6.2885` n `107` status `ready` deltaP `27.1742` edge `0.7574` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `6.2885` n `107` status `ready` deltaP `27.1742` edge `0.7574` maxDD `-19.828`
- `risk_on_high->unknown_4h` score `6.2479` n `107` status `ready` deltaP `18.2386` edge `0.4609` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `6.2479` n `107` status `ready` deltaP `18.2386` edge `0.4609` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `4.3286` n `147` status `ready` deltaP `13.9726` edge `0.3371` maxDD `-2.563`
- `news_risk_high->equity_24h` score `3.2887` n `59` status `ready` deltaP `13.1238` edge `0.4333` maxDD `-15.4056`
- `market_context_high->equity_24h` score `2.433` n `147` status `ready` deltaP `23.1434` edge `0.6385` maxDD `-24.4698`
- `risk_on_high->crypto_alt_24h` score `1.8487` n `107` status `ready` deltaP `19.3471` edge `0.7984` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `1.8487` n `107` status `ready` deltaP `19.3471` edge `0.7984` maxDD `-42.8959`
- `news_risk_high->crypto_alt_24h` score `1.8198` n `59` status `ready` deltaP `19.2679` edge `0.3983` maxDD `-19.4761`
- `news_risk_high->commodity_4h` score `0.2427` n `67` status `ready` deltaP `5.795` edge `0.0284` maxDD `-0.8733`
- `risk_on_high->index_4h` score `0.1388` n `107` status `ready` deltaP `20.783` edge `0.0123` maxDD `-3.6448`
- `risk_on_and_context->index_4h` score `0.1388` n `107` status `ready` deltaP `20.783` edge `0.0123` maxDD `-3.6448`
- `risk_on_high->index_1h` score `0.1337` n `107` status `ready` deltaP `8.5427` edge `0.0047` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.1337` n `107` status `ready` deltaP `8.5427` edge `0.0047` maxDD `-0.5605`
- `news_risk_high->index_1h` score `0.0333` n `67` status `ready` deltaP `5.8227` edge `0.0008` maxDD `-0.8275`
- `market_context_high->crypto_alt_24h` score `-0.0045` n `147` status `ready` deltaP `13.3645` edge `0.6602` maxDD `-46.3234`
- `risk_on_high->metal_1h` score `-0.0746` n `107` status `ready` deltaP `9.5501` edge `-0.002` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `-0.0746` n `107` status `ready` deltaP `9.5501` edge `-0.002` maxDD `-1.699`
- `risk_on_high->equity_1h` score `-0.1463` n `107` status `ready` deltaP `7.4179` edge `0.0145` maxDD `-2.2834`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
