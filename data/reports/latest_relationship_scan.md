# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T11:07:28.326940+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4842`

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

- `market_context_high->unknown_1h` score `341.0962` n `50` status `ready` deltaP `10.4251` edge `28.3601` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `289.4953` n `50` status `ready` deltaP `10.3659` edge `24.0555` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.5478` n `73` status `ready` deltaP `39.795` edge `1.0513` maxDD `-1.0093`
- `news_risk_high->equity_24h` score `10.3266` n `73` status `ready` deltaP `35.7044` edge `0.671` maxDD `-2.8784`
- `market_context_high->crypto_major_24h` score `10.2958` n `50` status `ready` deltaP `34.9514` edge `0.7666` maxDD `-9.3299`
- `market_context_high->crypto_alt_24h` score `9.0441` n `50` status `ready` deltaP `16.5347` edge `0.8144` maxDD `-11.6768`
- `market_context_high->crypto_major_4h` score `6.8851` n `50` status `ready` deltaP `17.0854` edge `0.5302` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.8501` n `50` status `ready` deltaP `14.9695` edge `0.4337` maxDD `-7.6792`
- `news_risk_high->crypto_alt_4h` score `4.4431` n `105` status `ready` deltaP `18.3028` edge `0.3826` maxDD `-6.4152`
- `market_context_high->crypto_alt_1h` score `3.044` n `50` status `ready` deltaP `14.6527` edge `0.2223` maxDD `-3.6387`
- `market_context_high->crypto_major_1h` score `2.9652` n `50` status `ready` deltaP `14.2994` edge `0.1968` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.9431` n `50` status `ready` deltaP `32.8415` edge `0.0398` maxDD `-0.0791`
- `news_risk_high->equity_4h` score `2.6049` n `105` status `ready` deltaP `24.1318` edge `0.1258` maxDD `-2.9013`
- `market_context_high->equity_24h` score `2.5389` n `50` status `ready` deltaP `11.9236` edge `0.4322` maxDD `-11.8957`
- `news_risk_high->crypto_major_24h` score `2.3571` n `73` status `ready` deltaP `9.1158` edge `0.5568` maxDD `-15.8971`
- `market_context_high->fx_1h` score `1.4651` n `50` status `ready` deltaP `20.491` edge `0.0119` maxDD `-0.113`
- `news_risk_high->metal_24h` score `1.2749` n `73` status `ready` deltaP `12.4881` edge `0.2076` maxDD `-2.192`
- `market_context_high->index_24h` score `0.9289` n `50` status `ready` deltaP `15.3125` edge `0.0741` maxDD `-1.2338`
- `news_risk_high->crypto_major_4h` score `0.9029` n `105` status `ready` deltaP `11.9425` edge `0.2671` maxDD `-10.477`
- `news_risk_high->crypto_alt_1h` score `0.8562` n `115` status `ready` deltaP `5.1744` edge `0.0931` maxDD `-2.4998`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
