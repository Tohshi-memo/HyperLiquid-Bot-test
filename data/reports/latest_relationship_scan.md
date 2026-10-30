# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T15:52:28.335007+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7030`

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

- `market_context_high->unknown_24h` score `1611.2662` n `134` status `ready` deltaP `-3.4852` edge `134.3384` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `183.5868` n `57` status `ready` deltaP `-0.0053` edge `15.3115` maxDD `-0.3382`
- `market_context_high->unknown_4h` score `31.719` n `134` status `ready` deltaP `1.0261` edge `2.6497` maxDD `-0.3966`
- `news_risk_high->crypto_alt_4h` score `7.4196` n `45` status `ready` deltaP `21.416` edge `0.5152` maxDD `-1.5072`
- `market_context_high->equity_24h` score `3.8009` n `134` status `ready` deltaP `16.6589` edge `0.4814` maxDD `-14.0571`
- `market_context_high->index_24h` score `3.4606` n `134` status `ready` deltaP `35.2638` edge `0.0716` maxDD `-0.1315`
- `news_risk_high->crypto_alt_1h` score `1.4757` n `57` status `ready` deltaP `9.0267` edge `0.1339` maxDD `-3.3547`
- `market_context_high->metal_1h` score `0.4132` n `134` status `ready` deltaP `11.3527` edge `0.0152` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.3772` n `134` status `ready` deltaP `15.9834` edge `0.0314` maxDD `-1.8344`
- `market_context_high->equity_1h` score `0.3277` n `134` status `ready` deltaP `5.53` edge `0.078` maxDD `-2.3383`
- `news_risk_high->commodity_4h` score `0.2289` n `45` status `ready` deltaP `1.1755` edge `0.045` maxDD `-0.7008`
- `market_context_high->commodity_4h` score `0.2111` n `134` status `ready` deltaP `13.4806` edge `0.0496` maxDD `-1.0837`
- `market_context_high->crypto_major_1h` score `0.0672` n `134` status `ready` deltaP `7.6146` edge `0.0576` maxDD `-5.2213`
- `market_context_high->equity_4h` score `-0.0226` n `134` status `ready` deltaP `3.3059` edge `0.1335` maxDD `-6.008`
- `market_context_high->fx_1h` score `-0.0676` n `134` status `ready` deltaP `4.1782` edge `-0.0007` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.3248` n `134` status `ready` deltaP `1.6445` edge `0.0134` maxDD `-0.4475`
- `news_risk_high->index_1h` score `-0.4548` n `57` status `ready` deltaP `2.4399` edge `-0.0043` maxDD `-0.622`
- `market_context_high->fx_4h` score `-0.503` n `134` status `ready` deltaP `-0.3208` edge `-0.0025` maxDD `-0.4545`
- `market_context_high->index_1h` score `-0.8162` n `134` status `ready` deltaP `-1.9461` edge `0.0008` maxDD `-1.1344`
- `market_context_high->crypto_alt_1h` score `-0.8547` n `134` status `ready` deltaP `3.1482` edge `0.0559` maxDD `-8.251`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
