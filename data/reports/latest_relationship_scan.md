# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T03:07:31.771067+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11041`

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

- `market_context_high->unknown_1h` score `86.7728` n `47` status `ready` deltaP `9.3675` edge `7.1757` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `48.2657` n `47` status `ready` deltaP `30.4226` edge `3.8586` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `31.6012` n `47` status `ready` deltaP `24.782` edge `2.5062` maxDD `-2.7051`
- `market_context_high->equity_24h` score `26.0686` n `47` status `ready` deltaP `34.7628` edge `1.9762` maxDD `-2.1786`
- `market_context_high->index_24h` score `8.2827` n `47` status `ready` deltaP `39.1031` edge `0.4425` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.5724` n `47` status `ready` deltaP `38.5306` edge `0.148` maxDD `-0.2401`
- `news_risk_high->commodity_24h` score `3.3368` n `59` status `ready` deltaP `30.8528` edge `0.1072` maxDD `-1.7857`
- `market_context_high->index_4h` score `2.9619` n `47` status `ready` deltaP `33.8739` edge `0.0364` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.5319` n `47` status `ready` deltaP `17.1445` edge `0.1385` maxDD `-1.3444`
- `news_risk_high->crypto_alt_1h` score `1.4706` n `116` status `ready` deltaP `10.1693` edge `0.1206` maxDD `-2.9342`
- `news_risk_high->crypto_major_1h` score `1.2678` n `116` status `ready` deltaP `12.2651` edge `0.0798` maxDD `-2.4737`
- `news_risk_high->metal_1h` score `1.0866` n `116` status `ready` deltaP `14.9494` edge `0.0194` maxDD `-0.6142`
- `market_context_high->index_1h` score `0.9343` n `47` status `ready` deltaP `14.3107` edge `0.0103` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.9103` n `47` status `ready` deltaP `11.167` edge `0.0417` maxDD `-1.5564`
- `market_context_high->crypto_alt_4h` score `0.659` n `47` status `ready` deltaP `7.8587` edge `0.0693` maxDD `-3.3417`
- `market_context_high->fx_1h` score `0.3296` n `47` status `ready` deltaP `8.4628` edge `0.0067` maxDD `-0.1854`
- `news_risk_high->fx_4h` score `0.0031` n `104` status `ready` deltaP `8.5483` edge `0.0142` maxDD `-0.997`
- `news_risk_high->equity_1h` score `-0.0092` n `116` status `ready` deltaP `3.8303` edge `0.0317` maxDD `-2.6402`
- `market_context_high->metal_1h` score `-0.0256` n `47` status `ready` deltaP `2.6787` edge `0.0105` maxDD `-0.1976`
- `market_context_high->crypto_major_1h` score `-0.2404` n `47` status `ready` deltaP `1.6085` edge `0.051` maxDD `-4.5405`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
