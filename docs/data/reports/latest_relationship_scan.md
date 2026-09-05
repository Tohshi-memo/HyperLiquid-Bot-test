# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-05T14:37:25.518426+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10531`

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

- `risk_on_high->unknown_4h` score `22.209` n `140` status `ready` deltaP `2.0122` edge `1.9075` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `22.209` n `140` status `ready` deltaP `2.0122` edge `1.9075` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `10.3478` n `228` status `ready` deltaP `4.3806` edge `0.9228` maxDD `-2.8419`
- `news_risk_high->crypto_alt_24h` score `7.3739` n `37` status `ready` deltaP `25.1783` edge `0.4736` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `3.8167` n `37` status `ready` deltaP `20.1389` edge `0.1838` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.6378` n `37` status `ready` deltaP `17.1803` edge `0.2299` maxDD `-0.9693`
- `news_risk_high->metal_4h` score `2.3527` n `37` status `ready` deltaP `23.8464` edge `0.0592` maxDD `-0.7692`
- `news_risk_high->commodity_4h` score `1.8753` n `37` status `ready` deltaP `11.124` edge `0.1022` maxDD `-0.2737`
- `news_risk_high->equity_1h` score `1.623` n `37` status `ready` deltaP `13.5338` edge `0.0841` maxDD `-0.7924`
- `news_risk_high->metal_1h` score `1.2466` n `37` status `ready` deltaP `14.8649` edge `0.0241` maxDD `-0.2118`
- `news_risk_high->crypto_major_1h` score `1.2314` n `37` status `ready` deltaP `6.6152` edge `0.0768` maxDD `-0.4628`
- `news_risk_high->index_1h` score `1.1634` n `37` status `ready` deltaP `14.5736` edge `0.0132` maxDD `-0.0724`
- `news_risk_high->crypto_major_24h` score `1.0147` n `37` status `ready` deltaP `16.5776` edge `0.2972` maxDD `-18.2098`
- `news_risk_high->crypto_alt_1h` score `1.0077` n `37` status `ready` deltaP `9.4757` edge `0.0473` maxDD `-0.7867`
- `news_risk_high->crypto_alt_4h` score `0.6383` n `37` status `ready` deltaP `6.3983` edge `0.0434` maxDD `-1.296`
- `news_risk_high->fx_24h` score `0.5001` n `37` status `ready` deltaP `15.0947` edge `0.0426` maxDD `-3.1244`
- `market_context_high->equity_24h` score `0.4361` n `185` status `ready` deltaP `14.9118` edge `0.3715` maxDD `-20.7654`
- `news_risk_high->commodity_1h` score `-0.0169` n `37` status `ready` deltaP `5.8748` edge `0.0033` maxDD `-0.9036`
- `risk_on_high->metal_1h` score `-0.0318` n `150` status `ready` deltaP `10.0` edge `0.0005` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `-0.0318` n `150` status `ready` deltaP `10.0` edge `0.0005` maxDD `-1.699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
