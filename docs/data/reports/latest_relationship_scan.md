# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-26T14:37:29.848764+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14776`

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

- `news_risk_high->unknown_24h` score `45.2166` n `53` status `ready` deltaP `11.6319` edge `3.6905` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.2488` n `53` status `ready` deltaP `25.2847` edge `0.8621` maxDD `-0.1281`
- `news_risk_high->crypto_alt_24h` score `11.4585` n `53` status `ready` deltaP `32.6847` edge `0.7811` maxDD `-2.8629`
- `news_risk_high->equity_24h` score `6.8626` n `53` status `ready` deltaP `29.2453` edge `0.47` maxDD `-4.7801`
- `news_risk_high->index_24h` score `3.9951` n `53` status `ready` deltaP `39.7668` edge `0.083` maxDD `-0.2147`
- `news_risk_high->fx_4h` score `2.9814` n `53` status `ready` deltaP `35.8779` edge `0.0227` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `2.8819` n `136` status `ready` deltaP `23.5922` edge `0.1237` maxDD `-0.5994`
- `news_risk_high->unknown_1h` score `2.8022` n `53` status `ready` deltaP `15.7129` edge `0.1643` maxDD `-0.8426`
- `news_risk_high->metal_24h` score `1.8399` n `53` status `ready` deltaP `29.3632` edge `-0.0382` maxDD `-0.0053`
- `news_risk_high->equity_4h` score `1.7465` n `53` status `ready` deltaP `19.889` edge `0.09` maxDD `-2.164`
- `news_risk_high->fx_1h` score `1.1285` n `53` status `ready` deltaP `15.7694` edge `0.0059` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `1.1147` n `137` status `ready` deltaP `11.9531` edge `0.0581` maxDD `-1.5916`
- `news_risk_high->equity_1h` score `0.4349` n `53` status `ready` deltaP `12.9251` edge `0.006` maxDD `-0.9128`
- `news_risk_high->commodity_1h` score `0.4104` n `53` status `ready` deltaP `10.5271` edge `-0.0047` maxDD `-0.5024`
- `news_risk_high->index_4h` score `0.1743` n `53` status `ready` deltaP `7.1186` edge `0.0068` maxDD `-0.1788`
- `news_risk_high->metal_4h` score `-0.0531` n `53` status `ready` deltaP `7.5586` edge `-0.0017` maxDD `-0.249`
- `news_risk_high->index_1h` score `-0.0628` n `53` status `ready` deltaP `3.9996` edge `0.0006` maxDD `-0.1583`
- `news_risk_high->metal_1h` score `-0.227` n `53` status `ready` deltaP `1.4829` edge `-0.0062` maxDD `-0.1413`
- `market_context_high->fx_1h` score `-0.4271` n `137` status `ready` deltaP `2.8924` edge `-0.0008` maxDD `-0.8587`
- `market_context_high->metal_4h` score `-0.8822` n `136` status `ready` deltaP `5.0753` edge `-0.0279` maxDD `-2.6898`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
