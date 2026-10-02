# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T02:07:27.386230+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6602`

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

- `market_context_high->unknown_1h` score `338.7912` n `50` status `ready` deltaP `9.5269` edge `28.174` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `287.9131` n `50` status `ready` deltaP `8.9939` edge `23.9328` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `18.7285` n `78` status `ready` deltaP `38.4081` edge `1.3256` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `11.0003` n `50` status `ready` deltaP `36.1667` edge `0.8172` maxDD `-9.3299`
- `market_context_high->crypto_alt_24h` score `7.2571` n `50` status `ready` deltaP `14.9722` edge `0.6759` maxDD `-11.6768`
- `market_context_high->crypto_major_4h` score `7.1123` n `50` status `ready` deltaP `18.3049` edge `0.541` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.8379` n `50` status `ready` deltaP `15.7317` edge `0.4276` maxDD `-7.6792`
- `news_risk_high->crypto_alt_4h` score `3.4892` n `91` status `ready` deltaP `13.8636` edge `0.3327` maxDD `-6.4152`
- `market_context_high->equity_24h` score `3.4838` n `50` status `ready` deltaP `17.8264` edge `0.514` maxDD `-11.8957`
- `market_context_high->crypto_major_1h` score `3.0323` n `50` status `ready` deltaP `14.8982` edge `0.1984` maxDD `-2.2692`
- `news_risk_high->equity_24h` score `2.9882` n `78` status `ready` deltaP `19.0572` edge `0.438` maxDD `-7.5558`
- `market_context_high->fx_4h` score `2.9009` n `50` status `ready` deltaP `32.689` edge `0.0373` maxDD `-0.0791`
- `market_context_high->crypto_alt_1h` score `2.8954` n `50` status `ready` deltaP `13.4551` edge `0.2179` maxDD `-3.6387`
- `news_risk_high->crypto_major_24h` score `2.8083` n `78` status `ready` deltaP `13.1411` edge `0.4618` maxDD `-15.8971`
- `news_risk_high->equity_4h` score `2.6052` n `91` status `ready` deltaP `23.3852` edge `0.1308` maxDD `-2.9013`
- `news_risk_high->commodity_24h` score `1.6146` n `78` status `ready` deltaP `25.9348` edge `0.1465` maxDD `-3.9922`
- `market_context_high->fx_1h` score `1.446` n `50` status `ready` deltaP `20.3413` edge `0.0113` maxDD `-0.113`
- `news_risk_high->metal_24h` score `1.3934` n `78` status `ready` deltaP `13.8355` edge `0.2138` maxDD `-2.192`
- `news_risk_high->index_24h` score `1.238` n `78` status `ready` deltaP `16.5866` edge `0.0404` maxDD `-0.4916`
- `market_context_high->index_24h` score `0.9214` n `50` status `ready` deltaP `14.7917` edge `0.0766` maxDD `-1.2338`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
