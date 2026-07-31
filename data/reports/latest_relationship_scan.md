# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T23:47:46.350196+00:00`
- Price records: `672`
- Market context records: `8564`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5919`

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

- `news_risk_high->unknown_24h` score `5076.5495` n `61` status `ready` deltaP `39.9704` edge `422.8214` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.8142` n `64` status `ready` deltaP `20.8079` edge `0.4055` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.0922` n `64` status `ready` deltaP `17.4162` edge `0.0773` maxDD `-0.191`
- `market_context_high->crypto_alt_4h` score `2.065` n `62` status `ready` deltaP `14.4276` edge `0.1716` maxDD `-5.323`
- `news_risk_high->equity_1h` score `1.7613` n `64` status `ready` deltaP `16.5513` edge `0.0841` maxDD `-2.4803`
- `news_risk_high->crypto_major_4h` score `1.1399` n `64` status `ready` deltaP `7.9649` edge `0.1706` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.7513` n `64` status `ready` deltaP `14.0244` edge `0.142` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.4874` n `64` status `ready` deltaP `8.561` edge `0.0581` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.396` n `64` status `ready` deltaP `7.5131` edge `0.0519` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.0986` n `64` status `ready` deltaP `5.436` edge `0.0045` maxDD `-0.2475`
- `news_risk_high->fx_4h` score `0.0728` n `64` status `ready` deltaP `11.9284` edge `0.0223` maxDD `-0.6604`
- `news_risk_high->index_1h` score `0.0247` n `64` status `ready` deltaP `3.9203` edge `0.0087` maxDD `-0.5338`
- `news_risk_high->metal_4h` score `-0.0357` n `64` status `ready` deltaP `1.7149` edge `0.0316` maxDD `-0.8085`
- `market_context_high->fx_4h` score `-0.0954` n `62` status `ready` deltaP `8.753` edge `0.0133` maxDD `-1.3685`
- `news_risk_high->metal_1h` score `-0.1096` n `64` status `ready` deltaP `3.5554` edge `0.0075` maxDD `-0.5599`
- `market_context_high->fx_1h` score `-0.2661` n `62` status `ready` deltaP `2.3614` edge `0.0004` maxDD `-0.6874`
- `market_context_high->commodity_1h` score `-0.3473` n `62` status `ready` deltaP `3.559` edge `-0.0057` maxDD `-2.0038`
- `market_context_high->crypto_alt_1h` score `-0.4894` n `62` status `ready` deltaP `-2.4773` edge `0.0165` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.7453` n `62` status `ready` deltaP `0.9465` edge `-0.0155` maxDD `-1.5667`
- `market_context_high->metal_1h` score `-0.9505` n `62` status `ready` deltaP `-2.6946` edge `-0.0118` maxDD `-1.6224`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
