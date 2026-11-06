# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T06:37:26.659774+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4278`

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

- `news_risk_high->crypto_alt_4h` score `-0.063` n `144` status `ready` deltaP `7.9607` edge `0.2025` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4672` n `144` status `ready` deltaP `3.6884` edge `0.0383` maxDD `-5.8225`
- `news_risk_high->index_1h` score `-0.6615` n `144` status `ready` deltaP `3.4431` edge `0.0019` maxDD `-1.3981`
- `news_risk_high->fx_1h` score `-0.7061` n `144` status `ready` deltaP `-2.7071` edge `-0.0024` maxDD `-0.6065`
- `news_risk_high->metal_1h` score `-1.439` n `144` status `ready` deltaP `-7.3811` edge `-0.0173` maxDD `-2.772`
- `news_risk_high->fx_4h` score `-1.4872` n `144` status `ready` deltaP `-8.0115` edge `-0.0121` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-1.6035` n `144` status `ready` deltaP `1.355` edge `0.0068` maxDD `-4.0461`
- `news_risk_high->index_24h` score `-2.1867` n `144` status `ready` deltaP `-11.6301` edge `0.0679` maxDD `-6.99`
- `news_risk_high->equity_1h` score `-2.3218` n `144` status `ready` deltaP `-4.8486` edge `0.0016` maxDD `-16.3557`
- `news_risk_high->commodity_1h` score `-2.5402` n `144` status `ready` deltaP `-11.3149` edge `0.0004` maxDD `-3.2657`
- `news_risk_high->crypto_major_1h` score `-2.7604` n `144` status `ready` deltaP `-5.0815` edge `-0.0236` maxDD `-9.4709`
- `news_risk_high->fx_24h` score `-2.7919` n `144` status `ready` deltaP `-25.2643` edge `-0.029` maxDD `-2.1737`
- `news_risk_high->commodity_4h` score `-4.1135` n `144` status `ready` deltaP `-16.5989` edge `0.0033` maxDD `-9.5011`
- `news_risk_high->crypto_major_4h` score `-5.037` n `144` status `ready` deltaP `-8.2487` edge `-0.0025` maxDD `-21.6473`
- `news_risk_high->metal_4h` score `-5.5265` n `144` status `ready` deltaP `-12.3984` edge `-0.0706` maxDD `-8.916`
- `news_risk_high->equity_24h` score `-8.3466` n `144` status `ready` deltaP `10.7483` edge `0.6078` maxDD `-97.0001`
- `news_risk_high->metal_24h` score `-8.7373` n `144` status `ready` deltaP `-16.2533` edge `-0.2873` maxDD `-15.2631`
- `news_risk_high->equity_4h` score `-9.4085` n `144` status `ready` deltaP `1.8123` edge `0.0121` maxDD `-50.6581`
- `news_risk_high->commodity_24h` score `-10.2753` n `144` status `ready` deltaP `-17.4452` edge `0.0861` maxDD `-43.7525`
- `news_risk_high->crypto_alt_24h` score `-12.2324` n `144` status `ready` deltaP `7.1102` edge `0.0838` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
