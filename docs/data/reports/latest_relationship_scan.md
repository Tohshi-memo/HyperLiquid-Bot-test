# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T13:52:29.404532+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4863`

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

- `news_risk_high->crypto_alt_4h` score `-0.012` n `146` status `ready` deltaP `5.4753` edge `0.2256` maxDD `-14.0916`
- `news_risk_high->fx_1h` score `-0.5424` n `146` status `ready` deltaP `0.4717` edge `-0.0026` maxDD `-0.6065`
- `news_risk_high->crypto_alt_1h` score `-0.5532` n `146` status `ready` deltaP `1.134` edge `0.0443` maxDD `-5.8225`
- `news_risk_high->metal_24h` score `-0.8556` n `125` status `ready` deltaP `12.2569` edge `0.1342` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-1.0712` n `146` status `ready` deltaP `-0.4491` edge `-0.0063` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.1342` n `146` status `ready` deltaP `-1.372` edge `-0.0111` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.2868` n `146` status `ready` deltaP `-4.9483` edge `-0.0098` maxDD `-3.1082`
- `news_risk_high->fx_24h` score `-1.9947` n `125` status `ready` deltaP `-13.3903` edge `0.0044` maxDD `-2.336`
- `news_risk_high->index_4h` score `-2.2228` n `146` status `ready` deltaP `-4.6463` edge `-0.0239` maxDD `-4.0745`
- `news_risk_high->crypto_alt_24h` score `-2.2987` n `125` status `ready` deltaP `14.6264` edge `0.5275` maxDD `-63.2436`
- `news_risk_high->commodity_1h` score `-2.3757` n `146` status `ready` deltaP `-8.4776` edge `-0.0048` maxDD `-3.2657`
- `news_risk_high->index_24h` score `-2.6066` n `125` status `ready` deltaP `-6.8681` edge `-0.0042` maxDD `-7.402`
- `news_risk_high->equity_1h` score `-2.9082` n `146` status `ready` deltaP `-7.3845` edge `-0.056` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.3518` n `146` status `ready` deltaP `-8.7544` edge `-0.0484` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.9436` n `146` status `ready` deltaP `-11.8652` edge `-0.0141` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.561` n `146` status `ready` deltaP `-4.7089` edge `-0.0282` maxDD `-9.3056`
- `news_risk_high->equity_24h` score `-5.1398` n `125` status `ready` deltaP `8.6181` edge `0.2931` maxDD `-67.0937`
- `news_risk_high->crypto_major_4h` score `-7.253` n `146` status `ready` deltaP `-14.2312` edge `-0.1076` maxDD `-24.1554`
- `news_risk_high->crypto_major_24h` score `-12.1453` n `125` status `ready` deltaP `-22.3472` edge `-0.1887` maxDD `-42.6211`
- `news_risk_high->commodity_24h` score `-12.1906` n `125` status `ready` deltaP `-26.4056` edge `-0.162` maxDD `-31.8942`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
