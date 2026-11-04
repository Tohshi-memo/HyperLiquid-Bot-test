# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-04T10:37:29.474424+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4038`

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

- `news_risk_high->crypto_alt_4h` score `0.0936` n `146` status `ready` deltaP `7.7619` edge `0.2239` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4457` n `146` status `ready` deltaP `2.3316` edge `0.0501` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7191` n `146` status `ready` deltaP `-2.8217` edge `-0.0033` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.8568` n `146` status `ready` deltaP `1.6467` edge `-0.0024` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.353` n `146` status `ready` deltaP `-5.6968` edge `-0.0133` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.4693` n `146` status `ready` deltaP `-7.622` edge `-0.0124` maxDD `-1.6794`
- `news_risk_high->index_24h` score `-1.8139` n `146` status `ready` deltaP `0.3354` edge `0.0494` maxDD `-7.402`
- `news_risk_high->index_4h` score `-1.846` n `146` status `ready` deltaP `0.0793` edge `-0.0071` maxDD `-4.0745`
- `news_risk_high->metal_24h` score `-2.1517` n `146` status `ready` deltaP `8.652` edge `0.1212` maxDD `-16.6552`
- `news_risk_high->fx_24h` score `-2.3625` n `146` status `ready` deltaP `-17.8534` edge `-0.013` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.3815` n `146` status `ready` deltaP `-9.2261` edge `-0.0003` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.6244` n `146` status `ready` deltaP `-5.7378` edge `-0.0306` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.1192` n `146` status `ready` deltaP `-7.4071` edge `-0.038` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.7938` n `146` status `ready` deltaP `-12.0177` edge `-0.0006` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.6914` n `146` status `ready` deltaP `-4.404` edge `-0.0411` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.7723` n `146` status `ready` deltaP `-11.7921` edge `-0.0838` maxDD `-24.1554`
- `news_risk_high->crypto_alt_24h` score `-8.1598` n `146` status `ready` deltaP `17.2851` edge `0.5381` maxDD `-118.6236`
- `news_risk_high->equity_24h` score `-10.4188` n `146` status `ready` deltaP `14.8545` edge `0.4831` maxDD `-102.3626`
- `news_risk_high->equity_4h` score `-11.3626` n `146` status `ready` deltaP `-0.9877` edge `-0.1042` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.2787` n `146` status `ready` deltaP `-20.7834` edge `-0.0586` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
