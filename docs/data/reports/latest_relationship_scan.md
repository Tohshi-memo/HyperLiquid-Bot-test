# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T01:52:25.291579+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11566`

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

- `market_context_high->unknown_24h` score `96.6444` n `88` status `ready` deltaP `4.9937` edge `8.0345` maxDD `-0.4609`
- `market_context_high->unknown_4h` score `94.0398` n `88` status `ready` deltaP `8.1347` edge `7.8272` maxDD `-0.9161`
- `news_risk_high->equity_24h` score `42.8664` n `43` status `ready` deltaP `35.6401` edge `3.3346` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `24.465` n `43` status `ready` deltaP `45.3167` edge `1.9332` maxDD `-12.7247`
- `market_context_high->equity_24h` score `18.6626` n `88` status `ready` deltaP `18.5946` edge `1.6704` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `11.2747` n `53` status `ready` deltaP `33.9536` edge `0.8254` maxDD `-6.9762`
- `news_risk_high->commodity_24h` score `6.6664` n `43` status `ready` deltaP `39.9654` edge `0.2891` maxDD `0.0`
- `news_risk_high->index_24h` score `6.4522` n `43` status `ready` deltaP `32.3529` edge `0.322` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `6.1937` n `88` status `ready` deltaP `34.9638` edge `1.0704` maxDD `-33.4213`
- `news_risk_high->crypto_alt_24h` score `5.1306` n `43` status `ready` deltaP `17.9448` edge `0.7626` maxDD `-14.2906`
- `market_context_high->metal_24h` score `4.8477` n `88` status `ready` deltaP `35.0071` edge `0.2259` maxDD `-1.4245`
- `news_risk_high->metal_4h` score `4.3329` n `53` status `ready` deltaP `41.6705` edge `0.1209` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `3.8788` n `53` status `ready` deltaP `20.7433` edge `0.3337` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.5142` n `53` status `ready` deltaP `18.3143` edge `0.242` maxDD `-3.6997`
- `market_context_high->index_24h` score `3.4959` n `88` status `ready` deltaP `18.7165` edge `0.2128` maxDD `-2.3671`
- `news_risk_high->commodity_4h` score `2.6078` n `53` status `ready` deltaP `23.815` edge `0.0839` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.1984` n `53` status `ready` deltaP `20.8985` edge `0.0875` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `2.1536` n `53` status `ready` deltaP `24.6692` edge `0.2755` maxDD `-10.1088`
- `news_risk_high->metal_1h` score `2.0432` n `53` status `ready` deltaP `24.5424` edge `0.0321` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3305` n `53` status `ready` deltaP `17.4754` edge `0.0245` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
