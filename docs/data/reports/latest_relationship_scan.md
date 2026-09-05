# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-05T14:52:26.351139+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10537`

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

- `risk_on_high->unknown_4h` score `22.1638` n `140` status `ready` deltaP `2.0122` edge `1.9079` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `22.1638` n `140` status `ready` deltaP `2.0122` edge `1.9079` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `10.3002` n `228` status `ready` deltaP `4.3806` edge `0.923` maxDD `-2.8419`
- `news_risk_high->crypto_alt_24h` score `7.3247` n `37` status `ready` deltaP `25.1783` edge `0.4695` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `3.8016` n `37` status `ready` deltaP `19.9653` edge `0.1837` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.6258` n `37` status `ready` deltaP `17.1803` edge `0.2289` maxDD `-0.9693`
- `news_risk_high->metal_4h` score `2.3661` n `37` status `ready` deltaP `23.9989` edge `0.0593` maxDD `-0.7692`
- `news_risk_high->commodity_4h` score `1.8619` n `37` status `ready` deltaP `10.9715` edge `0.1021` maxDD `-0.2737`
- `news_risk_high->equity_1h` score `1.6099` n `37` status `ready` deltaP `13.3841` edge `0.084` maxDD `-0.7924`
- `news_risk_high->metal_1h` score `1.2478` n `37` status `ready` deltaP `14.8649` edge `0.0242` maxDD `-0.2118`
- `news_risk_high->crypto_major_1h` score `1.211` n `37` status `ready` deltaP `6.4655` edge `0.0761` maxDD `-0.4628`
- `news_risk_high->index_1h` score `1.1634` n `37` status `ready` deltaP `14.5736` edge `0.0132` maxDD `-0.0724`
- `news_risk_high->crypto_major_24h` score `0.9921` n `37` status `ready` deltaP `16.5776` edge `0.2943` maxDD `-18.2098`
- `news_risk_high->crypto_alt_1h` score `0.9909` n `37` status `ready` deltaP `9.326` edge `0.0469` maxDD `-0.7867`
- `news_risk_high->crypto_alt_4h` score `0.6189` n `37` status `ready` deltaP `6.2459` edge `0.0428` maxDD `-1.296`
- `news_risk_high->fx_24h` score `0.514` n `37` status `ready` deltaP `15.2684` edge `0.0426` maxDD `-3.1244`
- `market_context_high->equity_24h` score `0.4436` n `184` status `ready` deltaP `14.7796` edge `0.373` maxDD `-20.7654`
- `news_risk_high->commodity_1h` score `-0.0169` n `37` status `ready` deltaP `5.8748` edge `0.0033` maxDD `-0.9036`
- `risk_on_high->metal_1h` score `-0.0318` n `150` status `ready` deltaP `10.0` edge `0.0005` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `-0.0318` n `150` status `ready` deltaP `10.0` edge `0.0005` maxDD `-1.699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
