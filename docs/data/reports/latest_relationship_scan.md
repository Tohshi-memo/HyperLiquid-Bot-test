# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T01:37:27.010390+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5392`

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

- `market_context_high->unknown_1h` score `106.6908` n `95` status `ready` deltaP `-0.23` edge `8.9339` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `60.6844` n `95` status `ready` deltaP `2.4743` edge `5.0717` maxDD `-0.4928`
- `market_context_high->crypto_major_24h` score `10.5503` n `50` status `ready` deltaP `30.6319` edge `0.6886` maxDD `-0.423`
- `market_context_high->crypto_alt_24h` score `10.0135` n `50` status `ready` deltaP `24.8889` edge `0.7305` maxDD `-2.9571`
- `news_risk_high->crypto_major_4h` score `9.56` n `65` status `ready` deltaP `33.3138` edge `0.5949` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.5262` n `65` status `ready` deltaP `21.1585` edge `0.5372` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `4.8461` n `65` status `ready` deltaP `16.7629` edge `0.3021` maxDD `-0.1344`
- `market_context_high->crypto_major_4h` score `4.4528` n `95` status `ready` deltaP `18.9008` edge `0.3154` maxDD `-3.294`
- `news_risk_high->index_24h` score `3.4979` n `65` status `ready` deltaP `24.4792` edge `0.1283` maxDD `0.0`
- `news_risk_high->equity_4h` score `2.958` n `65` status `ready` deltaP `21.7964` edge `0.1622` maxDD `-2.881`
- `news_risk_high->index_4h` score `2.946` n `65` status `ready` deltaP `32.371` edge `0.0559` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.6103` n `65` status `ready` deltaP `10.7646` edge `0.1813` maxDD `-1.5096`
- `market_context_high->crypto_major_1h` score `2.2186` n `95` status `ready` deltaP `15.1371` edge `0.129` maxDD `-2.2692`
- `news_risk_high->metal_4h` score `2.1403` n `65` status `ready` deltaP `19.5357` edge `0.0897` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.0974` n `65` status `ready` deltaP `25.9166` edge `0.017` maxDD `-0.1997`
- `market_context_high->equity_24h` score `1.6584` n `50` status `ready` deltaP `2.9167` edge `0.139` maxDD `-0.6196`
- `market_context_high->fx_24h` score `1.4684` n `50` status `ready` deltaP `26.6667` edge `0.1026` maxDD `-1.703`
- `market_context_high->fx_4h` score `1.4393` n `95` status `ready` deltaP `25.1717` edge `0.0278` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.4131` n `65` status `ready` deltaP `4.5693` edge `0.1392` maxDD `-2.4854`
- `market_context_high->crypto_alt_4h` score `1.4059` n `95` status `ready` deltaP `4.3164` edge `0.2673` maxDD `-7.6465`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
