# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T16:52:27.206241+00:00`
- Price records: `672`
- Market context records: `5683`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8768`

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

- `market_context_high->equity_24h` score `1.8157` n `205` status `ready` deltaP `16.0205` edge `0.5524` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `0.8393` n `255` status `ready` deltaP `11.6571` edge `0.215` maxDD `-13.4882`
- `market_context_high->crypto_alt_4h` score `0.4038` n `255` status `ready` deltaP `8.7387` edge `0.1564` maxDD `-9.1473`
- `market_context_high->equity_4h` score `0.1667` n `255` status `ready` deltaP `5.7538` edge `0.1394` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2705` n `267` status `ready` deltaP `1.7605` edge `0.0012` maxDD `-0.4764`
- `market_context_high->crypto_alt_1h` score `-0.4369` n `267` status `ready` deltaP `2.8864` edge `0.0405` maxDD `-5.0257`
- `market_context_high->metal_1h` score `-0.4865` n `267` status `ready` deltaP `0.8623` edge `-0.0006` maxDD `-2.0682`
- `market_context_high->equity_1h` score `-0.5454` n `267` status `ready` deltaP `3.9371` edge `0.029` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.6153` n `267` status `ready` deltaP `0.4884` edge `0.0047` maxDD `-0.9472`
- `market_context_high->crypto_major_1h` score `-0.6652` n `267` status `ready` deltaP `4.3077` edge `0.0404` maxDD `-6.9639`
- `market_context_high->commodity_1h` score `-0.9289` n `267` status `ready` deltaP `0.4115` edge `-0.0036` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.1575` n `255` status `ready` deltaP `4.2049` edge `0.007` maxDD `-1.3415`
- `market_context_high->fx_24h` score `-1.1977` n `205` status `ready` deltaP `13.7864` edge `0.0468` maxDD `-3.0816`
- `market_context_high->index_4h` score `-1.2709` n `255` status `ready` deltaP `-0.5207` edge `0.0077` maxDD `-3.04`
- `market_context_high->index_24h` score `-2.5149` n `205` status `ready` deltaP `6.0815` edge `0.0382` maxDD `-17.0937`
- `market_context_high->metal_4h` score `-2.8748` n `255` status `ready` deltaP `-11.6547` edge `-0.0533` maxDD `-11.6719`
- `market_context_high->commodity_4h` score `-3.8029` n `255` status `ready` deltaP `-2.6178` edge `-0.0319` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.9128` n `205` status `ready` deltaP `3.8093` edge `0.0109` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-8.2977` n `205` status `ready` deltaP `-12.2155` edge `-0.2478` maxDD `-32.7652`
- `market_context_high->commodity_24h` score `-11.9935` n `205` status `ready` deltaP `-9.5952` edge `-0.0746` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
