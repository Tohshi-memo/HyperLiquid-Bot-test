# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T16:07:30.580270+00:00`
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

- `market_context_high->unknown_24h` score `1610.2852` n `134` status `ready` deltaP `-3.6588` edge `134.2578` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `176.3774` n `58` status `ready` deltaP `0.0567` edge `14.7103` maxDD `-0.3382`
- `market_context_high->unknown_4h` score `31.7718` n `134` status `ready` deltaP `1.0261` edge `2.6541` maxDD `-0.3966`
- `news_risk_high->crypto_alt_4h` score `7.3988` n `46` status `ready` deltaP `21.8915` edge `0.5103` maxDD `-1.5072`
- `market_context_high->equity_24h` score `3.9029` n `134` status `ready` deltaP `16.6589` edge `0.4899` maxDD `-14.0571`
- `market_context_high->index_24h` score `3.4678` n `134` status `ready` deltaP `35.2638` edge `0.0722` maxDD `-0.1315`
- `news_risk_high->crypto_alt_1h` score `1.3491` n `58` status `ready` deltaP `8.2387` edge `0.1286` maxDD `-3.3547`
- `market_context_high->metal_1h` score `0.414` n `134` status `ready` deltaP `11.3527` edge `0.0153` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.3788` n `134` status `ready` deltaP `15.9834` edge `0.0316` maxDD `-1.8344`
- `market_context_high->equity_1h` score `0.3385` n `134` status `ready` deltaP `5.53` edge `0.0789` maxDD `-2.3383`
- `news_risk_high->commodity_4h` score `0.325` n `46` status `ready` deltaP `2.2866` edge `0.0456` maxDD `-0.7008`
- `market_context_high->commodity_4h` score `0.2135` n `134` status `ready` deltaP `13.4806` edge `0.0498` maxDD `-1.0837`
- `market_context_high->crypto_major_1h` score `0.0875` n `134` status `ready` deltaP `7.7643` edge `0.0583` maxDD `-5.2213`
- `market_context_high->equity_4h` score `-0.0132` n `134` status `ready` deltaP `3.3059` edge `0.1347` maxDD `-6.008`
- `market_context_high->fx_1h` score `-0.0761` n `134` status `ready` deltaP `4.0285` edge `-0.0008` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.3272` n `134` status `ready` deltaP `1.6445` edge `0.0132` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.503` n `134` status `ready` deltaP `-0.3208` edge `-0.0025` maxDD `-0.4545`
- `news_risk_high->index_1h` score `-0.5177` n `58` status `ready` deltaP `1.5022` edge `-0.0053` maxDD `-0.6869`
- `market_context_high->index_1h` score `-0.8162` n `134` status `ready` deltaP `-1.9461` edge `0.0008` maxDD `-1.1344`
- `market_context_high->crypto_alt_1h` score `-0.8407` n `134` status `ready` deltaP `3.2979` edge `0.0567` maxDD `-8.251`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
