# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T11:07:27.844187+00:00`
- Price records: `672`
- Market context records: `5448`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11438`

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

- `market_context_high->equity_24h` score `3.5005` n `186` status `ready` deltaP `11.4248` edge `0.5978` maxDD `-23.5803`
- `market_context_high->crypto_major_24h` score `3.1584` n `186` status `ready` deltaP `17.3891` edge `0.6013` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `3.1057` n `196` status `ready` deltaP `15.6981` edge `0.3834` maxDD `-14.0065`
- `market_context_high->equity_4h` score `2.6276` n `196` status `ready` deltaP `12.8142` edge `0.2974` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `2.3743` n `196` status `ready` deltaP `10.761` edge `0.2902` maxDD `-9.46`
- `market_context_high->equity_1h` score `0.5255` n `199` status `ready` deltaP `8.3125` edge `0.0849` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.2897` n `186` status `ready` deltaP `11.6208` edge `0.0362` maxDD `-0.8294`
- `market_context_high->index_1h` score `0.157` n `199` status `ready` deltaP `6.7839` edge `0.0172` maxDD `-0.9472`
- `market_context_high->metal_1h` score `-0.3013` n `199` status `ready` deltaP `3.662` edge `0.018` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.3057` n `199` status `ready` deltaP `1.1066` edge `0.0633` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.4075` n `199` status `ready` deltaP `2.2936` edge `0.0753` maxDD `-6.9639`
- `market_context_high->fx_1h` score `-0.5908` n `199` status `ready` deltaP `-0.0376` edge `-0.0001` maxDD `-0.577`
- `market_context_high->index_4h` score `-0.7965` n `196` status `ready` deltaP `7.6873` edge `0.0433` maxDD `-2.874`
- `market_context_high->index_24h` score `-0.8776` n `186` status `ready` deltaP `15.7762` edge `0.0922` maxDD `-13.1248`
- `market_context_high->fx_4h` score `-1.1162` n `196` status `ready` deltaP `0.8991` edge `0.0035` maxDD `-1.5345`
- `market_context_high->commodity_1h` score `-1.4164` n `199` status `ready` deltaP `-2.5712` edge `-0.0061` maxDD `-3.5831`
- `market_context_high->metal_4h` score `-2.6467` n `196` status `ready` deltaP `-8.2753` edge `-0.0317` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.2661` n `196` status `ready` deltaP `-6.8224` edge `-0.0462` maxDD `-14.1062`
- `market_context_high->metal_24h` score `-7.444` n `186` status `ready` deltaP `-5.4603` edge `-0.1802` maxDD `-33.021`
- `market_context_high->crypto_alt_24h` score `-7.5189` n `186` status `ready` deltaP `8.1653` edge `0.1887` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
