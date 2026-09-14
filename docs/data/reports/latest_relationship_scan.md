# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T20:07:33.623073+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10548`

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

- `news_risk_high->unknown_4h` score `396.8648` n `78` status `ready` deltaP `-22.4554` edge `33.3111` maxDD `-4.1464`
- `news_risk_high->unknown_24h` score `24.0655` n `78` status `ready` deltaP `18.9236` edge `1.8793` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `21.9457` n `78` status `ready` deltaP `46.7281` edge `1.5564` maxDD `-1.4626`
- `news_risk_high->crypto_major_24h` score `16.7978` n `78` status `ready` deltaP `34.0011` edge `1.3202` maxDD `-9.098`
- `news_risk_high->equity_24h` score `13.6756` n `78` status `ready` deltaP `41.3461` edge `1.042` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.7255` n `78` status `ready` deltaP `61.9391` edge `0.3318` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.4241` n `78` status `ready` deltaP `37.7938` edge `0.3288` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `6.4135` n `120` status `ready` deltaP `36.4583` edge `0.2914` maxDD `0.0`
- `risk_on_high->commodity_24h` score `5.8987` n `51` status `ready` deltaP `36.4583` edge `0.2485` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.8987` n `51` status `ready` deltaP `36.4583` edge `0.2485` maxDD `0.0`
- `risk_on_high->fx_24h` score `4.5293` n `51` status `ready` deltaP `50.817` edge `0.0429` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `4.5293` n `51` status `ready` deltaP `50.817` edge `0.0429` maxDD `-0.0054`
- `market_context_high->fx_24h` score `4.1585` n `120` status `ready` deltaP `47.7778` edge `0.0496` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.1069` n `52` status `ready` deltaP `27.0521` edge `0.0302` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.1069` n `52` status `ready` deltaP `27.0521` edge `0.0302` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.9072` n `137` status `ready` deltaP `22.462` edge `0.051` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.7814` n `137` status `ready` deltaP `12.812` edge `0.0174` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.625` n `78` status `ready` deltaP `15.7442` edge `0.038` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.266` n `52` status `ready` deltaP `7.1972` edge `0.0094` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.266` n `52` status `ready` deltaP `7.1972` edge `0.0094` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
