# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T20:22:26.975956+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11621`

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

- `market_context_high->crypto_major_24h` score `2.7309` n `91` status `ready` deltaP `10.0294` edge `0.2815` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `1.6475` n `91` status `ready` deltaP `19.1163` edge `0.2671` maxDD `-4.666`
- `market_context_high->equity_1h` score `1.3143` n `96` status `ready` deltaP `10.8097` edge `0.0676` maxDD `-0.4112`
- `market_context_high->equity_4h` score `0.9559` n `96` status `ready` deltaP `5.9705` edge `0.1287` maxDD `-2.4411`
- `market_context_high->metal_4h` score `0.8881` n `96` status `ready` deltaP `15.1931` edge `0.0303` maxDD `-1.273`
- `market_context_high->index_1h` score `0.7102` n `96` status `ready` deltaP `13.367` edge `0.0088` maxDD `-0.0982`
- `market_context_high->crypto_major_4h` score `0.6648` n `96` status `ready` deltaP `8.7144` edge `0.0994` maxDD `-3.1677`
- `market_context_high->unknown_1h` score `0.5322` n `96` status `ready` deltaP `9.8054` edge `0.0017` maxDD `-0.4843`
- `market_context_high->crypto_alt_4h` score `0.162` n `96` status `ready` deltaP `9.2988` edge `0.0785` maxDD `-5.4926`
- `market_context_high->unknown_24h` score `0.0424` n `91` status `ready` deltaP `14.4765` edge `-0.0716` maxDD `-0.3771`
- `market_context_high->metal_1h` score `0.0374` n `96` status `ready` deltaP `4.7717` edge `0.01` maxDD `-0.4291`
- `market_context_high->fx_4h` score `-0.202` n `96` status `ready` deltaP `3.6839` edge `-0.0002` maxDD `-0.3539`
- `market_context_high->crypto_alt_1h` score `-0.405` n `96` status `ready` deltaP `2.2268` edge `0.0134` maxDD `-2.413`
- `market_context_high->index_4h` score `-0.4234` n `96` status `ready` deltaP `2.312` edge `0.0148` maxDD `-0.5728`
- `market_context_high->fx_1h` score `-0.4397` n `96` status `ready` deltaP `-3.2685` edge `0.0013` maxDD `-0.2043`
- `market_context_high->commodity_4h` score `-0.4619` n `96` status `ready` deltaP `2.5661` edge `0.0087` maxDD `-2.4692`
- `market_context_high->crypto_major_1h` score `-0.5208` n `96` status `ready` deltaP `0.736` edge `0.0128` maxDD `-2.7581`
- `market_context_high->commodity_1h` score `-0.8806` n `96` status `ready` deltaP `-7.5911` edge `-0.0057` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-2.0758` n `91` status `ready` deltaP `-5.0652` edge `0.0447` maxDD `-8.831`
- `market_context_high->fx_24h` score `-4.289` n `91` status `ready` deltaP `-27.0395` edge `-0.0272` maxDD `-1.3293`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
