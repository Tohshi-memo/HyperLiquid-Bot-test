# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T01:07:19.958872+00:00`
- Price records: `672`
- Market context records: `2299`
- Flow alert records: `8509`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9289`

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

- `news_risk_high->crypto_alt_24h` score `20.6077` n `43` status `ready` deltaP `50.0363` edge `1.4426` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `15.6254` n `43` status `ready` deltaP `40.5563` edge `1.0757` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `13.5727` n `43` status `ready` deltaP `29.7925` edge `0.9639` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.3646` n `43` status `ready` deltaP `19.7674` edge `0.79` maxDD `-3.3119`
- `market_context_high->crypto_alt_4h` score `7.5841` n `159` status `ready` deltaP `24.766` edge `0.7348` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `7.5691` n `159` status `ready` deltaP `29.5885` edge `0.6145` maxDD `-10.1468`
- `market_context_high->unknown_24h` score `7.3274` n `115` status `ready` deltaP `24.1168` edge `0.491` maxDD `-1.626`
- `news_risk_high->unknown_24h` score `6.8909` n `43` status `ready` deltaP `28.1613` edge `0.4091` maxDD `-1.4744`
- `market_context_high->unknown_4h` score `5.6154` n `159` status `ready` deltaP `22.3079` edge `0.3802` maxDD `-1.8773`
- `market_context_high->crypto_major_24h` score `5.0154` n `115` status `ready` deltaP `13.4783` edge `0.9424` maxDD `-25.1408`
- `news_risk_high->commodity_4h` score `3.8923` n `43` status `ready` deltaP `32.6148` edge `0.3487` maxDD `-3.0367`
- `news_risk_high->index_24h` score `3.7214` n `43` status `ready` deltaP `11.5351` edge `0.2751` maxDD `-1.3507`
- `news_risk_high->fx_24h` score `3.4299` n `43` status `ready` deltaP `36.0142` edge `0.0642` maxDD `-0.1442`
- `market_context_high->index_24h` score `3.3317` n `115` status `ready` deltaP `13.3349` edge `0.2405` maxDD `-1.4737`
- `news_risk_high->commodity_24h` score `3.2334` n `43` status `ready` deltaP `4.4614` edge `0.3214` maxDD `-3.202`
- `market_context_high->index_4h` score `2.2589` n `159` status `ready` deltaP `22.024` edge `0.124` maxDD `-2.2732`
- `news_risk_high->fx_4h` score `2.2318` n `43` status `ready` deltaP `28.3465` edge `0.0154` maxDD `-0.1382`
- `market_context_high->crypto_alt_1h` score `2.0522` n `159` status `ready` deltaP `13.0729` edge `0.2026` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `1.8268` n `159` status `ready` deltaP `13.3723` edge `0.1825` maxDD `-4.2199`
- `market_context_high->equity_4h` score `1.7943` n `159` status `ready` deltaP `16.5555` edge `0.1796` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
