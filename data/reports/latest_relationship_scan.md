# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T09:22:29.730004+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11488`

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

- `market_context_high->unknown_4h` score `81.976` n `88` status `ready` deltaP `7.9823` edge `6.8229` maxDD `-0.9161`
- `market_context_high->equity_24h` score `33.167` n `88` status `ready` deltaP `29.8295` edge `2.8042` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `12.9992` n `48` status `ready` deltaP `37.1951` edge `0.9475` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `8.8431` n `88` status `ready` deltaP `35.8901` edge `1.4039` maxDD `-33.4213`
- `market_context_high->index_24h` score `5.9573` n `88` status `ready` deltaP `29.94` edge `0.3431` maxDD `-2.3671`
- `market_context_high->metal_24h` score `4.1317` n `88` status `ready` deltaP `31.2026` edge `0.1916` maxDD `-1.4245`
- `news_risk_high->crypto_major_4h` score `3.7517` n `48` status `ready` deltaP `22.4085` edge `0.312` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.6129` n `52` status `ready` deltaP `17.8835` edge `0.2531` maxDD `-3.6997`
- `news_risk_high->metal_4h` score `3.5144` n `48` status `ready` deltaP `35.2643` edge `0.0954` maxDD `-1.0104`
- `news_risk_high->commodity_4h` score `3.2727` n `48` status `ready` deltaP `26.5752` edge `0.1209` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.9454` n `48` status `ready` deltaP `27.8963` edge `0.1031` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `2.1743` n `48` status `ready` deltaP `27.0326` edge `0.2624` maxDD `-10.1088`
- `news_risk_high->metal_1h` score `1.5971` n `52` status `ready` deltaP `20.1059` edge `0.0245` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.4242` n `52` status `ready` deltaP `18.4823` edge `0.0256` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.7908` n `52` status `ready` deltaP `18.2519` edge `0.0494` maxDD `-7.0808`
- `news_risk_high->crypto_alt_1h` score `0.583` n `52` status `ready` deltaP `17.9525` edge `0.053` maxDD `-6.1688`
- `news_risk_high->commodity_1h` score `-0.1732` n `52` status `ready` deltaP `-2.5449` edge `0.036` maxDD `-0.3438`
- `market_context_high->metal_1h` score `-0.3508` n `88` status `ready` deltaP `3.4976` edge `0.0151` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.3731` n `88` status `ready` deltaP `3.1369` edge `-0.0005` maxDD `-1.7935`
- `market_context_high->index_4h` score `-0.7101` n `88` status `ready` deltaP `2.3281` edge `-0.0088` maxDD `-2.4871`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
