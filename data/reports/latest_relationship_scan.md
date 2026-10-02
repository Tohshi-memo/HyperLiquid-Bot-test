# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T19:37:49.959050+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4940`

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

- `market_context_high->unknown_1h` score `365.9338` n `50` status `ready` deltaP `10.8743` edge `30.4269` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `292.1545` n `50` status `ready` deltaP `10.3659` edge `24.2771` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.0854` n `73` status `ready` deltaP `40.8367` edge `1.0891` maxDD `-1.005`
- `market_context_high->crypto_alt_24h` score `9.76` n `50` status `ready` deltaP `17.5764` edge `0.8665` maxDD `-11.6271`
- `market_context_high->crypto_major_24h` score `9.0066` n `50` status `ready` deltaP `31.8264` edge `0.68` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `8.7986` n `73` status `ready` deltaP `31.3641` edge `0.5726` maxDD `-2.8784`
- `market_context_high->crypto_major_4h` score `7.4567` n `50` status `ready` deltaP `18.3049` edge `0.5697` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.6369` n `50` status `ready` deltaP `16.4939` edge `0.4887` maxDD `-7.6465`
- `news_risk_high->crypto_alt_4h` score `5.458` n `116` status `ready` deltaP `22.356` edge `0.4402` maxDD `-6.4195`
- `market_context_high->crypto_alt_1h` score `3.3837` n `50` status `ready` deltaP `15.4012` edge `0.2456` maxDD `-3.6376`
- `market_context_high->crypto_major_1h` score `3.1919` n `50` status `ready` deltaP `14.8982` edge `0.2117` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.7519` n `50` status `ready` deltaP `30.7073` edge `0.0381` maxDD `-0.0791`
- `news_risk_high->equity_4h` score `2.5095` n `116` status `ready` deltaP `22.0984` edge `0.1314` maxDD `-2.9013`
- `market_context_high->equity_24h` score `1.5456` n `50` status `ready` deltaP `7.5833` edge `0.3338` maxDD `-11.8957`
- `news_risk_high->crypto_major_24h` score `1.5191` n `73` status `ready` deltaP `5.9908` edge `0.4702` maxDD `-15.8971`
- `market_context_high->fx_1h` score `1.4591` n `50` status `ready` deltaP `20.491` edge `0.0114` maxDD `-0.113`
- `news_risk_high->crypto_major_4h` score `1.4163` n `116` status `ready` deltaP `14.9601` edge `0.3128` maxDD `-10.477`
- `news_risk_high->metal_24h` score `1.3519` n `73` status `ready` deltaP `13.009` edge `0.214` maxDD `-2.192`
- `news_risk_high->crypto_alt_1h` score `1.2362` n `116` status `ready` deltaP `6.2978` edge `0.1171` maxDD `-2.4854`
- `market_context_high->fx_24h` score `0.8358` n `50` status `ready` deltaP `17.9028` edge `0.0896` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
