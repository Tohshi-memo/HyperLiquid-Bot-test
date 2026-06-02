# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T12:37:22.800062+00:00`
- Price records: `672`
- Market context records: `2663`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9230`

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

- `market_context_high->crypto_alt_24h` score `8.3822` n `115` status `ready` deltaP `14.6966` edge `0.9499` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.2265` n `115` status `ready` deltaP `17.3505` edge `0.6027` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `4.3895` n `121` status `ready` deltaP `22.4539` edge `0.484` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `2.7899` n `121` status `ready` deltaP `11.8789` edge `0.3343` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `1.1332` n `121` status `ready` deltaP `6.0459` edge `0.1591` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `0.7165` n `133` status `ready` deltaP `8.4969` edge `0.1218` maxDD `-6.1656`
- `market_context_high->index_24h` score `0.1486` n `115` status `ready` deltaP `8.6338` edge `0.0529` maxDD `-2.5127`
- `market_context_high->crypto_major_1h` score `0.1124` n `133` status `ready` deltaP `6.2447` edge `0.0922` maxDD `-4.2199`
- `market_context_high->fx_24h` score `-0.2239` n `115` status `ready` deltaP `9.8445` edge `0.0029` maxDD `-0.6418`
- `market_context_high->index_4h` score `-0.225` n `121` status `ready` deltaP `6.8245` edge `0.0199` maxDD `-2.3986`
- `market_context_high->commodity_1h` score `-0.2721` n `133` status `ready` deltaP `4.132` edge `0.0129` maxDD `-4.3601`
- `market_context_high->unknown_1h` score `-0.2957` n `133` status `ready` deltaP `1.7401` edge `0.0217` maxDD `-1.9684`
- `market_context_high->index_1h` score `-0.3259` n `133` status `ready` deltaP `2.0463` edge `0.0086` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.5523` n `133` status `ready` deltaP `-0.8183` edge `0.0038` maxDD `-0.2164`
- `market_context_high->metal_4h` score `-0.561` n `121` status `ready` deltaP `2.8762` edge `0.0157` maxDD `-2.5301`
- `market_context_high->metal_1h` score `-0.5649` n `133` status `ready` deltaP `-0.6787` edge `0.0015` maxDD `-1.8854`
- `market_context_high->fx_4h` score `-0.6324` n `121` status `ready` deltaP `-0.0037` edge `0.0127` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.1571` n `121` status `ready` deltaP `3.9999` edge `0.017` maxDD `-10.0279`
- `market_context_high->equity_1h` score `-1.3085` n `133` status `ready` deltaP `-4.993` edge `0.0081` maxDD `-2.7085`
- `market_context_high->commodity_24h` score `-1.4374` n `115` status `ready` deltaP `5.8318` edge `0.145` maxDD `-17.1199`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
