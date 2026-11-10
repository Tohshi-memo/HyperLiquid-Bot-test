# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T23:22:36.654354+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11740`

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

- `market_context_high->unknown_4h` score `72.7751` n `88` status `ready` deltaP `7.525` edge `6.0592` maxDD `-0.9153`
- `market_context_high->equity_24h` score `35.2676` n `88` status `ready` deltaP `33.6489` edge `2.9551` maxDD `-16.9034`
- `market_context_high->crypto_alt_24h` score `6.8841` n `88` status `ready` deltaP `29.9874` edge `1.1921` maxDD `-33.4213`
- `market_context_high->index_24h` score `6.0546` n `88` status `ready` deltaP `31.1553` edge `0.3431` maxDD `-2.3671`
- `news_risk_high->equity_1h` score `2.7791` n `32` status `ready` deltaP `13.2485` edge `0.2148` maxDD `-3.7228`
- `market_context_high->metal_24h` score `2.3167` n `88` status `ready` deltaP `25.2999` edge `0.0797` maxDD `-1.4245`
- `news_risk_high->index_1h` score `0.9167` n `32` status `ready` deltaP `13.2485` edge `0.0182` maxDD `-0.4103`
- `news_risk_high->metal_1h` score `0.3895` n `32` status `ready` deltaP `8.7762` edge `-0.0006` maxDD `-0.3692`
- `news_risk_high->crypto_alt_1h` score `0.312` n `32` status `ready` deltaP `16.8413` edge `0.0215` maxDD `-6.1688`
- `news_risk_high->commodity_1h` score `0.1065` n `32` status `ready` deltaP `-2.3952` edge `0.0479` maxDD `-0.1782`
- `news_risk_high->crypto_major_1h` score `0.0881` n `32` status `ready` deltaP `16.6916` edge `0.0052` maxDD `-7.0808`
- `market_context_high->metal_1h` score `-0.3413` n `88` status `ready` deltaP `3.9467` edge `0.0129` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.356` n `88` status `ready` deltaP `3.2866` edge `0.0007` maxDD `-1.7935`
- `news_risk_high->fx_1h` score `-0.5062` n `32` status `ready` deltaP `-1.3473` edge `-0.0042` maxDD `-0.3199`
- `market_context_high->commodity_4h` score `-0.5911` n `88` status `ready` deltaP `2.4945` edge `0.0182` maxDD `-4.182`
- `market_context_high->index_4h` score `-0.5932` n `88` status `ready` deltaP `4.005` edge `-0.005` maxDD `-2.4871`
- `market_context_high->index_1h` score `-0.9745` n `88` status `ready` deltaP `-7.206` edge `0.0062` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.0371` n `88` status `ready` deltaP `-0.9007` edge `0.0114` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.233` n `88` status `ready` deltaP `-12.7109` edge `-0.0049` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.5348` n `88` status `ready` deltaP `-7.206` edge `0.0359` maxDD `-8.1039`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
