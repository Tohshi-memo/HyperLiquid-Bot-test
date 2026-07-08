# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T11:22:25.692410+00:00`
- Price records: `672`
- Market context records: `6081`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11147`

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

- `news_risk_high->fx_24h` score `8.1606` n `30` status `ready` deltaP `72.7431` edge `0.1951` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `5.1754` n `30` status `ready` deltaP `31.3541` edge `0.237` maxDD `-0.5131`
- `news_risk_high->fx_4h` score `4.3309` n `32` status `ready` deltaP `45.0457` edge `0.0652` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.4458` n `32` status `ready` deltaP `29.3413` edge `0.0221` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.8943` n `204` status `ready` deltaP `9.8368` edge `0.184` maxDD `-2.671`
- `news_risk_high->crypto_major_1h` score `1.1295` n `32` status `ready` deltaP `13.0801` edge `0.1043` maxDD `-2.0691`
- `news_risk_high->commodity_24h` score `0.7584` n `30` status `ready` deltaP `19.132` edge `-0.0438` maxDD `-0.3101`
- `news_risk_high->crypto_alt_1h` score `0.6267` n `32` status `ready` deltaP `8.9259` edge `0.067` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.1008` n `30` status `ready` deltaP `9.2361` edge `0.0385` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.3169` n `204` status `ready` deltaP `4.2357` edge `0.011` maxDD `-2.0564`
- `market_context_high->fx_1h` score `-0.4719` n `204` status `ready` deltaP `0.9099` edge `-0.0005` maxDD `-0.5916`
- `market_context_high->equity_1h` score `-0.5205` n `204` status `ready` deltaP `2.043` edge `0.0312` maxDD `-4.2573`
- `market_context_high->metal_4h` score `-0.617` n `204` status `ready` deltaP `5.3294` edge `0.0318` maxDD `-3.4996`
- `news_risk_high->metal_1h` score `-0.7147` n `32` status `ready` deltaP `-1.6467` edge `-0.0309` maxDD `-1.6464`
- `market_context_high->crypto_alt_1h` score `-0.7402` n `204` status `ready` deltaP `4.9431` edge `0.0474` maxDD `-9.3536`
- `market_context_high->commodity_1h` score `-0.7546` n `204` status `ready` deltaP `-1.9872` edge `-0.005` maxDD `-0.5708`
- `market_context_high->crypto_major_1h` score `-0.8026` n `204` status `ready` deltaP `4.808` edge `0.0418` maxDD `-9.807`
- `market_context_high->index_4h` score `-0.8039` n `204` status `ready` deltaP `2.8007` edge `0.0271` maxDD `-1.573`
- `news_risk_high->index_1h` score `-0.9683` n `32` status `ready` deltaP `-7.7283` edge `-0.0163` maxDD `-1.1725`
- `market_context_high->index_1h` score `-1.1598` n `204` status `ready` deltaP `-1.7847` edge `0.0044` maxDD `-1.1324`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
