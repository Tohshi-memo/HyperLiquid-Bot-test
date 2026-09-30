# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T07:23:05.265368+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7460`

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

- `news_risk_high->unknown_24h` score `1058.1544` n `135` status `ready` deltaP `1.9097` edge `88.1668` maxDD `0.0`
- `market_context_high->unknown_1h` score `681.9788` n `35` status `ready` deltaP `9.7305` edge `56.7667` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `18.2077` n `135` status `ready` deltaP `28.5532` edge `1.3479` maxDD `-1.0093`
- `news_risk_high->equity_24h` score `8.1611` n `135` status `ready` deltaP `28.0324` edge `0.7281` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `7.7025` n `135` status `ready` deltaP `23.9931` edge `0.7973` maxDD `-15.8971`
- `news_risk_high->index_24h` score `3.819` n `135` status `ready` deltaP `34.2245` edge `0.1379` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `3.462` n `135` status `ready` deltaP `26.4004` edge `0.2399` maxDD `-2.192`
- `news_risk_high->equity_4h` score `2.9532` n `135` status `ready` deltaP `29.6285` edge `0.2087` maxDD `-9.143`
- `news_risk_high->crypto_alt_4h` score `1.8988` n `135` status `ready` deltaP `11.2647` edge `0.3491` maxDD `-15.9436`
- `market_context_high->fx_1h` score `1.2409` n `35` status `ready` deltaP `17.6475` edge `0.008` maxDD `-0.113`
- `news_risk_high->crypto_alt_1h` score `1.1377` n `135` status `ready` deltaP `9.5509` edge `0.1222` maxDD `-4.2849`
- `market_context_high->crypto_major_1h` score `1.0389` n `35` status `ready` deltaP `5.6202` edge `0.1101` maxDD `-3.546`
- `market_context_high->crypto_alt_1h` score `0.9313` n `35` status `ready` deltaP `6.6938` edge `0.0993` maxDD `-3.6387`
- `news_risk_high->equity_1h` score `0.9296` n `135` status `ready` deltaP `9.5509` edge `0.0761` maxDD `-1.6514`
- `market_context_high->equity_1h` score `0.7721` n `35` status `ready` deltaP `12.408` edge `0.0588` maxDD `-2.4027`
- `market_context_high->metal_1h` score `0.6112` n `35` status `ready` deltaP `7.8785` edge `0.0205` maxDD `-0.4338`
- `news_risk_high->index_1h` score `0.5197` n `135` status `ready` deltaP `9.1173` edge `0.0113` maxDD `-0.302`
- `market_context_high->index_1h` score `0.1003` n `35` status `ready` deltaP `4.8845` edge `0.014` maxDD `-0.3627`
- `news_risk_high->index_4h` score `-0.1296` n `135` status `ready` deltaP `6.9489` edge `0.0282` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.5251` n `135` status `ready` deltaP `2.3397` edge `0.0689` maxDD `-7.2607`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
