# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-03T08:52:26.253203+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4490`

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

- `news_risk_high->crypto_alt_4h` score `0.2764` n `146` status `ready` deltaP `6.2375` edge `0.2575` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4191` n `146` status `ready` deltaP `2.1819` edge `0.0545` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6374` n `146` status `ready` deltaP `-1.3247` edge `-0.0028` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.8915` n `146` status `ready` deltaP `1.3473` edge `-0.0033` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.2447` n `146` status `ready` deltaP `-4.3495` edge `-0.0084` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.2705` n `146` status `ready` deltaP `-3.9634` edge `-0.0113` maxDD `-1.6794`
- `news_risk_high->metal_24h` score `-1.9175` n `143` status `ready` deltaP `9.3969` edge `0.1159` maxDD `-15.0667`
- `news_risk_high->index_4h` score `-2.0269` n `146` status `ready` deltaP `-2.6646` edge `-0.012` maxDD `-4.0745`
- `news_risk_high->index_24h` score `-2.2679` n `143` status `ready` deltaP `-3.8948` edge `0.0194` maxDD `-7.402`
- `news_risk_high->fx_24h` score `-2.393` n `143` status `ready` deltaP `-17.3733` edge `-0.0201` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.4235` n `146` status `ready` deltaP `-9.3758` edge `-0.0028` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.6766` n `146` status `ready` deltaP `-6.636` edge `-0.0313` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.2331` n `146` status `ready` deltaP `-8.3053` edge `-0.0415` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-4.0105` n `146` status `ready` deltaP `-13.5421` edge `-0.0085` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.6697` n `146` status `ready` deltaP `-6.2333` edge `-0.0271` maxDD `-9.3056`
- `news_risk_high->crypto_alt_24h` score `-5.9363` n `143` status `ready` deltaP `18.7962` edge `0.7226` maxDD `-112.3843`
- `news_risk_high->crypto_major_4h` score `-6.9054` n `146` status `ready` deltaP `-13.6214` edge `-0.0827` maxDD `-24.1554`
- `news_risk_high->equity_24h` score `-9.3741` n `143` status `ready` deltaP `13.9351` edge `0.4398` maxDD `-91.4434`
- `news_risk_high->equity_4h` score `-11.3022` n `146` status `ready` deltaP `-0.6828` edge `-0.1012` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.9245` n `143` status `ready` deltaP `-24.2424` edge `-0.0978` maxDD `-43.0768`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
