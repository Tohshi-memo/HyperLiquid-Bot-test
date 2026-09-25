# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T02:22:31.217172+00:00`
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

- `market_context_high->unknown_1h` score `84.4088` n `47` status `ready` deltaP `9.3675` edge `6.9787` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `47.9225` n `47` status `ready` deltaP `30.4226` edge `3.83` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `31.3768` n `47` status `ready` deltaP `24.782` edge `2.4875` maxDD `-2.7051`
- `market_context_high->equity_24h` score `26.0062` n `47` status `ready` deltaP `34.7628` edge `1.971` maxDD `-2.1786`
- `market_context_high->index_24h` score `8.2489` n `47` status `ready` deltaP `38.7559` edge `0.442` maxDD `-0.3705`
- `news_risk_high->unknown_1h` score `8.0698` n `116` status `ready` deltaP `-0.1703` edge `0.6955` maxDD `-0.7504`
- `market_context_high->metal_24h` score `4.5152` n `47` status `ready` deltaP `38.0098` edge `0.1467` maxDD `-0.2401`
- `news_risk_high->commodity_24h` score `3.3372` n `62` status `ready` deltaP `31.0988` edge `0.1056` maxDD `-1.7857`
- `market_context_high->index_4h` score `2.9583` n `47` status `ready` deltaP `33.8739` edge `0.0361` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.4959` n `47` status `ready` deltaP `17.1445` edge `0.1355` maxDD `-1.3444`
- `news_risk_high->crypto_alt_1h` score `2.2813` n `116` status `ready` deltaP `12.3065` edge `0.159` maxDD `-1.7416`
- `news_risk_high->crypto_major_1h` score `1.7315` n `116` status `ready` deltaP `14.4023` edge `0.1042` maxDD `-2.4737`
- `news_risk_high->metal_1h` score `1.2876` n `116` status `ready` deltaP `17.0865` edge `0.0219` maxDD `-0.6142`
- `market_context_high->index_1h` score `0.9176` n `47` status `ready` deltaP `14.161` edge `0.0099` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.8623` n `47` status `ready` deltaP `10.8676` edge `0.0397` maxDD `-1.5564`
- `market_context_high->crypto_alt_4h` score `0.5253` n `47` status `ready` deltaP `7.4014` edge `0.0612` maxDD `-3.3417`
- `market_context_high->fx_1h` score `0.2853` n `47` status `ready` deltaP `8.0137` edge `0.006` maxDD `-0.1854`
- `news_risk_high->equity_1h` score `0.2152` n `116` status `ready` deltaP `5.255` edge `0.0409` maxDD `-2.6402`
- `news_risk_high->fx_4h` score `0.1537` n `104` status `ready` deltaP `10.1665` edge `0.0186` maxDD `-0.6668`
- `market_context_high->metal_1h` score `-0.0528` n `47` status `ready` deltaP `2.2296` edge `0.01` maxDD `-0.1976`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
