# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T15:37:31.053923+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7375`

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

- `market_context_high->unknown_24h` score `2567.6386` n `106` status `ready` deltaP `-8.2252` edge `214.0677` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `77.1906` n `108` status `ready` deltaP `-6.2431` edge `6.5028` maxDD `-0.9571`
- `market_context_high->unknown_4h` score `63.0158` n `106` status `ready` deltaP `1.1706` edge `5.2568` maxDD `-0.3966`
- `news_risk_high->crypto_alt_24h` score `17.6513` n `56` status `ready` deltaP `45.0397` edge `1.1758` maxDD `-0.0763`
- `market_context_high->equity_24h` score `11.2979` n `106` status `ready` deltaP `27.6304` edge `1.033` maxDD `-14.0571`
- `market_context_high->index_24h` score `4.8607` n `106` status `ready` deltaP `43.5403` edge `0.1331` maxDD `-0.1315`
- `news_risk_high->crypto_alt_4h` score `4.4938` n `98` status `ready` deltaP `16.5039` edge `0.4031` maxDD `-7.4246`
- `market_context_high->metal_4h` score `1.8468` n `106` status `ready` deltaP `22.7076` edge `0.045` maxDD `-0.7323`
- `market_context_high->equity_4h` score `1.4541` n `106` status `ready` deltaP `8.6718` edge `0.2027` maxDD `-4.48`
- `market_context_high->metal_1h` score `0.9927` n `106` status `ready` deltaP `13.956` edge `0.0187` maxDD `-0.3209`
- `market_context_high->crypto_major_1h` score `0.8101` n `106` status `ready` deltaP `11.0666` edge `0.0965` maxDD `-5.2213`
- `market_context_high->equity_1h` score `0.7087` n `106` status `ready` deltaP `7.0981` edge `0.0993` maxDD `-2.3383`
- `news_risk_high->crypto_alt_1h` score `0.5986` n `108` status `ready` deltaP `7.6791` edge `0.0941` maxDD `-3.9659`
- `market_context_high->crypto_major_4h` score `0.3942` n `106` status `ready` deltaP `18.0396` edge `0.1866` maxDD `-14.5879`
- `market_context_high->metal_24h` score `0.2302` n `106` status `ready` deltaP `15.4809` edge `0.191` maxDD `-10.5088`
- `market_context_high->fx_1h` score `0.1526` n `106` status `ready` deltaP `7.0388` edge `-0.0006` maxDD `-0.1407`
- `market_context_high->fx_4h` score `0.0793` n `106` status `ready` deltaP `6.8425` edge `0.0001` maxDD `-0.1285`
- `market_context_high->commodity_4h` score `0.0021` n `106` status `ready` deltaP `10.3572` edge `0.0531` maxDD `-1.0837`
- `market_context_high->index_1h` score `-0.2879` n `106` status `ready` deltaP `4.3583` edge `0.0028` maxDD `-1.1344`
- `market_context_high->commodity_1h` score `-0.4983` n `106` status `ready` deltaP `-0.6751` edge `0.0144` maxDD `-0.4475`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
