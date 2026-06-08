# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-08T02:06:32.762265+00:00`
- Price records: `672`
- Market context records: `3238`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9724`

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

- `market_context_high->crypto_alt_24h` score `14.3668` n `103` status `ready` deltaP `18.9977` edge `2.6994` maxDD `-70.3986`
- `market_context_high->commodity_24h` score `13.7382` n `103` status `ready` deltaP `49.5567` edge `0.8573` maxDD `-2.0927`
- `market_context_high->index_24h` score `9.6949` n `103` status `ready` deltaP `32.1838` edge `0.8488` maxDD `-16.1026`
- `market_context_high->equity_24h` score `6.6698` n `103` status `ready` deltaP `19.7428` edge `1.5651` maxDD `-53.663`
- `market_context_high->crypto_major_24h` score `2.6994` n `103` status `ready` deltaP `23.0684` edge `2.2622` maxDD `-152.2601`
- `risk_on_high->crypto_major_1h` score `2.6305` n `31` status `ready` deltaP `10.8267` edge `0.372` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `2.6305` n `31` status `ready` deltaP `10.8267` edge `0.372` maxDD `-5.8885`
- `market_context_high->commodity_4h` score `1.7892` n `136` status `ready` deltaP `16.4276` edge `0.1354` maxDD `-3.9989`
- `risk_on_high->crypto_alt_1h` score `0.7324` n `31` status `ready` deltaP `4.0081` edge `0.2109` maxDD `-8.1649`
- `risk_on_and_context->crypto_alt_1h` score `0.7324` n `31` status `ready` deltaP `4.0081` edge `0.2109` maxDD `-8.1649`
- `risk_on_high->metal_1h` score `0.4873` n `31` status `ready` deltaP `8.2142` edge `0.0762` maxDD `-1.4793`
- `risk_on_and_context->metal_1h` score `0.4873` n `31` status `ready` deltaP `8.2142` edge `0.0762` maxDD `-1.4793`
- `risk_on_high->equity_1h` score `0.3516` n `31` status `ready` deltaP `2.6608` edge `0.1177` maxDD `-3.5625`
- `risk_on_and_context->equity_1h` score `0.3516` n `31` status `ready` deltaP `2.6608` edge `0.1177` maxDD `-3.5625`
- `risk_on_high->index_1h` score `-0.1172` n `31` status `ready` deltaP `0.1835` edge `0.0461` maxDD `-1.3216`
- `risk_on_and_context->index_1h` score `-0.1172` n `31` status `ready` deltaP `0.1835` edge `0.0461` maxDD `-1.3216`
- `market_context_high->commodity_1h` score `-0.3605` n `148` status `ready` deltaP `4.2038` edge `0.0235` maxDD `-2.5251`
- `market_context_high->unknown_4h` score `-0.4403` n `136` status `ready` deltaP `10.3838` edge `0.1009` maxDD `-15.1257`
- `market_context_high->index_1h` score `-0.581` n `148` status `ready` deltaP `3.1478` edge `0.0108` maxDD `-4.5023`
- `risk_on_high->fx_1h` score `-0.8111` n `31` status `ready` deltaP `-11.3724` edge `-0.0047` maxDD `-0.2106`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
