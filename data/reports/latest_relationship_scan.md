# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T03:08:01.788389+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6255`

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

- `market_context_high->unknown_24h` score `5062.3682` n `70` status `ready` deltaP `-3.9236` edge `421.9151` maxDD `-0.9938`
- `market_context_high->unknown_4h` score `225.7694` n `70` status `ready` deltaP `0.6315` edge `18.8232` maxDD `-0.3966`
- `news_risk_high->unknown_1h` score `81.4876` n `108` status `ready` deltaP `-5.0454` edge `6.8529` maxDD `-0.9571`
- `news_risk_high->crypto_alt_24h` score `14.6545` n `92` status `ready` deltaP `35.0921` edge `1.1046` maxDD `-6.3871`
- `market_context_high->equity_24h` score `14.5804` n `70` status `ready` deltaP `28.1846` edge `1.1938` maxDD `-8.3331`
- `market_context_high->index_24h` score `5.771` n `70` status `ready` deltaP `49.8958` edge `0.1661` maxDD `-0.0926`
- `news_risk_high->crypto_alt_4h` score `5.456` n `108` status `ready` deltaP `20.7317` edge `0.4551` maxDD `-7.4246`
- `market_context_high->commodity_4h` score `2.8317` n `70` status `ready` deltaP `28.0009` edge `0.0827` maxDD `-0.3387`
- `market_context_high->metal_4h` score `1.3406` n `70` status `ready` deltaP `16.5156` edge `0.0441` maxDD `-0.7323`
- `market_context_high->commodity_24h` score `1.1136` n `70` status `ready` deltaP `28.9087` edge `0.1268` maxDD `-9.1406`
- `news_risk_high->crypto_alt_1h` score `0.8888` n `108` status `ready` deltaP `9.1761` edge `0.1083` maxDD `-3.9659`
- `market_context_high->metal_1h` score `0.7752` n `70` status `ready` deltaP `10.8169` edge `0.0215` maxDD `-0.3209`
- `market_context_high->fx_1h` score `0.6403` n `70` status `ready` deltaP `15.0471` edge `0.0002` maxDD `-0.1407`
- `market_context_high->equity_4h` score `0.5785` n `70` status `ready` deltaP `-3.9808` edge `0.2118` maxDD `-3.8876`
- `market_context_high->fx_4h` score `0.365` n `70` status `ready` deltaP `10.1132` edge `0.0021` maxDD `-0.1285`
- `market_context_high->equity_1h` score `0.2795` n `70` status `ready` deltaP `0.5988` edge `0.1194` maxDD `-2.3383`
- `market_context_high->crypto_major_1h` score `-0.1557` n `70` status `ready` deltaP `2.4765` edge `0.0663` maxDD `-5.2213`
- `market_context_high->commodity_1h` score `-0.2711` n `70` status `ready` deltaP `1.4157` edge `0.0194` maxDD `-0.4475`
- `market_context_high->crypto_major_4h` score `-0.3233` n `70` status `ready` deltaP `14.1899` edge `0.0792` maxDD `-11.886`
- `market_context_high->index_1h` score `-0.5592` n `70` status `ready` deltaP `-2.5577` edge `0.0012` maxDD `-1.1344`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
