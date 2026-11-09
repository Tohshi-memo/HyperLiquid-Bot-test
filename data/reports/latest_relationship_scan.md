# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T19:07:32.514859+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `10180`

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

- `market_context_high->equity_24h` score `8.0128` n `40` status `ready` deltaP `15.1863` edge `1.1665` maxDD `-16.9034`
- `market_context_high->index_24h` score `1.4839` n `40` status `ready` deltaP `13.1542` edge `0.1488` maxDD `-2.3671`
- `market_context_high->commodity_24h` score `0.6543` n `40` status `ready` deltaP `-3.6265` edge `0.1668` maxDD `-1.6995`
- `market_context_high->metal_1h` score `-0.3101` n `88` status `ready` deltaP `4.1718` edge `0.014` maxDD `-1.4122`
- `market_context_high->fx_24h` score `-0.4446` n `40` status `ready` deltaP `1.8414` edge `-0.0228` maxDD `-1.0519`
- `market_context_high->commodity_1h` score `-0.607` n `88` status `ready` deltaP `-0.9699` edge `-0.0031` maxDD `-1.7935`
- `market_context_high->index_4h` score `-0.766` n `88` status `ready` deltaP `1.1917` edge `-0.0084` maxDD `-2.4871`
- `market_context_high->commodity_4h` score `-1.006` n `88` status `ready` deltaP `-3.8207` edge `0.0071` maxDD `-4.182`
- `market_context_high->metal_4h` score `-1.0208` n `88` status `ready` deltaP `-0.8267` edge `0.013` maxDD `-4.0688`
- `market_context_high->index_1h` score `-1.0329` n `88` status `ready` deltaP `-8.1787` edge `0.0052` maxDD `-0.9814`
- `market_context_high->fx_1h` score `-1.3224` n `88` status `ready` deltaP `-14.2784` edge `-0.0059` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.6456` n `88` status `ready` deltaP `-7.5808` edge `0.0242` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.9984` n `88` status `ready` deltaP `-0.0459` edge `-0.058` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-2.1057` n `88` status `ready` deltaP `-6.5293` edge `-0.0083` maxDD `-2.4506`
- `market_context_high->metal_24h` score `-2.3859` n `40` status `ready` deltaP `1.3475` edge `-0.1525` maxDD `-1.4245`
- `market_context_high->crypto_major_1h` score `-3.1973` n `88` status `ready` deltaP `-5.1892` edge `-0.113` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-7.2418` n `88` status `ready` deltaP `-2.207` edge `-0.2076` maxDD `-25.16`
- `market_context_high->unknown_4h` score `-7.4924` n `88` status `ready` deltaP `6.5864` edge `-0.6235` maxDD `-0.9153`
- `market_context_high->crypto_alt_24h` score `-7.7691` n `40` status `ready` deltaP `-11.1742` edge `-0.0635` maxDD `-33.4213`
- `market_context_high->crypto_alt_4h` score `-9.4042` n `88` status `ready` deltaP `0.6348` edge `-0.2761` maxDD `-34.2787`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
