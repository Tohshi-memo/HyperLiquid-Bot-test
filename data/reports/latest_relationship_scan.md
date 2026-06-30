# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T18:52:29.370249+00:00`
- Price records: `672`
- Market context records: `5275`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9652`

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

- `market_context_high->unknown_24h` score `25.9594` n `153` status `ready` deltaP `28.9011` edge `1.9796` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `7.6316` n `153` status `ready` deltaP `25.7353` edge `0.8794` maxDD `-26.5332`
- `market_context_high->crypto_alt_4h` score `4.2885` n `170` status `ready` deltaP `15.9236` edge `0.4153` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.7558` n `170` status `ready` deltaP `14.7041` edge `0.4442` maxDD `-14.0065`
- `market_context_high->equity_24h` score `3.707` n `153` status `ready` deltaP `19.9653` edge `0.7387` maxDD `-40.0306`
- `market_context_high->unknown_4h` score `0.9724` n `170` status `ready` deltaP `14.9928` edge `0.0833` maxDD `-5.5109`
- `market_context_high->equity_4h` score `0.8541` n `170` status `ready` deltaP `9.306` edge `0.173` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.5757` n `153` status `ready` deltaP `13.3068` edge `0.0488` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.5085` n `179` status `ready` deltaP `5.0589` edge `0.1048` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.2844` n `179` status `ready` deltaP `5.8876` edge `0.109` maxDD `-6.9639`
- `market_context_high->index_24h` score `0.2647` n `153` status `ready` deltaP `21.1703` edge `0.0563` maxDD `-7.413`
- `market_context_high->equity_1h` score `0.0547` n `179` status `ready` deltaP `6.7023` edge `0.0564` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.0259` n `179` status `ready` deltaP `6.1837` edge `0.0113` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.2697` n `179` status `ready` deltaP `3.7517` edge `0.0117` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.3423` n `179` status `ready` deltaP `0.1188` edge `0.0001` maxDD `-0.5823`
- `market_context_high->index_4h` score `-0.496` n `170` status `ready` deltaP `6.6463` edge `0.0261` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.6712` n `170` status `ready` deltaP `2.1395` edge `0.0026` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.4324` n `179` status `ready` deltaP `-3.0726` edge `-0.0071` maxDD `-3.3428`
- `market_context_high->metal_4h` score `-1.626` n `170` status `ready` deltaP `-2.5072` edge `0.0086` maxDD `-9.3609`
- `market_context_high->unknown_1h` score `-2.2308` n `179` status `ready` deltaP `6.622` edge `-0.1659` maxDD `-2.7986`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
