# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T03:52:30.795560+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11065`

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

- `market_context_high->unknown_1h` score `86.798` n `47` status `ready` deltaP `9.2178` edge `7.1788` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `48.5345` n `47` status `ready` deltaP `30.4226` edge `3.881` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `31.744` n `47` status `ready` deltaP `24.782` edge `2.5181` maxDD `-2.7051`
- `market_context_high->equity_24h` score `26.095` n `47` status `ready` deltaP `34.7628` edge `1.9784` maxDD `-2.1786`
- `market_context_high->index_24h` score `8.2827` n `47` status `ready` deltaP `39.1031` edge `0.4425` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.6297` n `47` status `ready` deltaP `39.0514` edge `0.1493` maxDD `-0.2401`
- `news_risk_high->commodity_24h` score `3.3294` n `56` status `ready` deltaP `30.5804` edge `0.1084` maxDD `-1.7857`
- `market_context_high->index_4h` score `2.9631` n `47` status `ready` deltaP `33.8739` edge `0.0365` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.5475` n `47` status `ready` deltaP `17.1445` edge `0.1398` maxDD `-1.3444`
- `news_risk_high->crypto_alt_1h` score `1.0696` n `116` status `ready` deltaP `10.1693` edge `0.1124` maxDD `-4.2849`
- `market_context_high->index_1h` score `0.9343` n `47` status `ready` deltaP `14.3107` edge `0.0103` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.9259` n `47` status `ready` deltaP `11.3167` edge `0.042` maxDD `-1.5564`
- `news_risk_high->crypto_major_1h` score `0.9244` n `116` status `ready` deltaP `10.8404` edge `0.0701` maxDD `-3.2271`
- `news_risk_high->metal_1h` score `0.7893` n `116` status `ready` deltaP `12.8123` edge `0.0172` maxDD `-0.6142`
- `market_context_high->crypto_alt_4h` score `0.77` n `47` status `ready` deltaP `8.316` edge `0.0755` maxDD `-3.3417`
- `market_context_high->fx_1h` score `0.3679` n `47` status `ready` deltaP `8.9119` edge `0.0069` maxDD `-0.1854`
- `market_context_high->metal_1h` score `0.0009` n `47` status `ready` deltaP `3.1278` edge `0.0109` maxDD `-0.1976`
- `news_risk_high->equity_1h` score `-0.0854` n `116` status `ready` deltaP `3.1179` edge `0.0301` maxDD `-2.6402`
- `market_context_high->crypto_major_1h` score `-0.1912` n `47` status `ready` deltaP `1.9079` edge `0.0531` maxDD `-4.5405`
- `news_risk_high->fx_4h` score `-0.2521` n `104` status `ready` deltaP `6.9301` edge `0.0105` maxDD `-1.4552`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
