# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T23:07:26.242641+00:00`
- Price records: `672`
- Market context records: `5604`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11433`

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

- `market_context_high->equity_24h` score `3.4591` n `174` status `ready` deltaP `15.0084` edge `0.6961` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `1.4607` n `217` status `ready` deltaP `13.1512` edge `0.2633` maxDD `-14.0065`
- `market_context_high->fx_24h` score `1.2015` n `174` status `ready` deltaP `21.0908` edge `0.0569` maxDD `-1.457`
- `market_context_high->crypto_alt_4h` score `0.8174` n `217` status `ready` deltaP `8.4151` edge `0.1761` maxDD `-9.46`
- `market_context_high->equity_4h` score `0.4901` n `217` status `ready` deltaP `6.2704` edge `0.1629` maxDD `-7.4425`
- `market_context_high->equity_1h` score `-0.3224` n `229` status `ready` deltaP `5.8835` edge `0.0346` maxDD `-5.0555`
- `market_context_high->fx_1h` score `-0.339` n `229` status `ready` deltaP `0.4805` edge `0.0009` maxDD `-0.472`
- `market_context_high->metal_1h` score `-0.5398` n `229` status `ready` deltaP `-0.3432` edge `0.0006` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.5969` n `229` status `ready` deltaP `1.1421` edge `0.0388` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.6037` n `229` status `ready` deltaP `4.1609` edge `0.0465` maxDD `-6.9639`
- `market_context_high->index_1h` score `-0.8855` n `229` status `ready` deltaP `1.042` edge `0.0061` maxDD `-0.9472`
- `market_context_high->fx_4h` score `-1.1088` n `217` status `ready` deltaP `1.4885` edge `0.0076` maxDD `-1.1074`
- `market_context_high->crypto_major_24h` score `-1.171` n `174` status `ready` deltaP `10.3269` edge `0.2876` maxDD `-29.6555`
- `market_context_high->commodity_1h` score `-1.1911` n `229` status `ready` deltaP `-2.4017` edge `-0.0067` maxDD `-3.7906`
- `market_context_high->index_4h` score `-1.6093` n `217` status `ready` deltaP `2.1019` edge `0.0128` maxDD `-2.874`
- `market_context_high->index_24h` score `-2.3687` n `174` status `ready` deltaP `10.261` edge `0.0266` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.9048` n `217` status `ready` deltaP `-11.7687` edge `-0.0556` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-4.2084` n `217` status `ready` deltaP `-5.962` edge `-0.0434` maxDD `-14.071`
- `market_context_high->metal_24h` score `-8.162` n `174` status `ready` deltaP `-9.5426` edge `-0.2467` maxDD `-32.8874`
- `market_context_high->crypto_alt_24h` score `-11.2147` n `174` status `ready` deltaP `0.1138` edge `-0.0656` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
