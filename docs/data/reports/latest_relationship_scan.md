# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T02:37:26.624314+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4818`

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

- `market_context_high->unknown_1h` score `364.8827` n `50` status `ready` deltaP `10.4251` edge `30.3423` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `293.1693` n `50` status `ready` deltaP `10.061` edge `24.3637` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `13.6101` n `70` status `ready` deltaP `29.1717` edge `1.017` maxDD `-3.8506`
- `market_context_high->crypto_alt_24h` score `10.9982` n `50` status `ready` deltaP `21.7431` edge `0.9419` maxDD `-11.6271`
- `news_risk_high->equity_24h` score `10.1606` n `70` status `ready` deltaP `33.7351` edge `0.6703` maxDD `-2.8784`
- `market_context_high->crypto_major_24h` score `8.8894` n `50` status `ready` deltaP `31.3056` edge `0.6737` maxDD `-9.3299`
- `news_risk_high->crypto_alt_4h` score `7.9253` n `99` status `ready` deltaP `32.7528` edge `0.5765` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.3631` n `50` status `ready` deltaP `17.3902` edge `0.568` maxDD `-3.294`
- `news_risk_high->crypto_major_24h` score `7.0536` n `70` status `ready` deltaP `12.1627` edge `0.6058` maxDD `-4.2603`
- `news_risk_high->crypto_major_4h` score `6.5301` n `99` status `ready` deltaP `25.1478` edge `0.4376` maxDD `-2.553`
- `market_context_high->crypto_alt_4h` score `5.7958` n `50` status `ready` deltaP `15.8841` edge `0.506` maxDD `-7.6465`
- `news_risk_high->equity_4h` score `3.2945` n `99` status `ready` deltaP `27.2265` edge `0.1543` maxDD `-2.9013`
- `market_context_high->crypto_alt_1h` score `3.1918` n `50` status `ready` deltaP `14.503` edge `0.2356` maxDD `-3.6376`
- `market_context_high->crypto_major_1h` score `2.9917` n `50` status `ready` deltaP `13.4012` edge `0.205` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.7787` n `50` status `ready` deltaP `31.0122` edge `0.0383` maxDD `-0.0791`
- `news_risk_high->index_24h` score `2.4192` n `70` status `ready` deltaP `23.001` edge `0.0808` maxDD `-0.2696`
- `news_risk_high->metal_24h` score `1.8271` n `70` status `ready` deltaP `9.6329` edge `0.1969` maxDD `-2.0419`
- `news_risk_high->crypto_alt_1h` score `1.6555` n `99` status `ready` deltaP `7.0889` edge `0.1426` maxDD `-2.4854`
- `market_context_high->fx_1h` score `1.4352` n `50` status `ready` deltaP `20.1916` edge `0.0114` maxDD `-0.113`
- `news_risk_high->crypto_major_1h` score `1.3072` n `99` status `ready` deltaP `6.977` edge `0.1252` maxDD `-2.3555`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
