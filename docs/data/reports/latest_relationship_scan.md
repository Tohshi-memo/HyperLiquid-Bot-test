# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T11:52:26.742909+00:00`
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

- `market_context_high->unknown_1h` score `341.3842` n `50` status `ready` deltaP `10.8743` edge `28.3811` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `291.1315` n `50` status `ready` deltaP `10.8232` edge `24.1888` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.543` n `73` status `ready` deltaP `39.795` edge `1.0509` maxDD `-1.0093`
- `news_risk_high->equity_24h` score `10.1709` n `73` status `ready` deltaP `35.1836` edge `0.6615` maxDD `-2.8784`
- `market_context_high->crypto_major_24h` score `10.0706` n `50` status `ready` deltaP `34.4306` edge `0.7513` maxDD `-9.3299`
- `market_context_high->crypto_alt_24h` score `9.0393` n `50` status `ready` deltaP `16.5347` edge `0.814` maxDD `-11.6768`
- `market_context_high->crypto_major_4h` score `6.7417` n `50` status `ready` deltaP `16.628` edge `0.5213` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.7319` n `50` status `ready` deltaP `14.5122` edge `0.4269` maxDD `-7.6792`
- `news_risk_high->crypto_alt_4h` score `4.4034` n `108` status `ready` deltaP `18.5863` edge `0.3774` maxDD `-6.4152`
- `market_context_high->crypto_alt_1h` score `2.9877` n `50` status `ready` deltaP `14.2036` edge `0.2206` maxDD `-3.6387`
- `market_context_high->fx_4h` score `2.9455` n `50` status `ready` deltaP `32.8415` edge `0.04` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `2.9256` n `50` status `ready` deltaP `14.0` edge `0.1955` maxDD `-2.2692`
- `news_risk_high->equity_4h` score `2.4988` n `108` status `ready` deltaP `23.5095` edge `0.1211` maxDD `-2.9013`
- `market_context_high->equity_24h` score `2.4377` n `50` status `ready` deltaP `11.4028` edge `0.4227` maxDD `-11.8957`
- `news_risk_high->crypto_major_24h` score `2.2107` n `73` status `ready` deltaP `8.595` edge `0.5415` maxDD `-15.8971`
- `market_context_high->fx_1h` score `1.4915` n `50` status `ready` deltaP `20.7904` edge `0.0121` maxDD `-0.113`
- `news_risk_high->metal_24h` score `1.2522` n `73` status `ready` deltaP `12.1409` edge `0.207` maxDD `-2.192`
- `news_risk_high->crypto_major_4h` score `0.971` n `108` status `ready` deltaP `12.5169` edge `0.272` maxDD `-10.477`
- `market_context_high->index_24h` score `0.8933` n `50` status `ready` deltaP `14.7917` edge `0.073` maxDD `-1.2338`
- `news_risk_high->crypto_alt_1h` score `0.8286` n `116` status `ready` deltaP `5.1002` edge `0.0913` maxDD `-2.4998`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
