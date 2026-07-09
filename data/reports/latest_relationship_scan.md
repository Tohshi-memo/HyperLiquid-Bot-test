# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-09T05:52:30.321631+00:00`
- Price records: `672`
- Market context records: `6159`
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

- `news_risk_high->crypto_alt_24h` score `12.3059` n `30` status `ready` deltaP `42.4712` edge `0.7571` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `7.5226` n `30` status `ready` deltaP `66.2069` edge `0.1855` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.209` n `32` status `ready` deltaP `43.8068` edge `0.0633` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.428` n `32` status `ready` deltaP `29.1791` edge `0.0217` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.685` n `195` status `ready` deltaP `1.129` edge `0.2337` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.2382` n `32` status `ready` deltaP `13.2369` edge `0.1172` maxDD `-2.0691`
- `news_risk_high->crypto_major_24h` score `0.9541` n `30` status `ready` deltaP `14.023` edge `0.1068` maxDD `-4.2368`
- `news_risk_high->crypto_alt_1h` score `0.6441` n `32` status `ready` deltaP `8.4795` edge `0.0722` maxDD `-1.6923`
- `market_context_high->unknown_4h` score `0.0913` n `195` status `ready` deltaP `-0.9091` edge `0.2669` maxDD `-11.925`
- `market_context_high->equity_4h` score `0.0382` n `195` status `ready` deltaP `3.0303` edge `0.0747` maxDD `-2.671`
- `market_context_high->metal_24h` score `-0.0488` n `195` status `ready` deltaP `19.6331` edge `0.1197` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.2238` n `30` status `ready` deltaP `7.6436` edge `0.0075` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.2519` n `195` status `ready` deltaP `1.8714` edge `-0.0002` maxDD `-0.5659`
- `market_context_high->metal_4h` score `-0.5745` n `195` status `ready` deltaP `4.1842` edge `0.0172` maxDD `-3.4996`
- `news_risk_high->commodity_24h` score `-0.5979` n `30` status `ready` deltaP `13.9081` edge `-0.122` maxDD `-0.3101`
- `market_context_high->commodity_1h` score `-0.7171` n `195` status `ready` deltaP `-1.6839` edge `-0.0039` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.7733` n `32` status `ready` deltaP `-3.1343` edge `-0.0285` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.824` n `195` status `ready` deltaP `2.2503` edge `-0.0038` maxDD `-2.0564`
- `market_context_high->equity_1h` score `-0.8748` n `195` status `ready` deltaP `-1.7413` edge `0.011` maxDD `-4.2573`
- `market_context_high->crypto_alt_1h` score `-0.9318` n `195` status `ready` deltaP `3.4635` edge `0.0327` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
