# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T07:52:27.012920+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5072`

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

- `market_context_high->unknown_1h` score `340.6763` n `50` status `ready` deltaP `9.8263` edge `28.3291` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `287.2373` n `50` status `ready` deltaP `8.8415` edge `23.8775` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `13.7994` n `63` status `ready` deltaP `39.3601` edge `0.9085` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `11.0267` n `50` status `ready` deltaP `36.1667` edge `0.8194` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `9.294` n `63` status `ready` deltaP `36.6568` edge `0.5786` maxDD `-2.8784`
- `market_context_high->crypto_alt_24h` score `8.9181` n `50` status `ready` deltaP `16.5347` edge `0.8039` maxDD `-11.6768`
- `market_context_high->crypto_major_4h` score `6.9097` n `50` status `ready` deltaP `17.5427` edge `0.5292` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.9169` n `50` status `ready` deltaP `15.5793` edge `0.4352` maxDD `-7.6792`
- `news_risk_high->crypto_alt_4h` score `3.9901` n `92` status `ready` deltaP `15.1445` edge `0.3659` maxDD `-6.4152`
- `market_context_high->equity_24h` score `3.0197` n `50` status `ready` deltaP `14.1806` edge `0.4788` maxDD `-11.8957`
- `market_context_high->fx_4h` score `2.9129` n `50` status `ready` deltaP `32.689` edge `0.0383` maxDD `-0.0791`
- `market_context_high->crypto_alt_1h` score `2.9121` n `50` status `ready` deltaP `13.9042` edge `0.2163` maxDD `-3.6387`
- `market_context_high->crypto_major_1h` score `2.8728` n `50` status `ready` deltaP `14.0` edge `0.1911` maxDD `-2.2692`
- `news_risk_high->equity_4h` score `2.1111` n `92` status `ready` deltaP `22.7134` edge `0.0941` maxDD `-2.9013`
- `market_context_high->fx_1h` score `1.4639` n `50` status `ready` deltaP `20.491` edge `0.0118` maxDD `-0.113`
- `market_context_high->index_24h` score `1.0139` n `50` status `ready` deltaP `16.1806` edge `0.0792` maxDD `-1.2338`
- `news_risk_high->metal_24h` score `0.8977` n `63` status `ready` deltaP `3.5714` edge `0.1784` maxDD `-2.192`
- `news_risk_high->crypto_alt_1h` score `0.663` n `104` status `ready` deltaP `4.635` edge `0.0806` maxDD `-2.4998`
- `news_risk_high->commodity_24h` score `0.6209` n `63` status `ready` deltaP `15.3026` edge `0.103` maxDD `-5.0336`
- `market_context_high->fx_24h` score `0.5133` n `50` status `ready` deltaP `14.4306` edge `0.0714` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
