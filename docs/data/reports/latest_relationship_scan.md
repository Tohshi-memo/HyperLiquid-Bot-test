# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T10:37:29.972881+00:00`
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

- `market_context_high->unknown_1h` score `341.0302` n `50` status `ready` deltaP `10.4251` edge `28.3546` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `288.7461` n `50` status `ready` deltaP `10.061` edge `23.9951` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.5394` n `73` status `ready` deltaP `39.795` edge `1.0506` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `10.4376` n `50` status `ready` deltaP `35.2986` edge `0.7761` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `10.4276` n `73` status `ready` deltaP `36.0516` edge `0.6771` maxDD `-2.8784`
- `market_context_high->crypto_alt_24h` score `9.0357` n `50` status `ready` deltaP `16.5347` edge `0.8137` maxDD `-11.6768`
- `market_context_high->crypto_major_4h` score `6.9527` n `50` status `ready` deltaP `17.3902` edge `0.5338` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.9069` n `50` status `ready` deltaP `15.2744` edge `0.4364` maxDD `-7.6792`
- `news_risk_high->crypto_alt_4h` score `4.4549` n `103` status `ready` deltaP `18.0899` edge `0.385` maxDD `-6.4152`
- `market_context_high->crypto_alt_1h` score `3.0021` n `50` status `ready` deltaP `14.3533` edge `0.2208` maxDD `-3.6387`
- `market_context_high->crypto_major_1h` score `2.9532` n `50` status `ready` deltaP `14.2994` edge `0.1958` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.9407` n `50` status `ready` deltaP `32.8415` edge `0.0396` maxDD `-0.0791`
- `market_context_high->equity_24h` score `2.6045` n `50` status `ready` deltaP `12.2708` edge `0.4383` maxDD `-11.8957`
- `news_risk_high->equity_4h` score `2.5797` n `103` status `ready` deltaP `24.0114` edge `0.1245` maxDD `-2.9013`
- `news_risk_high->crypto_major_24h` score `2.4492` n `73` status `ready` deltaP `9.463` edge `0.5663` maxDD `-15.8971`
- `market_context_high->fx_1h` score `1.4651` n `50` status `ready` deltaP `20.491` edge `0.0119` maxDD `-0.113`
- `news_risk_high->metal_24h` score `1.2985` n `73` status `ready` deltaP `12.8354` edge `0.2083` maxDD `-2.192`
- `news_risk_high->crypto_alt_1h` score `0.9387` n `113` status `ready` deltaP `5.8754` edge `0.0953` maxDD `-2.4998`
- `market_context_high->index_24h` score `0.9336` n `50` status `ready` deltaP `15.3125` edge `0.0747` maxDD `-1.2338`
- `news_risk_high->crypto_major_4h` score `0.8687` n `103` status `ready` deltaP `11.5261` edge `0.2655` maxDD `-10.477`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
