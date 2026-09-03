# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T18:47:16.777419+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11685`

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

- `risk_on_high->unknown_4h` score `30.4756` n `133` status `ready` deltaP `12.5046` edge `2.5181` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `30.4756` n `133` status `ready` deltaP `12.5046` edge `2.5181` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `23.7106` n `167` status `ready` deltaP `14.1029` edge `1.9514` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `16.3349` n `133` status `ready` deltaP `1.0422` edge `1.412` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `16.3349` n `133` status `ready` deltaP `1.0422` edge `1.412` maxDD `-1.95`
- `market_context_high->unknown_1h` score `11.8551` n `167` status `ready` deltaP `1.497` edge `1.041` maxDD `-2.0446`
- `market_context_high->equity_24h` score `2.0055` n `127` status `ready` deltaP `18.7336` edge `0.4768` maxDD `-20.7654`
- `news_risk_high->crypto_alt_24h` score `1.6381` n `67` status `ready` deltaP `18.3095` edge `0.3814` maxDD `-19.4761`
- `risk_on_high->equity_24h` score `1.5226` n `107` status `ready` deltaP `13.9798` edge `0.4482` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `1.5226` n `107` status `ready` deltaP `13.9798` edge `0.4482` maxDD `-19.828`
- `news_risk_high->crypto_major_24h` score `1.0209` n `67` status `ready` deltaP `14.8062` edge `0.4705` maxDD `-30.7329`
- `news_risk_high->equity_24h` score `0.7883` n `67` status `ready` deltaP `6.4055` edge `0.3051` maxDD `-15.4056`
- `news_risk_high->commodity_4h` score `0.4308` n `67` status `ready` deltaP `7.7767` edge `0.0393` maxDD `-0.8733`
- `risk_on_high->metal_1h` score `0.0688` n `133` status `ready` deltaP `11.814` edge `0.0013` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0688` n `133` status `ready` deltaP `11.814` edge `0.0013` maxDD `-1.699`
- `news_risk_high->fx_4h` score `0.0617` n `67` status `ready` deltaP `9.9563` edge `0.0044` maxDD `-1.2507`
- `news_risk_high->index_1h` score `-0.085` n `67` status `ready` deltaP `4.176` edge `-0.0034` maxDD `-0.8275`
- `news_risk_high->commodity_1h` score `-0.1011` n `67` status `ready` deltaP `5.206` edge `0.0015` maxDD `-0.9036`
- `risk_on_high->index_1h` score `-0.1232` n `133` status `ready` deltaP `4.5912` edge `-0.0019` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.1232` n `133` status `ready` deltaP `4.5912` edge `-0.0019` maxDD `-0.5605`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
