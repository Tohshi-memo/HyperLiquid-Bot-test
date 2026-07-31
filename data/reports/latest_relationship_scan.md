# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T07:07:33.226545+00:00`
- Price records: `672`
- Market context records: `8491`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5871`

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

- `news_risk_high->unknown_24h` score `6271.3961` n `52` status `ready` deltaP `44.0438` edge `522.3648` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.0596` n `64` status `ready` deltaP `22.1799` edge `0.4168` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.0363` n `64` status `ready` deltaP `16.8064` edge `0.0767` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.7326` n `64` status `ready` deltaP `15.9525` edge `0.0857` maxDD `-2.4803`
- `news_risk_high->crypto_alt_4h` score `1.0253` n `64` status `ready` deltaP `15.2439` edge `0.169` maxDD `-5.8012`
- `news_risk_high->crypto_major_4h` score `0.9704` n `64` status `ready` deltaP `5.8308` edge `0.1631` maxDD `-3.5385`
- `news_risk_high->crypto_alt_1h` score `0.6323` n `64` status `ready` deltaP `10.2077` edge `0.0657` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3602` n `64` status `ready` deltaP `7.064` edge `0.0503` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.1695` n `64` status `ready` deltaP `6.7833` edge `0.0046` maxDD `-0.2475`
- `news_risk_high->fx_4h` score `0.0682` n `64` status `ready` deltaP `12.0808` edge `0.0209` maxDD `-0.6604`
- `news_risk_high->index_1h` score `0.0122` n `64` status `ready` deltaP `3.7706` edge `0.0081` maxDD `-0.5338`
- `news_risk_high->metal_4h` score `-0.1636` n `64` status `ready` deltaP `-0.1143` edge `0.0274` maxDD `-0.8085`
- `news_risk_high->metal_1h` score `-0.2389` n `64` status `ready` deltaP `2.2081` edge `0.0057` maxDD `-0.5599`
- `news_risk_high->commodity_1h` score `-1.604` n `64` status `ready` deltaP `-3.4057` edge `-0.0324` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.5381` n `52` status `ready` deltaP `-27.7244` edge `-0.0445` maxDD `-5.2413`
- `news_risk_high->commodity_4h` score `-7.5845` n `64` status `ready` deltaP `-20.0076` edge `-0.1659` maxDD `-13.2872`
- `news_risk_high->metal_24h` score `-9.4064` n `52` status `ready` deltaP `-36.6186` edge `-0.2627` maxDD `-10.8302`
- `news_risk_high->commodity_24h` score `-12.9414` n `52` status `ready` deltaP `-13.3013` edge `-0.3958` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-15.0001` n `52` status `ready` deltaP `-37.4466` edge `-0.4501` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-41.1908` n `52` status `ready` deltaP `-32.7857` edge `-1.7615` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
