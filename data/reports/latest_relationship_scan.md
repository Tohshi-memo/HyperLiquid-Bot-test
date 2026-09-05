# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-05T01:52:30.996459+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10456`

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

- `risk_on_high->unknown_4h` score `19.7423` n `133` status `ready` deltaP `8.3887` edge `1.6511` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `19.7423` n `133` status `ready` deltaP `8.3887` edge `1.6511` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `9.2448` n `217` status `ready` deltaP `8.8253` edge `0.7811` maxDD `-2.563`
- `news_risk_high->crypto_alt_24h` score `6.4676` n `39` status `ready` deltaP `22.3691` edge `0.4168` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `3.6498` n `39` status `ready` deltaP `21.0871` edge `0.172` maxDD `-0.0075`
- `news_risk_high->crypto_major_4h` score `3.3233` n `39` status `ready` deltaP `14.6576` edge `0.2233` maxDD `-1.1927`
- `news_risk_high->metal_4h` score `2.2678` n `39` status `ready` deltaP `23.2646` edge `0.056` maxDD `-0.7692`
- `news_risk_high->commodity_4h` score `1.7423` n `39` status `ready` deltaP `10.5418` edge `0.095` maxDD `-0.2737`
- `news_risk_high->equity_1h` score `1.6755` n `39` status `ready` deltaP `14.6093` edge `0.0813` maxDD `-0.7924`
- `news_risk_high->index_1h` score `1.3408` n `39` status `ready` deltaP `16.8356` edge `0.0129` maxDD `-0.0724`
- `news_risk_high->metal_1h` score `1.1114` n `39` status `ready` deltaP `13.3541` edge `0.0229` maxDD `-0.2118`
- `news_risk_high->crypto_major_1h` score `0.9885` n `39` status `ready` deltaP `4.3145` edge `0.0719` maxDD `-0.4628`
- `news_risk_high->crypto_alt_4h` score `0.8685` n `39` status `ready` deltaP `6.6057` edge `0.0612` maxDD `-1.296`
- `news_risk_high->crypto_alt_1h` score `0.7247` n `39` status `ready` deltaP `6.5984` edge `0.0429` maxDD `-0.7867`
- `risk_on_high->metal_1h` score `0.1373` n `133` status `ready` deltaP `13.1613` edge `0.0011` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.1373` n `133` status `ready` deltaP `13.1613` edge `0.0011` maxDD `-1.699`
- `news_risk_high->commodity_1h` score `0.084` n `39` status `ready` deltaP `7.8152` edge `0.0033` maxDD `-0.9036`
- `news_risk_high->fx_24h` score `-0.0795` n `39` status `ready` deltaP `9.8557` edge `0.0377` maxDD `-3.1357`
- `risk_on_high->index_1h` score `-0.205` n `133` status `ready` deltaP `3.2439` edge `-0.0034` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.205` n `133` status `ready` deltaP `3.2439` edge `-0.0034` maxDD `-0.5605`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
