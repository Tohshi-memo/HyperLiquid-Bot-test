# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T13:10:51.315650+00:00`
- Price records: `672`
- Market context records: `2564`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9198`

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

- `market_context_high->crypto_alt_4h` score `5.7904` n `148` status `ready` deltaP `25.2801` edge `0.5819` maxDD `-15.4319`
- `market_context_high->crypto_major_24h` score `5.0151` n `117` status `ready` deltaP `12.7137` edge `0.5985` maxDD `-15.2264`
- `market_context_high->unknown_24h` score `4.8724` n `117` status `ready` deltaP `19.0438` edge `0.3119` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `3.9384` n `148` status `ready` deltaP `17.3698` edge `0.3934` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `1.5305` n `148` status `ready` deltaP `9.6325` edge `0.1683` maxDD `-3.7312`
- `market_context_high->equity_24h` score `1.3766` n `117` status `ready` deltaP `19.765` edge `0.0413` maxDD `-2.0014`
- `market_context_high->crypto_alt_1h` score `1.3338` n `148` status `ready` deltaP `10.738` edge `0.1583` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `0.7592` n `148` status `ready` deltaP `8.7878` edge `0.1241` maxDD `-4.2199`
- `market_context_high->index_24h` score `0.6383` n `117` status `ready` deltaP `6.25` edge `0.1096` maxDD `-2.5127`
- `market_context_high->crypto_alt_24h` score `0.2596` n `117` status `ready` deltaP `-0.3873` edge `0.6737` maxDD `-39.0265`
- `market_context_high->index_4h` score `0.1102` n `148` status `ready` deltaP `7.6549` edge `0.0423` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1295` n `148` status `ready` deltaP `4.0662` edge `0.0115` maxDD `-1.2855`
- `market_context_high->commodity_1h` score `-0.4353` n `148` status `ready` deltaP `4.8835` edge `0.019` maxDD `-4.3601`
- `market_context_high->metal_1h` score `-0.4384` n `148` status `ready` deltaP `1.1207` edge `0.0111` maxDD `-2.9823`
- `market_context_high->unknown_1h` score `-0.495` n `148` status `ready` deltaP `1.3595` edge `0.0187` maxDD `-2.8543`
- `market_context_high->fx_1h` score `-0.5554` n `148` status `ready` deltaP `0.4491` edge `0.0042` maxDD `-0.278`
- `market_context_high->equity_1h` score `-0.7113` n `148` status `ready` deltaP `0.4775` edge `0.0214` maxDD `-2.7085`
- `market_context_high->fx_24h` score `-0.7114` n `117` status `ready` deltaP `1.1485` edge `0.0036` maxDD `-1.8634`
- `market_context_high->fx_4h` score `-0.8463` n `148` status `ready` deltaP `0.412` edge `0.0127` maxDD `-0.8774`
- `market_context_high->metal_4h` score `-0.9074` n `148` status `ready` deltaP `3.3949` edge `0.0405` maxDD `-4.7664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
