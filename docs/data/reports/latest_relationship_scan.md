# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-07T05:07:27.224073+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4184`

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

- `news_risk_high->equity_4h` score `1.1738` n `65` status `ready` deltaP `10.1524` edge `0.1567` maxDD `-4.2454`
- `news_risk_high->index_4h` score `0.8782` n `65` status `ready` deltaP `14.9343` edge `0.0214` maxDD `-0.4888`
- `news_risk_high->index_24h` score `0.3663` n `65` status `ready` deltaP `10.227` edge `0.1456` maxDD `-6.6786`
- `news_risk_high->index_1h` score `0.1194` n `65` status `ready` deltaP `8.5698` edge `0.0035` maxDD `-0.2931`
- `news_risk_high->fx_24h` score `0.0559` n `65` status `ready` deltaP `-1.7521` edge `0.0606` maxDD `-0.2073`
- `news_risk_high->equity_1h` score `-0.0757` n `65` status `ready` deltaP `-0.2787` edge `0.0471` maxDD `-1.396`
- `news_risk_high->fx_4h` score `-0.2262` n `65` status `ready` deltaP `1.7683` edge `0.0038` maxDD `-0.2336`
- `news_risk_high->fx_1h` score `-0.2471` n `65` status `ready` deltaP `0.7439` edge `0.0019` maxDD `-0.0826`
- `news_risk_high->metal_1h` score `-0.4652` n `65` status `ready` deltaP `-2.5656` edge `-0.0068` maxDD `-0.5256`
- `news_risk_high->metal_4h` score `-1.2058` n `65` status `ready` deltaP `-3.4709` edge `-0.0409` maxDD `-1.5773`
- `news_risk_high->crypto_major_4h` score `-1.5054` n `65` status `ready` deltaP `-5.2463` edge `0.0024` maxDD `-8.5004`
- `news_risk_high->commodity_1h` score `-1.7986` n `65` status `ready` deltaP `-12.287` edge `-0.0027` maxDD `-1.2218`
- `news_risk_high->crypto_major_1h` score `-1.962` n `65` status `ready` deltaP `-7.9042` edge `-0.028` maxDD `-3.291`
- `news_risk_high->crypto_alt_1h` score `-2.2133` n `65` status `ready` deltaP `-4.2285` edge `-0.0407` maxDD `-5.2444`
- `news_risk_high->crypto_alt_4h` score `-2.5174` n `65` status `ready` deltaP `-5.5511` edge `-0.0237` maxDD `-13.9624`
- `news_risk_high->metal_24h` score `-3.657` n `65` status `ready` deltaP `-4.0865` edge `-0.252` maxDD `-8.5019`
- `news_risk_high->equity_24h` score `-4.2644` n `65` status `ready` deltaP `22.0086` edge `0.4652` maxDD `-86.0244`
- `news_risk_high->commodity_4h` score `-4.4813` n `65` status `ready` deltaP `-30.7903` edge `-0.0103` maxDD `-3.9631`
- `news_risk_high->commodity_24h` score `-10.4755` n `65` status `ready` deltaP `-29.2629` edge `-0.111` maxDD `-28.0162`
- `news_risk_high->crypto_major_24h` score `-13.7683` n `65` status `ready` deltaP `-28.9102` edge `-0.1043` maxDD `-50.6925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
