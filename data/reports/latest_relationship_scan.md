# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-01T13:07:26.605477+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11487`

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

- `risk_on_high->unknown_4h` score `7.2941` n `107` status `ready` deltaP `20.5252` edge `0.5328` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.2941` n `107` status `ready` deltaP `20.5252` edge `0.5328` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `5.8407` n `151` status `ready` deltaP `16.8178` edge `0.4441` maxDD `-2.5597`
- `risk_on_high->unknown_1h` score `2.1754` n `107` status `ready` deltaP `4.7191` edge `0.2075` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `2.1754` n `107` status `ready` deltaP `4.7191` edge `0.2075` maxDD `-1.9475`
- `market_context_high->unknown_1h` score `2.0446` n `151` status `ready` deltaP `4.0816` edge `0.2062` maxDD `-2.042`
- `news_risk_high->unknown_1h` score `1.4651` n `59` status `ready` deltaP `2.1846` edge `0.1422` maxDD `-1.1072`
- `risk_on_high->commodity_24h` score `0.317` n `107` status `ready` deltaP `7.2171` edge `0.0771` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `0.317` n `107` status `ready` deltaP `7.2171` edge `0.0771` maxDD `-0.5706`
- `news_risk_high->fx_4h` score `0.0977` n `59` status `ready` deltaP `10.03` edge `0.0006` maxDD `-0.7461`
- `risk_on_high->index_1h` score `0.0963` n `107` status `ready` deltaP `8.0936` edge `0.0029` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.0963` n `107` status `ready` deltaP `8.0936` edge `0.0029` maxDD `-0.5605`
- `news_risk_high->commodity_24h` score `0.0688` n `59` status `ready` deltaP `4.049` edge `-0.002` maxDD `-0.2074`
- `market_context_high->commodity_1h` score `-0.0182` n `151` status `ready` deltaP `7.8241` edge `0.0113` maxDD `-1.5315`
- `risk_on_high->metal_1h` score `-0.0302` n `107` status `ready` deltaP `10.1489` edge `-0.0003` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `-0.0302` n `107` status `ready` deltaP `10.1489` edge `-0.0003` maxDD `-1.699`
- `risk_on_high->commodity_1h` score `-0.0851` n `107` status `ready` deltaP `4.7233` edge `0.0098` maxDD `-0.8428`
- `risk_on_and_context->commodity_1h` score `-0.0851` n `107` status `ready` deltaP `4.7233` edge `0.0098` maxDD `-0.8428`
- `news_risk_high->commodity_4h` score `-0.0893` n `59` status `ready` deltaP `2.0049` edge `0.0111` maxDD `-0.8733`
- `risk_on_high->index_4h` score `-0.1035` n `107` status `ready` deltaP `17.4294` edge `0.0036` maxDD `-3.6448`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
