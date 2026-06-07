# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T10:52:24.066616+00:00`
- Price records: `672`
- Market context records: `3170`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `8854`

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

- `market_context_high->commodity_24h` score `13.8643` n `101` status `ready` deltaP `47.2171` edge `0.8834` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `11.9268` n `101` status `ready` deltaP `20.2643` edge `0.9076` maxDD `-1.9039`
- `market_context_high->crypto_alt_24h` score `11.6925` n `101` status `ready` deltaP `14.9323` edge `2.3971` maxDD `-71.142`
- `market_context_high->index_24h` score `6.1898` n `101` status `ready` deltaP `29.2216` edge `0.8542` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.5705` n `101` status `ready` deltaP `13.497` edge `1.3376` maxDD `-53.663`
- `market_context_high->commodity_4h` score `3.076` n `134` status `ready` deltaP `19.3552` edge `0.1731` maxDD `-1.9973`
- `market_context_high->fx_24h` score `0.7524` n `101` status `ready` deltaP `12.3539` edge `0.0031` maxDD `-0.4876`
- `market_context_high->commodity_1h` score `0.2561` n `135` status `ready` deltaP `4.8148` edge `0.0315` maxDD `-1.7142`
- `market_context_high->unknown_4h` score `0.0138` n `134` status `ready` deltaP `11.0506` edge `0.1497` maxDD `-14.7778`
- `market_context_high->crypto_alt_1h` score `-0.3828` n `135` status `ready` deltaP `6.3118` edge `0.1218` maxDD `-14.7034`
- `market_context_high->index_1h` score `-0.4113` n `135` status `ready` deltaP `5.2717` edge `0.0184` maxDD `-4.5023`
- `market_context_high->index_4h` score `-0.9436` n `134` status `ready` deltaP `15.3189` edge `0.0678` maxDD `-17.6057`
- `market_context_high->crypto_major_1h` score `-1.0323` n `135` status `ready` deltaP `3.2457` edge `0.0723` maxDD `-15.1032`
- `market_context_high->fx_1h` score `-1.0944` n `135` status `ready` deltaP `-9.9767` edge `-0.0054` maxDD `-0.8046`
- `market_context_high->equity_1h` score `-1.3424` n `135` status `ready` deltaP `3.7824` edge `0.0115` maxDD `-8.8863`
- `market_context_high->fx_4h` score `-1.3631` n `134` status `ready` deltaP `-11.8925` edge `-0.007` maxDD `-1.4115`
- `market_context_high->metal_1h` score `-2.0937` n `135` status `ready` deltaP `-3.9166` edge `-0.009` maxDD `-7.4828`
- `market_context_high->crypto_alt_4h` score `-2.1521` n `134` status `ready` deltaP `17.9651` edge `0.4088` maxDD `-58.6918`
- `market_context_high->unknown_1h` score `-2.9996` n `135` status `ready` deltaP `2.8454` edge `-0.0663` maxDD `-14.2111`
- `market_context_high->crypto_major_4h` score `-3.6158` n `134` status `ready` deltaP `11.0553` edge `0.2551` maxDD `-54.3896`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
