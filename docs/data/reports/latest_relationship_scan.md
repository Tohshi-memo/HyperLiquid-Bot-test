# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T17:07:26.626067+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7457`

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

- `market_context_high->unknown_24h` score `2706.8985` n `103` status `ready` deltaP `-8.6924` edge `225.6758` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `77.1054` n `108` status `ready` deltaP `-6.2431` edge `6.4957` maxDD `-0.9571`
- `market_context_high->unknown_4h` score `75.1122` n `103` status `ready` deltaP `1.1307` edge `6.2651` maxDD `-0.3966`
- `news_risk_high->crypto_alt_24h` score `18.4518` n `62` status `ready` deltaP `45.3853` edge `1.2402` maxDD `-0.0763`
- `market_context_high->equity_24h` score `11.1889` n `103` status `ready` deltaP `26.9435` edge `1.0285` maxDD `-14.0571`
- `market_context_high->index_24h` score `4.9067` n `103` status `ready` deltaP `43.9051` edge `0.1345` maxDD `-0.1315`
- `news_risk_high->crypto_alt_4h` score `4.8467` n `102` status `ready` deltaP `17.5843` edge `0.4253` maxDD `-7.4246`
- `market_context_high->metal_4h` score `1.7644` n `103` status `ready` deltaP `21.8283` edge `0.044` maxDD `-0.7323`
- `market_context_high->equity_4h` score `1.2828` n `103` status `ready` deltaP `7.4902` edge `0.1963` maxDD `-4.48`
- `market_context_high->metal_1h` score `0.8914` n `103` status `ready` deltaP `12.7347` edge `0.0184` maxDD `-0.3209`
- `market_context_high->crypto_major_1h` score `0.6633` n `103` status `ready` deltaP `10.2668` edge `0.0896` maxDD `-5.2213`
- `news_risk_high->crypto_alt_1h` score `0.6047` n `108` status `ready` deltaP `7.5294` edge `0.0956` maxDD `-3.9659`
- `market_context_high->equity_1h` score `0.4546` n `103` status `ready` deltaP `7.1319` edge `0.0983` maxDD `-2.3383`
- `market_context_high->fx_1h` score `0.2356` n `103` status `ready` deltaP `8.6201` edge `-0.0005` maxDD `-0.1407`
- `market_context_high->fx_4h` score `0.2214` n `103` status `ready` deltaP `8.5735` edge `0.0004` maxDD `-0.1285`
- `market_context_high->metal_24h` score `0.1598` n `103` status `ready` deltaP `14.6828` edge `0.1873` maxDD `-10.5088`
- `market_context_high->crypto_major_4h` score `0.1006` n `103` status `ready` deltaP `17.5201` edge `0.1656` maxDD `-14.5879`
- `market_context_high->commodity_4h` score `0.0639` n `103` status `ready` deltaP `11.1325` edge `0.0553` maxDD `-1.0393`
- `market_context_high->index_1h` score `-0.3471` n `103` status `ready` deltaP `3.6931` edge `0.0023` maxDD `-1.1344`
- `market_context_high->commodity_1h` score `-0.4681` n `103` status `ready` deltaP `-0.327` edge `0.0146` maxDD `-0.4475`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
