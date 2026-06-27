# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T08:37:30.939740+00:00`
- Price records: `672`
- Market context records: `4916`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9384`

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

- `market_context_high->unknown_1h` score `15.8199` n `106` status `ready` deltaP `10.3181` edge `1.2913` maxDD `-1.674`
- `market_context_high->unknown_4h` score `10.4811` n `106` status `ready` deltaP `26.1965` edge `0.7502` maxDD `-1.7801`
- `market_context_high->crypto_alt_4h` score `6.7492` n `106` status `ready` deltaP `21.6693` edge `0.5532` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `6.5276` n `106` status `ready` deltaP `18.4767` edge `0.5432` maxDD `-7.1265`
- `market_context_high->unknown_24h` score `5.6216` n `88` status `ready` deltaP `24.5739` edge `0.3389` maxDD `-1.4072`
- `market_context_high->metal_4h` score `1.2785` n `106` status `ready` deltaP `9.5663` edge `0.109` maxDD `-1.9651`
- `market_context_high->equity_4h` score `0.9577` n `106` status `ready` deltaP `12.874` edge `0.1751` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.7444` n `106` status `ready` deltaP `10.1387` edge `0.0407` maxDD `-0.7006`
- `market_context_high->crypto_major_1h` score `0.5068` n `106` status `ready` deltaP `6.2281` edge `0.1273` maxDD `-5.6406`
- `market_context_high->equity_1h` score `0.3696` n `106` status `ready` deltaP `6.1095` edge `0.064` maxDD `-2.5875`
- `market_context_high->crypto_alt_1h` score `0.3469` n `106` status `ready` deltaP `6.858` edge `0.101` maxDD `-5.5126`
- `market_context_high->commodity_1h` score `-0.1329` n `106` status `ready` deltaP `4.8356` edge `0.0167` maxDD `-1.278`
- `market_context_high->metal_1h` score `-0.1754` n `106` status `ready` deltaP `1.6608` edge `0.0323` maxDD `-1.3057`
- `market_context_high->index_1h` score `-0.5224` n `106` status `ready` deltaP `-0.4039` edge `0.0112` maxDD `-0.7054`
- `market_context_high->commodity_4h` score `-0.6983` n `106` status `ready` deltaP `8.0217` edge `0.007` maxDD `-4.4933`
- `market_context_high->fx_4h` score `-0.8301` n `106` status `ready` deltaP `-1.8868` edge `0.0032` maxDD `-1.0967`
- `market_context_high->fx_1h` score `-0.8883` n `106` status `ready` deltaP `-7.8777` edge `-0.0001` maxDD `-0.5675`
- `market_context_high->fx_24h` score `-1.7721` n `88` status `ready` deltaP `-5.5872` edge `-0.0094` maxDD `-2.749`
- `market_context_high->commodity_24h` score `-4.7534` n `88` status `ready` deltaP `15.3094` edge `0.0127` maxDD `-27.5371`
- `market_context_high->index_24h` score `-4.808` n `88` status `ready` deltaP `-8.6332` edge `-0.1503` maxDD `-24.6845`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
