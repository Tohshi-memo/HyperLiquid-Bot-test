# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T21:07:26.490051+00:00`
- Price records: `672`
- Market context records: `5915`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11166`

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

- `news_risk_high->fx_4h` score `3.6497` n `30` status `ready` deltaP `37.8659` edge `0.0563` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.0501` n `30` status `ready` deltaP `24.8303` edge `0.0192` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `0.9346` n `30` status `ready` deltaP `11.2375` edge `0.0916` maxDD `-2.0691`
- `market_context_high->equity_4h` score `0.8941` n `220` status `ready` deltaP `7.9878` edge `0.1307` maxDD `-4.0887`
- `news_risk_high->crypto_alt_1h` score `0.2107` n `30` status `ready` deltaP `5.02` edge `0.0397` maxDD `-1.6923`
- `market_context_high->equity_1h` score `-0.1876` n `221` status `ready` deltaP `5.2443` edge `0.033` maxDD `-4.3608`
- `market_context_high->metal_1h` score `-0.3023` n `221` status `ready` deltaP `3.71` edge `0.0036` maxDD `-2.0339`
- `news_risk_high->metal_1h` score `-0.4383` n `30` status `ready` deltaP `1.3872` edge `-0.0288` maxDD `-1.2643`
- `market_context_high->commodity_1h` score `-0.5` n `221` status `ready` deltaP `-1.5973` edge `-0.0019` maxDD `-1.4578`
- `market_context_high->crypto_major_1h` score `-0.5245` n `221` status `ready` deltaP `4.0128` edge `0.0381` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-0.6581` n `221` status `ready` deltaP `2.6519` edge `0.0314` maxDD `-6.6758`
- `market_context_high->fx_1h` score `-0.75` n `221` status `ready` deltaP `-1.8967` edge `-0.001` maxDD `-0.5751`
- `market_context_high->index_1h` score `-0.9549` n `221` status `ready` deltaP `0.2398` edge `0.0036` maxDD `-0.7819`
- `news_risk_high->index_1h` score `-1.1988` n `30` status `ready` deltaP `-11.7964` edge `-0.0236` maxDD `-1.1161`
- `market_context_high->commodity_4h` score `-1.67` n `220` status `ready` deltaP `-3.5947` edge `-0.0188` maxDD `-6.3734`
- `market_context_high->metal_4h` score `-1.7928` n `220` status `ready` deltaP `-4.4429` edge `-0.037` maxDD `-5.725`
- `market_context_high->equity_24h` score `-1.9568` n `213` status `ready` deltaP `13.6713` edge `0.1656` maxDD `-31.2762`
- `news_risk_high->commodity_4h` score `-1.988` n `30` status `ready` deltaP `-16.4735` edge `-0.0575` maxDD `-2.3372`
- `market_context_high->index_4h` score `-1.9945` n `220` status `ready` deltaP `-0.9423` edge `0.0088` maxDD `-3.165`
- `market_context_high->fx_24h` score `-2.1398` n `213` status `ready` deltaP `0.8949` edge `0.0015` maxDD `-5.5435`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
