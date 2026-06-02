# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T17:37:24.743484+00:00`
- Price records: `672`
- Market context records: `2684`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9250`

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

- `market_context_high->crypto_alt_24h` score `9.2489` n `111` status `ready` deltaP `16.0051` edge `1.0134` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.7043` n `111` status `ready` deltaP `17.652` edge `0.6405` maxDD `-1.626`
- `market_context_high->unknown_4h` score `1.2323` n `134` status `ready` deltaP `6.5799` edge `0.1638` maxDD `-3.7312`
- `market_context_high->crypto_alt_4h` score `1.0149` n `134` status `ready` deltaP `18.4952` edge `0.3177` maxDD `-22.5139`
- `market_context_high->index_4h` score `0.252` n `134` status `ready` deltaP `10.673` edge `0.034` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1438` n `141` status `ready` deltaP `3.1448` edge `0.01` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.1519` n `141` status `ready` deltaP `2.9632` edge `0.0404` maxDD `-3.1587`
- `market_context_high->fx_24h` score `-0.3351` n `111` status `ready` deltaP `9.0841` edge `-0.0013` maxDD `-0.6418`
- `market_context_high->commodity_1h` score `-0.4268` n `141` status `ready` deltaP `1.9227` edge `0.0078` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.4416` n `141` status `ready` deltaP `0.5362` edge `0.004` maxDD `-0.2164`
- `market_context_high->crypto_alt_1h` score `-0.5284` n `141` status `ready` deltaP `6.5486` edge `0.0646` maxDD `-10.747`
- `market_context_high->commodity_24h` score `-0.5784` n `111` status `ready` deltaP `7.7891` edge `0.1833` maxDD `-12.4171`
- `market_context_high->fx_4h` score `-0.6211` n `134` status `ready` deltaP `0.2571` edge `0.0119` maxDD `-0.5631`
- `market_context_high->index_24h` score `-0.663` n `111` status `ready` deltaP `5.0582` edge `0.0091` maxDD `-2.5127`
- `market_context_high->metal_1h` score `-0.7951` n `141` status `ready` deltaP `-2.0332` edge `-0.0055` maxDD `-2.9635`
- `market_context_high->crypto_major_4h` score `-0.9816` n `134` status `ready` deltaP `6.7801` edge `0.1614` maxDD `-22.2624`
- `market_context_high->crypto_major_1h` score `-0.9898` n `141` status `ready` deltaP `3.562` edge `0.0363` maxDD `-9.622`
- `market_context_high->crypto_major_24h` score `-1.1427` n `111` status `ready` deltaP `5.9967` edge `0.5698` maxDD `-44.169`
- `market_context_high->commodity_4h` score `-1.154` n `134` status `ready` deltaP `3.8201` edge `0.0186` maxDD `-10.0279`
- `market_context_high->equity_1h` score `-1.1572` n `141` status `ready` deltaP `-4.0015` edge `0.0141` maxDD `-2.7085`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
