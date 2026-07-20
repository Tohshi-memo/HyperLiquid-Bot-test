# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-20T22:52:31.840223+00:00`
- Price records: `672`
- Market context records: `7399`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14677`

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

- `risk_on_high->crypto_major_4h` score `6.3072` n `32` status `ready` deltaP `36.2043` edge `0.3035` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `6.3072` n `32` status `ready` deltaP `36.2043` edge `0.3035` maxDD `-0.8742`
- `risk_on_high->unknown_4h` score `4.9269` n `32` status `ready` deltaP `15.5488` edge `0.3499` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `4.9269` n `32` status `ready` deltaP `15.5488` edge `0.3499` maxDD `-0.4384`
- `risk_on_high->crypto_alt_4h` score `4.7638` n `32` status `ready` deltaP `27.6677` edge `0.2369` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `4.7638` n `32` status `ready` deltaP `27.6677` edge `0.2369` maxDD `-0.9492`
- `risk_on_high->crypto_major_1h` score `1.1131` n `32` status `ready` deltaP `19.3301` edge `0.0383` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.1131` n `32` status `ready` deltaP `19.3301` edge `0.0383` maxDD `-0.957`
- `risk_on_high->commodity_1h` score `0.3856` n `32` status `ready` deltaP `5.1989` edge `0.0254` maxDD `-0.2339`
- `risk_on_and_context->commodity_1h` score `0.3856` n `32` status `ready` deltaP `5.1989` edge `0.0254` maxDD `-0.2339`
- `risk_on_high->equity_1h` score `0.1694` n `32` status `ready` deltaP `4.0541` edge `0.0324` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.1694` n `32` status `ready` deltaP `4.0541` edge `0.0324` maxDD `-1.3497`
- `risk_on_high->crypto_alt_1h` score `-0.0348` n `32` status `ready` deltaP `-0.4491` edge `0.0356` maxDD `-0.9651`
- `risk_on_and_context->crypto_alt_1h` score `-0.0348` n `32` status `ready` deltaP `-0.4491` edge `0.0356` maxDD `-0.9651`
- `market_context_high->fx_1h` score `-0.1561` n `132` status `ready` deltaP `4.3817` edge `-0.0001` maxDD `-0.5967`
- `risk_on_high->metal_4h` score `-0.1594` n `32` status `ready` deltaP `-0.3049` edge `0.0711` maxDD `-0.5882`
- `risk_on_and_context->metal_4h` score `-0.1594` n `32` status `ready` deltaP `-0.3049` edge `0.0711` maxDD `-0.5882`
- `market_context_high->commodity_1h` score `-0.5368` n `132` status `ready` deltaP `-1.0511` edge `-0.0046` maxDD `-1.5775`
- `market_context_high->unknown_4h` score `-0.8169` n `132` status `ready` deltaP `3.9958` edge `0.1045` maxDD `-6.2031`
- `market_context_high->commodity_4h` score `-0.9543` n `132` status `ready` deltaP `1.0217` edge `0.0105` maxDD `-2.4139`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
