# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T08:22:14.598285+00:00`
- Price records: `672`
- Market context records: `1202`
- Flow alert records: `5366`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8768`

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

- `market_context_high->crypto_major_24h` score `18.5501` n `134` status `ready` deltaP `44.2553` edge `1.364` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `7.5202` n `134` status `ready` deltaP `22.0668` edge `0.6812` maxDD `-15.1306`
- `market_context_high->unknown_4h` score `5.6405` n `134` status `ready` deltaP `3.8837` edge `0.5658` maxDD `-6.7322`
- `market_context_high->metal_24h` score `4.3798` n `134` status `ready` deltaP `-3.9153` edge `0.5578` maxDD `-6.3373`
- `market_context_high->commodity_24h` score `3.1445` n `134` status `ready` deltaP `-3.7028` edge `0.5747` maxDD `-18.0378`
- `market_context_high->equity_4h` score `2.7887` n `134` status `ready` deltaP `14.5682` edge `0.2016` maxDD `-3.6396`
- `market_context_high->index_24h` score `2.1725` n `134` status `ready` deltaP `17.1564` edge `0.1753` maxDD `-5.3574`
- `market_context_high->equity_24h` score `1.7099` n `134` status `ready` deltaP `17.4` edge `0.3359` maxDD `-14.2815`
- `market_context_high->index_4h` score `0.9326` n `134` status `ready` deltaP `10.4273` edge `0.0765` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.4784` n `134` status `ready` deltaP `8.3184` edge `0.0161` maxDD `-0.5353`
- `market_context_high->fx_24h` score `0.3882` n `134` status `ready` deltaP `8.4965` edge `0.0516` maxDD `-2.7379`
- `market_context_high->equity_1h` score `0.3563` n `134` status `ready` deltaP `3.8341` edge `0.0419` maxDD `-1.3546`
- `market_context_high->crypto_major_4h` score `-0.0925` n `134` status `ready` deltaP `6.4593` edge `0.1372` maxDD `-8.3693`
- `market_context_high->fx_1h` score `-0.149` n `134` status `ready` deltaP `4.9133` edge `0.0004` maxDD `-0.3124`
- `market_context_high->metal_1h` score `-0.213` n `134` status `ready` deltaP `8.3386` edge `-0.0123` maxDD `-2.2164`
- `market_context_high->crypto_major_1h` score `-0.3543` n `134` status `ready` deltaP `3.4275` edge `0.0083` maxDD `-4.1256`
- `market_context_high->crypto_alt_1h` score `-0.3714` n `134` status `ready` deltaP `0.7284` edge `0.0318` maxDD `-3.4088`
- `market_context_high->unknown_24h` score `-0.4029` n `134` status `ready` deltaP `1.4382` edge `0.2298` maxDD `-10.1706`
- `market_context_high->commodity_1h` score `-0.8172` n `134` status `ready` deltaP `-2.6879` edge `0.0113` maxDD `-2.252`
- `market_context_high->metal_4h` score `-0.9759` n `134` status `ready` deltaP `8.3067` edge `-0.0374` maxDD `-6.4478`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
