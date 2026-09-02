# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-02T21:07:37.552184+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11561`

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

- `risk_on_high->equity_24h` score `6.2969` n `107` status `ready` deltaP `27.1742` edge `0.7581` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `6.2969` n `107` status `ready` deltaP `27.1742` edge `0.7581` maxDD `-19.828`
- `risk_on_high->unknown_4h` score `6.2261` n `107` status `ready` deltaP `18.0861` edge `0.4601` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `6.2261` n `107` status `ready` deltaP `18.0861` edge `0.4601` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `4.3068` n `147` status `ready` deltaP `13.8201` edge `0.3363` maxDD `-2.563`
- `news_risk_high->equity_24h` score `3.2971` n `59` status `ready` deltaP `13.1238` edge `0.434` maxDD `-15.4056`
- `market_context_high->equity_24h` score `2.4384` n `147` status `ready` deltaP `23.1434` edge `0.6392` maxDD `-24.4698`
- `risk_on_high->crypto_alt_24h` score `1.8007` n `107` status `ready` deltaP `19.1735` edge `0.7934` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `1.8007` n `107` status `ready` deltaP `19.1735` edge `0.7934` maxDD `-42.8959`
- `news_risk_high->crypto_alt_24h` score `1.7717` n `59` status `ready` deltaP `19.0943` edge `0.3933` maxDD `-19.4761`
- `news_risk_high->commodity_4h` score `0.2419` n `67` status `ready` deltaP `5.795` edge `0.0283` maxDD `-0.8733`
- `risk_on_high->index_4h` score `0.1475` n `107` status `ready` deltaP `20.9355` edge `0.0124` maxDD `-3.6448`
- `risk_on_and_context->index_4h` score `0.1475` n `107` status `ready` deltaP `20.9355` edge `0.0124` maxDD `-3.6448`
- `risk_on_high->index_1h` score `0.133` n `107` status `ready` deltaP `8.5427` edge `0.0046` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.133` n `107` status `ready` deltaP `8.5427` edge `0.0046` maxDD `-0.5605`
- `news_risk_high->index_1h` score `0.0326` n `67` status `ready` deltaP `5.8227` edge `0.0007` maxDD `-0.8275`
- `market_context_high->crypto_alt_24h` score `-0.0525` n `147` status `ready` deltaP `13.1909` edge `0.6552` maxDD `-46.3234`
- `risk_on_high->metal_1h` score `-0.0754` n `107` status `ready` deltaP `9.5501` edge `-0.0021` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `-0.0754` n `107` status `ready` deltaP `9.5501` edge `-0.0021` maxDD `-1.699`
- `risk_on_high->equity_1h` score `-0.1486` n `107` status `ready` deltaP `7.4179` edge `0.0142` maxDD `-2.2834`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
