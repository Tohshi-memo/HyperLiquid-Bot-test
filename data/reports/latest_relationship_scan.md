# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T08:22:30.245043+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4806`

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

- `market_context_high->unknown_1h` score `366.1414` n `50` status `ready` deltaP `10.8743` edge `30.4442` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `293.8078` n `50` status `ready` deltaP `12.0427` edge `24.4037` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `12.3964` n `50` status `ready` deltaP `25.7361` edge `1.0318` maxDD `-11.6271`
- `news_risk_high->equity_24h` score `10.6902` n `70` status `ready` deltaP `32.4801` edge `0.7228` maxDD `-2.8784`
- `market_context_high->crypto_major_24h` score `9.8456` n `50` status `ready` deltaP `33.3889` edge `0.7395` maxDD `-9.3299`
- `news_risk_high->crypto_major_4h` score `9.5995` n `76` status `ready` deltaP `36.5372` edge `0.5767` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.5815` n `76` status `ready` deltaP `30.1508` edge `0.5652` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.3959` n `50` status `ready` deltaP `17.6951` edge `0.5687` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `6.1359` n `50` status `ready` deltaP `17.2561` edge `0.5252` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.2204` n `70` status `ready` deltaP `33.0407` edge `0.1473` maxDD `-0.2696`
- `news_risk_high->equity_4h` score `3.9601` n `76` status `ready` deltaP `30.1909` edge `0.19` maxDD `-2.9013`
- `market_context_high->crypto_alt_1h` score `3.3309` n `50` status `ready` deltaP `15.2515` edge `0.2422` maxDD `-3.6376`
- `market_context_high->crypto_major_1h` score `3.0121` n `50` status `ready` deltaP `13.7006` edge `0.2047` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.9189` n `50` status `ready` deltaP `32.689` edge `0.0388` maxDD `-0.0791`
- `news_risk_high->crypto_major_1h` score `2.8147` n `76` status `ready` deltaP `14.1743` edge `0.1756` maxDD `-1.5096`
- `news_risk_high->metal_4h` score `2.1992` n `76` status `ready` deltaP `19.087` edge `0.0976` maxDD `-0.993`
- `news_risk_high->index_4h` score `2.1963` n `76` status `ready` deltaP `25.3289` edge `0.0487` maxDD `-0.4296`
- `news_risk_high->crypto_alt_1h` score `1.7657` n `76` status `ready` deltaP `7.1462` edge `0.1514` maxDD `-2.4854`
- `market_context_high->fx_1h` score `1.4232` n `50` status `ready` deltaP `20.0419` edge `0.0114` maxDD `-0.113`
- `market_context_high->fx_24h` score `1.2933` n `50` status `ready` deltaP `25.0208` edge `0.1008` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
