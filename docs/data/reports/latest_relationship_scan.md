# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T11:52:17.236988+00:00`
- Price records: `672`
- Market context records: `1009`
- Flow alert records: `4813`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8634`

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

- `market_context_high->crypto_major_24h` score `13.1476` n `203` status `ready` deltaP `32.1132` edge `0.9404` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.1722` n `203` status `ready` deltaP `10.9929` edge `0.3978` maxDD `-9.5387`
- `market_context_high->index_24h` score `-0.255` n `203` status `ready` deltaP `4.6575` edge `0.14` maxDD `-5.384`
- `market_context_high->fx_1h` score `-0.3616` n `203` status `ready` deltaP `1.7728` edge `-0.0001` maxDD `-0.3124`
- `market_context_high->commodity_1h` score `-0.5635` n `203` status `ready` deltaP `2.4483` edge `0.0175` maxDD `-3.7959`
- `market_context_high->fx_4h` score `-0.6891` n `203` status `ready` deltaP `1.4545` edge `0.0016` maxDD `-1.6381`
- `market_context_high->index_1h` score `-0.7305` n `203` status `ready` deltaP `2.817` edge `0.0057` maxDD `-2.8282`
- `market_context_high->equity_24h` score `-0.7397` n `203` status `ready` deltaP `4.9638` edge `0.1553` maxDD `-10.3358`
- `market_context_high->equity_1h` score `-0.7405` n `203` status `ready` deltaP `-0.2014` edge `0.0165` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.2499` n `203` status `ready` deltaP `4.598` edge `-0.0186` maxDD `-11.4508`
- `market_context_high->crypto_alt_1h` score `-1.3861` n `203` status `ready` deltaP `-1.5206` edge `-0.0236` maxDD `-8.1842`
- `market_context_high->equity_4h` score `-1.5262` n `203` status `ready` deltaP `1.2488` edge `0.0797` maxDD `-10.5498`
- `market_context_high->index_4h` score `-1.7357` n `203` status `ready` deltaP `-1.7421` edge `0.0188` maxDD `-6.4794`
- `market_context_high->metal_1h` score `-1.8258` n `203` status `ready` deltaP `0.0826` edge `-0.0387` maxDD `-9.0076`
- `market_context_high->crypto_major_4h` score `-3.0132` n `203` status `ready` deltaP `6.4047` edge `0.0768` maxDD `-22.648`
- `market_context_high->commodity_4h` score `-3.0753` n `203` status `ready` deltaP `-0.8575` edge `0.0662` maxDD `-13.0076`
- `market_context_high->crypto_alt_4h` score `-3.3016` n `203` status `ready` deltaP `-2.1191` edge `0.0168` maxDD `-15.2248`
- `market_context_high->fx_24h` score `-3.4267` n `203` status `ready` deltaP `-0.7362` edge `-0.0218` maxDD `-19.6757`
- `market_context_high->metal_4h` score `-4.5957` n `203` status `ready` deltaP `-4.5371` edge `-0.1661` maxDD `-24.7606`
- `market_context_high->commodity_24h` score `-8.4` n `203` status `ready` deltaP `1.9591` edge `0.3748` maxDD `-102.8492`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
