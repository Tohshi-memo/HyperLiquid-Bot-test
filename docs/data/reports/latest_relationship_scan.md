# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T11:37:26.566067+00:00`
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

- `market_context_high->unknown_1h` score `341.2966` n `50` status `ready` deltaP `10.7246` edge `28.3748` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `290.8037` n `50` status `ready` deltaP `10.6707` edge `24.1625` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.5406` n `73` status `ready` deltaP `39.795` edge `1.0507` maxDD `-1.0093`
- `news_risk_high->equity_24h` score `10.2208` n `73` status `ready` deltaP `35.3572` edge `0.6645` maxDD `-2.8784`
- `market_context_high->crypto_major_24h` score `10.1397` n `50` status `ready` deltaP `34.6042` edge `0.7559` maxDD `-9.3299`
- `market_context_high->crypto_alt_24h` score `9.0369` n `50` status `ready` deltaP `16.5347` edge `0.8138` maxDD `-11.6768`
- `market_context_high->crypto_major_4h` score `6.7947` n `50` status `ready` deltaP `16.7805` edge `0.5247` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.7741` n `50` status `ready` deltaP `14.6646` edge `0.4294` maxDD `-7.6792`
- `news_risk_high->crypto_alt_4h` score `4.443` n `107` status `ready` deltaP `18.4964` edge `0.3813` maxDD `-6.4152`
- `market_context_high->crypto_alt_1h` score `3.0033` n `50` status `ready` deltaP `14.3533` edge `0.2209` maxDD `-3.6387`
- `market_context_high->fx_4h` score `2.9443` n `50` status `ready` deltaP `32.8415` edge `0.0399` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `2.94` n `50` status `ready` deltaP `14.1497` edge `0.1957` maxDD `-2.2692`
- `news_risk_high->equity_4h` score `2.5977` n `107` status `ready` deltaP `24.2364` edge `0.1245` maxDD `-2.9013`
- `market_context_high->equity_24h` score `2.4701` n `50` status `ready` deltaP `11.5764` edge `0.4257` maxDD `-11.8957`
- `news_risk_high->crypto_major_24h` score `2.2556` n `73` status `ready` deltaP `8.7686` edge `0.5461` maxDD `-15.8971`
- `market_context_high->fx_1h` score `1.4783` n `50` status `ready` deltaP `20.6407` edge `0.012` maxDD `-0.113`
- `news_risk_high->metal_24h` score `1.2522` n `73` status `ready` deltaP `12.1409` edge `0.207` maxDD `-2.192`
- `news_risk_high->crypto_major_4h` score `0.9614` n `107` status `ready` deltaP `12.3319` edge `0.272` maxDD `-10.477`
- `market_context_high->index_24h` score `0.9046` n `50` status `ready` deltaP `14.9653` edge `0.0733` maxDD `-1.2338`
- `news_risk_high->crypto_alt_1h` score `0.8442` n `116` status `ready` deltaP `5.2499` edge `0.0916` maxDD `-2.4998`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
