# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T00:37:24.532561+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9858`

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

- `market_context_high->unknown_1h` score `72.261` n `47` status `ready` deltaP `10.7148` edge `5.9574` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `35.5069` n `46` status `ready` deltaP `22.5619` edge `2.8241` maxDD `-0.5817`
- `market_context_high->equity_24h` score `20.6363` n `46` status `ready` deltaP `19.9578` edge `1.5967` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `19.4556` n `46` status `ready` deltaP `17.5347` edge `1.5044` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `9.8508` n `97` status `ready` deltaP `-0.9254` edge `1.5129` maxDD `-46.1999`
- `market_context_high->index_24h` score `6.9435` n `46` status `ready` deltaP `28.9855` edge `0.3941` maxDD `-0.03`
- `news_risk_high->crypto_alt_24h` score `5.5649` n `97` status `ready` deltaP `-3.0839` edge `0.9724` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `4.8986` n `103` status `ready` deltaP `14.5365` edge `0.4111` maxDD `-5.9838`
- `news_risk_high->crypto_major_4h` score `4.5886` n `103` status `ready` deltaP `17.4328` edge `0.3239` maxDD `-2.619`
- `news_risk_high->crypto_alt_1h` score `2.5905` n `103` status `ready` deltaP `13.6068` edge `0.1742` maxDD `-1.5895`
- `market_context_high->index_4h` score `2.4588` n `47` status `ready` deltaP `28.9958` edge `0.027` maxDD `-0.2323`
- `news_risk_high->commodity_24h` score `2.3957` n `97` status `ready` deltaP `23.8688` edge `0.1584` maxDD `-2.431`
- `news_risk_high->crypto_major_1h` score `2.0097` n `103` status `ready` deltaP `15.5529` edge `0.1073` maxDD `-1.8141`
- `market_context_high->metal_24h` score `1.8467` n `46` status `ready` deltaP `22.962` edge `0.0242` maxDD `-0.2042`
- `news_risk_high->fx_4h` score `1.6246` n `103` status `ready` deltaP `23.6814` edge `0.0411` maxDD `-0.421`
- `market_context_high->equity_4h` score `1.3575` n `47` status `ready` deltaP `10.8945` edge `0.0823` maxDD `-1.3444`
- `news_risk_high->fx_24h` score `1.1094` n `97` status `ready` deltaP `27.6221` edge `0.1212` maxDD `-1.7159`
- `news_risk_high->metal_24h` score `0.8624` n `97` status `ready` deltaP `19.0399` edge `0.0754` maxDD `-3.0086`
- `market_context_high->index_1h` score `0.7942` n `47` status `ready` deltaP `12.8137` edge `0.0086` maxDD `-0.2275`
- `news_risk_high->metal_1h` score `0.6757` n `103` status `ready` deltaP `15.6517` edge `0.0113` maxDD `-0.7468`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
