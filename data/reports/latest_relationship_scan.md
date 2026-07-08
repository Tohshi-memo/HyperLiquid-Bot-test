# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T23:52:25.084290+00:00`
- Price records: `672`
- Market context records: `6137`
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

- `news_risk_high->crypto_alt_24h` score `10.9782` n `30` status `ready` deltaP `40.0347` edge `0.6627` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `7.7481` n `30` status `ready` deltaP `68.5764` edge `0.1885` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.3457` n `32` status `ready` deltaP `45.3506` edge `0.0644` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.4302` n `32` status `ready` deltaP `29.1916` edge `0.0218` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.4622` n `195` status `ready` deltaP `0.8046` edge `0.2173` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.1646` n `32` status `ready` deltaP `12.7807` edge `0.1108` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.58` n `32` status `ready` deltaP `8.0277` edge `0.067` maxDD `-1.6923`
- `market_context_high->equity_4h` score `0.3983` n `195` status `ready` deltaP `3.9024` edge `0.0989` maxDD `-2.671`
- `news_risk_high->index_24h` score `-0.1735` n `30` status `ready` deltaP `7.8472` edge `0.0126` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.2505` n `195` status `ready` deltaP `1.8839` edge `-0.0001` maxDD `-0.5659`
- `market_context_high->unknown_4h` score `-0.3895` n `195` status `ready` deltaP `-2.7643` edge `0.2392` maxDD `-11.925`
- `news_risk_high->crypto_major_24h` score `-0.4138` n `30` status `ready` deltaP `10.3819` edge `-0.0443` maxDD `-4.2368`
- `news_risk_high->commodity_24h` score `-0.5827` n `30` status `ready` deltaP `14.0973` edge `-0.122` maxDD `-0.3101`
- `market_context_high->metal_4h` score `-0.6241` n `195` status `ready` deltaP `3.6945` edge `0.0141` maxDD `-3.4996`
- `market_context_high->commodity_1h` score `-0.7727` n `195` status `ready` deltaP `-2.2885` edge `-0.0045` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.7933` n `32` status `ready` deltaP `-3.2934` edge `-0.03` maxDD `-1.6464`
- `market_context_high->metal_24h` score `-0.8494` n `195` status `ready` deltaP `15.8627` edge `0.0422` maxDD `-11.8809`
- `market_context_high->equity_1h` score `-0.8515` n `195` status `ready` deltaP `-1.1577` edge `0.0101` maxDD `-4.2573`
- `market_context_high->metal_1h` score `-0.8548` n `195` status `ready` deltaP `2.0912` edge `-0.0053` maxDD `-2.0564`
- `market_context_high->index_4h` score `-0.9941` n `195` status `ready` deltaP `0.3267` edge `0.0168` maxDD `-1.381`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
