# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T23:22:28.017609+00:00`
- Price records: `672`
- Market context records: `5605`
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

- `market_context_high->equity_24h` score `3.4255` n `174` status `ready` deltaP `15.0084` edge `0.6933` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `1.465` n `218` status `ready` deltaP `13.3097` edge `0.2626` maxDD `-14.0065`
- `market_context_high->fx_24h` score `1.2027` n `174` status `ready` deltaP `21.0908` edge `0.057` maxDD `-1.457`
- `market_context_high->crypto_alt_4h` score `0.8306` n `218` status `ready` deltaP `8.58` edge `0.1761` maxDD `-9.46`
- `market_context_high->equity_4h` score `0.4684` n `218` status `ready` deltaP `6.1353` edge `0.162` maxDD `-7.4425`
- `market_context_high->equity_1h` score `-0.3115` n `230` status `ready` deltaP `6.0505` edge `0.0344` maxDD `-5.0555`
- `market_context_high->fx_1h` score `-0.3514` n `230` status `ready` deltaP `0.2564` edge `0.0008` maxDD `-0.472`
- `market_context_high->metal_1h` score `-0.5275` n `230` status `ready` deltaP `-0.1211` edge `0.0007` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.6111` n `230` status `ready` deltaP `1.0544` edge `0.0382` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.6296` n `230` status `ready` deltaP `3.9274` edge `0.0459` maxDD `-6.9639`
- `market_context_high->index_1h` score `-0.8679` n `230` status `ready` deltaP `1.2471` edge `0.0062` maxDD `-0.9472`
- `market_context_high->fx_4h` score `-1.1578` n `218` status `ready` deltaP `1.2349` edge `0.0074` maxDD `-1.1257`
- `market_context_high->commodity_1h` score `-1.1945` n `230` status `ready` deltaP `-2.459` edge `-0.0066` maxDD `-3.7906`
- `market_context_high->crypto_major_24h` score `-1.2737` n `174` status `ready` deltaP `10.1533` edge `0.2802` maxDD `-29.6555`
- `market_context_high->index_4h` score `-1.6188` n `218` status `ready` deltaP `1.9985` edge `0.0127` maxDD `-2.874`
- `market_context_high->index_24h` score `-2.3839` n `174` status `ready` deltaP `10.0874` edge `0.0258` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.888` n `218` status `ready` deltaP `-11.4749` edge `-0.0554` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-4.2101` n `218` status `ready` deltaP `-5.9829` edge `-0.0434` maxDD `-14.071`
- `market_context_high->metal_24h` score `-8.1796` n `174` status `ready` deltaP `-9.7162` edge `-0.2478` maxDD `-32.8874`
- `market_context_high->crypto_alt_24h` score `-11.3089` n `174` status `ready` deltaP `-0.0599` edge `-0.0723` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
