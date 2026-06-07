# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T13:37:23.979701+00:00`
- Price records: `672`
- Market context records: `3182`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `8856`

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

- `market_context_high->commodity_24h` score `13.7784` n `104` status `ready` deltaP `47.329` edge `0.8755` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `12.347` n `104` status `ready` deltaP `19.9519` edge `0.9447` maxDD `-1.9039`
- `market_context_high->crypto_alt_24h` score `11.611` n `104` status `ready` deltaP `14.8504` edge `2.3872` maxDD `-71.142`
- `market_context_high->index_24h` score `6.2431` n `104` status `ready` deltaP `30.0213` edge `0.8557` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.5616` n `104` status `ready` deltaP `13.101` edge `1.3391` maxDD `-53.663`
- `market_context_high->commodity_4h` score `3.1114` n `134` status `ready` deltaP `19.8125` edge `0.173` maxDD `-1.9973`
- `market_context_high->unknown_4h` score `0.8604` n `134` status `ready` deltaP `11.508` edge `0.2172` maxDD `-14.7778`
- `market_context_high->fx_24h` score `0.6938` n `104` status `ready` deltaP `11.7121` edge `0.0025` maxDD `-0.4876`
- `market_context_high->commodity_1h` score `0.3456` n `140` status `ready` deltaP `5.9795` edge `0.0312` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.3229` n `140` status `ready` deltaP `6.6125` edge `0.0208` maxDD `-4.5023`
- `market_context_high->crypto_alt_1h` score `-0.465` n `140` status `ready` deltaP `5.9324` edge `0.1138` maxDD `-14.7034`
- `market_context_high->index_4h` score `-0.8199` n `134` status `ready` deltaP `16.8433` edge `0.0735` maxDD `-17.6057`
- `market_context_high->crypto_major_1h` score `-1.0368` n `140` status `ready` deltaP `3.4303` edge `0.0705` maxDD `-15.1032`
- `market_context_high->equity_1h` score `-1.237` n `140` status `ready` deltaP `4.4696` edge `0.0157` maxDD `-8.8863`
- `market_context_high->fx_4h` score `-1.3544` n `134` status `ready` deltaP `-11.7401` edge `-0.0069` maxDD `-1.4115`
- `market_context_high->fx_1h` score `-1.624` n `140` status `ready` deltaP `-9.2173` edge `-0.0052` maxDD `-0.8278`
- `market_context_high->metal_1h` score `-2.0714` n `140` status `ready` deltaP `-3.8024` edge `-0.0079` maxDD `-7.4828`
- `market_context_high->crypto_alt_4h` score `-2.2172` n `134` status `ready` deltaP `17.5078` edge `0.4035` maxDD `-58.6918`
- `market_context_high->unknown_1h` score `-3.1051` n `140` status `ready` deltaP `2.6519` edge `-0.0738` maxDD `-14.2111`
- `market_context_high->crypto_major_4h` score `-3.6179` n `134` status `ready` deltaP `10.4455` edge `0.2589` maxDD `-54.3896`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
