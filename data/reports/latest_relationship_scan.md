# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T23:56:03.716418+00:00`
- Price records: `672`
- Market context records: `6138`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11131`

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

- `news_risk_high->crypto_alt_24h` score `10.9758` n `30` status `ready` deltaP `40.0347` edge `0.6625` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `7.7481` n `30` status `ready` deltaP `68.5764` edge `0.1885` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.3457` n `32` status `ready` deltaP `45.3506` edge `0.0644` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.4302` n `32` status `ready` deltaP `29.1916` edge `0.0218` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.461` n `195` status `ready` deltaP `0.8046` edge `0.2172` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.1638` n `32` status `ready` deltaP `12.7807` edge `0.1107` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.5785` n `32` status `ready` deltaP `8.0277` edge `0.0668` maxDD `-1.6923`
- `market_context_high->equity_4h` score `0.3971` n `195` status `ready` deltaP `3.9024` edge `0.0988` maxDD `-2.671`
- `news_risk_high->index_24h` score `-0.1743` n `30` status `ready` deltaP `7.8472` edge `0.0125` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.2505` n `195` status `ready` deltaP `1.8839` edge `-0.0001` maxDD `-0.5659`
- `market_context_high->unknown_4h` score `-0.3895` n `195` status `ready` deltaP `-2.7643` edge `0.2392` maxDD `-11.925`
- `news_risk_high->crypto_major_24h` score `-0.4145` n `30` status `ready` deltaP `10.3819` edge `-0.0444` maxDD `-4.2368`
- `news_risk_high->commodity_24h` score `-0.5827` n `30` status `ready` deltaP `14.0973` edge `-0.122` maxDD `-0.3101`
- `market_context_high->metal_4h` score `-0.6241` n `195` status `ready` deltaP `3.6945` edge `0.0141` maxDD `-3.4996`
- `market_context_high->commodity_1h` score `-0.7727` n `195` status `ready` deltaP `-2.2885` edge `-0.0045` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.8018` n `32` status `ready` deltaP `-3.4431` edge `-0.0301` maxDD `-1.6464`
- `market_context_high->metal_24h` score `-0.8494` n `195` status `ready` deltaP `15.8627` edge `0.0422` maxDD `-11.8809`
- `market_context_high->equity_1h` score `-0.8523` n `195` status `ready` deltaP `-1.1577` edge `0.01` maxDD `-4.2573`
- `market_context_high->metal_1h` score `-0.8679` n `195` status `ready` deltaP `1.9415` edge `-0.0054` maxDD `-2.0564`
- `market_context_high->crypto_alt_1h` score `-0.9974` n `195` status `ready` deltaP `3.0117` edge `0.0273` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
