# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T04:37:29.126286+00:00`
- Price records: `672`
- Market context records: `5420`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11474`

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

- `market_context_high->crypto_major_24h` score `3.9161` n `191` status `ready` deltaP `19.4653` edge `0.6506` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `3.8497` n `202` status `ready` deltaP `16.4936` edge `0.4401` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `3.0012` n `202` status `ready` deltaP `11.9219` edge `0.3347` maxDD `-9.46`
- `market_context_high->equity_4h` score `2.4962` n `202` status `ready` deltaP `12.2977` edge `0.2899` maxDD `-7.4425`
- `market_context_high->equity_24h` score `1.986` n `191` status `ready` deltaP `9.2714` edge `0.5431` maxDD `-28.4861`
- `market_context_high->equity_1h` score `0.4263` n `202` status `ready` deltaP `7.943` edge `0.0791` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.1243` n `202` status `ready` deltaP `6.5853` edge `0.0158` maxDD `-0.9472`
- `market_context_high->fx_24h` score `0.0681` n `191` status `ready` deltaP `9.4368` edge `0.0323` maxDD `-0.8294`
- `market_context_high->crypto_major_1h` score `-0.1872` n `202` status `ready` deltaP `3.5928` edge `0.085` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `-0.248` n `202` status `ready` deltaP `1.1976` edge `0.0675` maxDD `-5.0257`
- `market_context_high->fx_1h` score `-0.3952` n `202` status `ready` deltaP `-0.2075` edge `-0.0004` maxDD `-0.577`
- `market_context_high->metal_1h` score `-0.5571` n `202` status `ready` deltaP `1.4392` edge `0.0115` maxDD `-2.0682`
- `market_context_high->index_4h` score `-0.9924` n `202` status `ready` deltaP `6.0191` edge `0.0381` maxDD `-2.874`
- `market_context_high->fx_4h` score `-1.206` n `202` status `ready` deltaP `0.0317` edge `0.0018` maxDD `-1.5345`
- `market_context_high->commodity_1h` score `-1.4683` n `202` status `ready` deltaP `-3.1659` edge `-0.0068` maxDD `-3.5563`
- `market_context_high->index_24h` score `-1.4749` n `191` status `ready` deltaP `13.9043` edge `0.083` maxDD `-12.5551`
- `market_context_high->metal_4h` score `-2.6311` n `202` status `ready` deltaP `-7.5389` edge `-0.0346` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.2477` n `202` status `ready` deltaP `-6.6968` edge `-0.0455` maxDD `-14.1062`
- `market_context_high->crypto_alt_24h` score `-6.4353` n `191` status `ready` deltaP `10.5512` edge `0.2631` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.1942` n `191` status `ready` deltaP `-4.9902` edge `-0.1513` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
