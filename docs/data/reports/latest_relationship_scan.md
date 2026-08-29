# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T00:37:24.622516+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11666`

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

- `news_risk_high->unknown_24h` score `56.3005` n `50` status `ready` deltaP `17.851` edge `4.5727` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `34.5143` n `50` status `ready` deltaP `46.6066` edge `2.6096` maxDD `-2.8629`
- `news_risk_high->crypto_major_24h` score `9.0471` n `50` status `ready` deltaP `26.2877` edge `0.628` maxDD `-2.6128`
- `news_risk_high->unknown_4h` score `8.7495` n `71` status `ready` deltaP `17.5863` edge `0.6429` maxDD `-1.4812`
- `news_risk_high->equity_24h` score `6.7231` n `50` status `ready` deltaP `30.1005` edge `0.4524` maxDD `-4.7584`
- `market_context_high->unknown_24h` score `5.6092` n `120` status `ready` deltaP `11.1843` edge `0.4661` maxDD `-3.1917`
- `news_risk_high->metal_24h` score `4.4682` n `50` status `ready` deltaP `43.4073` edge `0.0872` maxDD `-0.0053`
- `news_risk_high->unknown_1h` score `3.2995` n `72` status `ready` deltaP `7.959` edge `0.2576` maxDD `-0.8558`
- `market_context_high->metal_24h` score `3.2854` n `120` status `ready` deltaP `28.7406` edge `0.1841` maxDD `-3.1535`
- `news_risk_high->index_24h` score `2.4382` n `50` status `ready` deltaP `26.9948` edge `0.0383` maxDD `-0.2064`
- `news_risk_high->fx_4h` score `2.2211` n `71` status `ready` deltaP `32.6112` edge `0.0226` maxDD `-0.3931`
- `market_context_high->unknown_4h` score `2.1921` n `120` status `ready` deltaP `17.246` edge `0.1084` maxDD `-0.5894`
- `market_context_high->unknown_1h` score `0.9108` n `120` status `ready` deltaP `8.7924` edge `0.0623` maxDD `-1.6015`
- `news_risk_high->fx_1h` score `0.5493` n `72` status `ready` deltaP `11.818` edge `0.0058` maxDD `-0.1052`
- `news_risk_high->commodity_1h` score `0.3274` n `72` status `ready` deltaP `10.6204` edge `0.0032` maxDD `-0.5618`
- `market_context_high->metal_4h` score `0.0159` n `120` status `ready` deltaP `12.0833` edge `0.0132` maxDD `-3.3377`
- `market_context_high->fx_1h` score `-0.3795` n `120` status `ready` deltaP `3.7625` edge `-0.0005` maxDD `-0.8587`
- `news_risk_high->index_1h` score `-0.3997` n `72` status `ready` deltaP `0.2329` edge `-0.0094` maxDD `-0.8054`
- `market_context_high->crypto_alt_4h` score `-0.6518` n `120` status `ready` deltaP `15.7723` edge `0.2959` maxDD `-31.4361`
- `news_risk_high->metal_1h` score `-0.6853` n `72` status `ready` deltaP `-0.5988` edge `-0.0263` maxDD `-2.605`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
