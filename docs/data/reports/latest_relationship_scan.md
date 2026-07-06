# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T05:52:28.445933+00:00`
- Price records: `672`
- Market context records: `5850`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10128`

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

- `news_risk_high->fx_1h` score `1.9878` n `30` status `ready` deltaP `24.0818` edge `0.019` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `0.8862` n `30` status `ready` deltaP `11.6866` edge `0.0824` maxDD `-2.0691`
- `market_context_high->equity_4h` score `0.7359` n `254` status `ready` deltaP `7.8464` edge `0.1548` maxDD `-6.9958`
- `news_risk_high->crypto_alt_1h` score `0.2614` n `30` status `ready` deltaP `5.3194` edge `0.0442` maxDD `-1.6923`
- `market_context_high->fx_1h` score `-0.32` n `254` status `ready` deltaP `1.1422` edge `-0.0001` maxDD `-0.5499`
- `news_risk_high->metal_1h` score `-0.3861` n `30` status `ready` deltaP `1.986` edge `-0.0261` maxDD `-1.2643`
- `market_context_high->equity_1h` score `-0.4554` n `254` status `ready` deltaP `4.1763` edge `0.0349` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.5013` n `254` status `ready` deltaP `3.3771` edge `0.0028` maxDD `-2.0339`
- `market_context_high->commodity_1h` score `-0.5456` n `254` status `ready` deltaP `-1.1481` edge `-0.0022` maxDD `-2.1412`
- `market_context_high->index_1h` score `-0.5799` n `254` status `ready` deltaP `0.9041` edge `0.0044` maxDD `-0.7819`
- `market_context_high->crypto_major_1h` score `-0.8431` n `254` status `ready` deltaP `3.4714` edge `0.0387` maxDD `-6.2348`
- `market_context_high->equity_24h` score `-0.9084` n `226` status `ready` deltaP `17.2643` edge `0.3171` maxDD `-31.6316`
- `market_context_high->crypto_alt_1h` score `-1.0009` n `254` status `ready` deltaP `2.196` edge `0.0354` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.1952` n `254` status `ready` deltaP `0.2401` edge `0.0139` maxDD `-3.165`
- `news_risk_high->index_1h` score `-1.2229` n `30` status `ready` deltaP `-12.2455` edge `-0.0237` maxDD `-1.1161`
- `market_context_high->fx_4h` score `-1.7577` n `254` status `ready` deltaP `-4.1915` edge `-0.0025` maxDD `-2.2593`
- `market_context_high->fx_24h` score `-1.8455` n `226` status `ready` deltaP `4.3787` edge `0.016` maxDD `-5.5435`
- `market_context_high->metal_4h` score `-2.0409` n `254` status `ready` deltaP `-4.2179` edge `-0.0372` maxDD `-8.3735`
- `market_context_high->commodity_4h` score `-2.3568` n `254` status `ready` deltaP `-0.5053` edge `-0.0138` maxDD `-7.0053`
- `market_context_high->crypto_major_4h` score `-2.7447` n `254` status `ready` deltaP `7.3519` edge `0.1595` maxDD `-25.6458`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
