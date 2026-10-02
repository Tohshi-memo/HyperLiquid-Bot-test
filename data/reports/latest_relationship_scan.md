# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T01:07:33.304956+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6602`

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

- `market_context_high->unknown_1h` score `338.6712` n `50` status `ready` deltaP `9.6766` edge `28.163` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `287.5421` n `50` status `ready` deltaP `8.8415` edge `23.9029` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.2464` n `82` status `ready` deltaP `38.0124` edge `1.3714` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `10.8825` n `50` status `ready` deltaP `35.8194` edge `0.8097` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `7.2113` n `50` status `ready` deltaP `18.7622` edge `0.5462` maxDD `-3.294`
- `market_context_high->crypto_alt_24h` score `6.9502` n `50` status `ready` deltaP `14.4514` edge `0.6538` maxDD `-11.6768`
- `market_context_high->crypto_alt_4h` score `4.9452` n `50` status `ready` deltaP `16.189` edge `0.4335` maxDD `-7.6792`
- `market_context_high->equity_24h` score `3.5816` n `50` status `ready` deltaP `18.5208` edge `0.5219` maxDD `-11.8957`
- `news_risk_high->crypto_major_24h` score `3.3438` n `82` status `ready` deltaP `14.795` edge `0.4954` maxDD `-15.8971`
- `market_context_high->crypto_major_1h` score `3.0479` n `50` status `ready` deltaP `14.8982` edge `0.1997` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `2.953` n `50` status `ready` deltaP `13.7545` edge `0.2207` maxDD `-3.6387`
- `market_context_high->fx_4h` score `2.9179` n `50` status `ready` deltaP `32.8415` edge `0.0377` maxDD `-0.0791`
- `news_risk_high->crypto_alt_4h` score `2.8775` n `95` status `ready` deltaP `11.4522` edge `0.2978` maxDD `-6.4152`
- `news_risk_high->equity_4h` score `2.7141` n `95` status `ready` deltaP `24.2506` edge `0.1341` maxDD `-2.9013`
- `news_risk_high->equity_24h` score `2.4693` n `82` status `ready` deltaP `16.3745` edge `0.424` maxDD `-8.9931`
- `news_risk_high->commodity_24h` score `1.7442` n `82` status `ready` deltaP `27.4983` edge `0.1527` maxDD `-3.9922`
- `news_risk_high->metal_24h` score `1.5091` n `82` status `ready` deltaP `15.9553` edge `0.2145` maxDD `-2.192`
- `market_context_high->fx_1h` score `1.4472` n `50` status `ready` deltaP `20.3413` edge `0.0114` maxDD `-0.113`
- `news_risk_high->index_24h` score `1.4021` n `82` status `ready` deltaP `17.9624` edge `0.0449` maxDD `-0.4916`
- `market_context_high->index_24h` score `0.9206` n `50` status `ready` deltaP `14.7917` edge `0.0765` maxDD `-1.2338`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
