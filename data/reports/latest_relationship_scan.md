# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T09:52:24.748163+00:00`
- Price records: `672`
- Market context records: `2958`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6954`

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

- `market_context_high->crypto_alt_24h` score `17.297` n `124` status `ready` deltaP `12.9593` edge `1.7467` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `8.6713` n `124` status `ready` deltaP `17.3667` edge `0.6533` maxDD `-1.7175`
- `market_context_high->equity_24h` score `8.0286` n `124` status `ready` deltaP `18.1676` edge `0.7483` maxDD `-12.6963`
- `market_context_high->commodity_24h` score `6.3492` n `124` status `ready` deltaP `25.4984` edge `0.4935` maxDD `-4.4176`
- `market_context_high->index_24h` score `3.2201` n `124` status `ready` deltaP `13.7881` edge `0.2745` maxDD `-2.5127`
- `market_context_high->equity_4h` score `3.0872` n `125` status `ready` deltaP `16.1683` edge `0.1999` maxDD `-1.7002`
- `market_context_high->crypto_alt_4h` score `2.4143` n `125` status `ready` deltaP `22.3841` edge `0.5081` maxDD `-30.8239`
- `market_context_high->unknown_4h` score `0.8748` n `125` status `ready` deltaP `6.8756` edge `0.1324` maxDD `-3.7602`
- `market_context_high->index_4h` score `0.6777` n `125` status `ready` deltaP `13.5049` edge `0.081` maxDD `-2.3986`
- `market_context_high->equity_1h` score `0.2041` n `125` status `ready` deltaP `2.8096` edge `0.0529` maxDD `-1.7034`
- `market_context_high->index_1h` score `0.0865` n `125` status `ready` deltaP `5.8036` edge `0.0218` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.2895` n `125` status `ready` deltaP `0.4048` edge `0.0039` maxDD `-0.1244`
- `market_context_high->crypto_alt_1h` score `-0.3557` n `125` status `ready` deltaP `5.8503` edge `0.0914` maxDD `-10.747`
- `market_context_high->commodity_1h` score `-0.5255` n `125` status `ready` deltaP `-0.8443` edge `0.0008` maxDD `-3.3365`
- `market_context_high->crypto_major_1h` score `-0.5627` n `125` status `ready` deltaP `4.8443` edge `0.07` maxDD `-9.622`
- `market_context_high->unknown_1h` score `-0.5859` n `125` status `ready` deltaP `2.3042` edge `0.0089` maxDD `-3.1801`
- `market_context_high->crypto_major_4h` score `-0.6394` n `125` status `ready` deltaP `11.7561` edge `0.3522` maxDD `-33.6701`
- `market_context_high->commodity_4h` score `-0.7356` n `125` status `ready` deltaP `6.1878` edge `0.0434` maxDD `-8.9839`
- `market_context_high->metal_1h` score `-0.7669` n `125` status `ready` deltaP `-1.2563` edge `-0.0012` maxDD `-3.4325`
- `market_context_high->fx_4h` score `-0.819` n `125` status `ready` deltaP `0.0183` edge `0.0095` maxDD `-0.5631`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
