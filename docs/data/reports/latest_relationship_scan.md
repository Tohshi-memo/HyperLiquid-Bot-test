# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T07:07:16.942837+00:00`
- Price records: `672`
- Market context records: `1094`
- Flow alert records: `5055`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8686`

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

- `market_context_high->crypto_major_24h` score `16.56` n `150` status `ready` deltaP `35.9931` edge `1.1864` maxDD `-3.3749`
- `market_context_high->equity_24h` score `6.0208` n `150` status `ready` deltaP `15.4791` edge `0.4482` maxDD `-3.6396`
- `market_context_high->crypto_alt_24h` score `5.7571` n `150` status `ready` deltaP `12.3541` edge `0.5208` maxDD `-9.5387`
- `market_context_high->metal_24h` score `5.1412` n `150` status `ready` deltaP `-3.2777` edge `0.617` maxDD `-6.3373`
- `market_context_high->index_24h` score `4.7745` n `150` status `ready` deltaP `15.1319` edge `0.3278` maxDD `-2.1308`
- `market_context_high->equity_4h` score `2.1641` n `164` status `ready` deltaP `11.8902` edge `0.1674` maxDD `-3.6396`
- `market_context_high->index_4h` score `1.1549` n `164` status `ready` deltaP `9.7561` edge `0.0995` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.5876` n `168` status `ready` deltaP `8.3939` edge `0.0247` maxDD `-0.5353`
- `market_context_high->crypto_major_4h` score `0.4918` n `164` status `ready` deltaP `9.2988` edge `0.15` maxDD `-6.6806`
- `market_context_high->equity_1h` score `0.4359` n `168` status `ready` deltaP `3.329` edge `0.0519` maxDD `-1.3546`
- `market_context_high->fx_1h` score `0.1376` n `168` status `ready` deltaP `8.3155` edge `0.0016` maxDD `-0.3124`
- `market_context_high->crypto_major_1h` score `0.0765` n `168` status `ready` deltaP `7.2819` edge `0.0344` maxDD `-4.1256`
- `market_context_high->metal_1h` score `-0.0613` n `168` status `ready` deltaP `7.6989` edge `0.0046` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.3185` n `168` status `ready` deltaP `2.6447` edge `0.0401` maxDD `-3.4088`
- `market_context_high->fx_4h` score `-0.6197` n `164` status `ready` deltaP `2.7439` edge `0.0019` maxDD `-1.6381`
- `market_context_high->crypto_alt_4h` score `-0.7026` n `164` status `ready` deltaP `5.6403` edge `0.133` maxDD `-13.854`
- `market_context_high->commodity_1h` score `-0.7684` n `168` status `ready` deltaP `-1.775` edge `-0.0059` maxDD `-3.7959`
- `market_context_high->metal_4h` score `-2.2247` n `164` status `ready` deltaP `7.622` edge `-0.0408` maxDD `-9.2991`
- `market_context_high->unknown_4h` score `-2.2352` n `164` status `ready` deltaP `10.2134` edge `-0.1327` maxDD `-6.7322`
- `market_context_high->commodity_4h` score `-3.1183` n `164` status `ready` deltaP `-10.5183` edge `-0.0129` maxDD `-13.0076`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
