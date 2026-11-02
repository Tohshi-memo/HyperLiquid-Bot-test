# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T14:52:48.673347+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4881`

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

- `news_risk_high->crypto_alt_4h` score `-0.0326` n `146` status `ready` deltaP `5.1704` edge `0.225` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.501` n `146` status `ready` deltaP `1.4334` edge `0.049` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.5175` n `146` status `ready` deltaP `0.9208` edge `-0.0024` maxDD `-0.6065`
- `news_risk_high->metal_24h` score `-0.8313` n `126` status `ready` deltaP `12.5744` edge `0.1352` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-1.0485` n `146` status `ready` deltaP `-0.2994` edge `-0.0054` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.1334` n `146` status `ready` deltaP `-1.372` edge `-0.011` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.2969` n `146` status `ready` deltaP `-5.098` edge `-0.0101` maxDD `-3.1082`
- `news_risk_high->fx_24h` score `-2.0122` n `126` status `ready` deltaP `-13.6657` edge `0.004` maxDD `-2.336`
- `news_risk_high->index_4h` score `-2.2086` n `146` status `ready` deltaP `-4.4938` edge `-0.0231` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.3085` n `146` status `ready` deltaP `-8.0285` edge `-0.0022` maxDD `-3.2657`
- `news_risk_high->crypto_alt_24h` score `-2.5472` n `126` status `ready` deltaP `14.6329` edge `0.5264` maxDD `-65.3749`
- `news_risk_high->index_24h` score `-2.5624` n `126` status `ready` deltaP `-6.4237` edge `-0.0015` maxDD `-7.402`
- `news_risk_high->equity_1h` score `-2.8122` n `146` status `ready` deltaP `-7.0851` edge `-0.0457` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.2858` n `146` status `ready` deltaP `-8.455` edge `-0.0449` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.8564` n `146` status `ready` deltaP `-11.2555` edge `-0.0109` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.5851` n `146` status `ready` deltaP `-4.8613` edge `-0.0292` maxDD `-9.3056`
- `news_risk_high->equity_24h` score `-4.9626` n `126` status `ready` deltaP `9.251` edge `0.3116` maxDD `-67.0937`
- `news_risk_high->crypto_major_4h` score `-7.2218` n `146` status `ready` deltaP `-14.2312` edge `-0.105` maxDD `-24.1554`
- `news_risk_high->crypto_major_24h` score `-12.099` n `126` status `ready` deltaP `-21.875` edge `-0.1814` maxDD `-43.1482`
- `news_risk_high->commodity_24h` score `-12.3342` n `126` status `ready` deltaP `-26.4881` edge `-0.1624` maxDD `-32.7755`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
