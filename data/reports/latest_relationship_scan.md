# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T19:07:19.894188+00:00`
- Price records: `672`
- Market context records: `3208`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `10908`

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

- `market_context_high->commodity_24h` score `13.7231` n `97` status `ready` deltaP `47.4924` edge `0.8698` maxDD `-2.0927`
- `market_context_high->crypto_alt_24h` score `11.1383` n `97` status `ready` deltaP `11.9398` edge `2.346` maxDD `-71.142`
- `market_context_high->index_24h` score `9.2417` n `97` status `ready` deltaP `28.0784` edge `0.8384` maxDD `-16.1026`
- `market_context_high->equity_24h` score `7.283` n `97` status `ready` deltaP `11.8109` edge `1.3698` maxDD `-53.663`
- `market_context_high->commodity_4h` score `3.3655` n `124` status `ready` deltaP `22.1037` edge `0.1789` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `0.4675` n `135` status `ready` deltaP `6.5879` edge `0.0373` maxDD `-1.7142`
- `market_context_high->unknown_4h` score `0.4252` n `124` status `ready` deltaP `10.7936` edge `0.1857` maxDD `-14.7778`
- `market_context_high->fx_24h` score `0.4224` n `97` status `ready` deltaP `10.4042` edge `-0.0037` maxDD `-0.7702`
- `market_context_high->crypto_major_1h` score `-0.9043` n `135` status `ready` deltaP `5.0188` edge `0.0769` maxDD `-15.1032`
- `market_context_high->index_1h` score `-0.9216` n `135` status `ready` deltaP `3.0572` edge `0.0091` maxDD `-4.5023`
- `market_context_high->crypto_alt_1h` score `-0.9595` n `135` status `ready` deltaP `4.98` edge `0.0998` maxDD `-14.7034`
- `market_context_high->fx_4h` score `-1.1135` n `124` status `ready` deltaP `-7.3466` edge `-0.0053` maxDD `-1.4115`
- `market_context_high->equity_1h` score `-1.5178` n `135` status `ready` deltaP `2.3087` edge `0.0067` maxDD `-8.8863`
- `market_context_high->index_4h` score `-1.5478` n `124` status `ready` deltaP `15.0177` edge `0.0618` maxDD `-17.6057`
- `market_context_high->fx_1h` score `-1.7182` n `135` status `ready` deltaP `-10.4258` edge `-0.005` maxDD `-0.8278`
- `market_context_high->unknown_24h` score `-1.7655` n `97` status `ready` deltaP `12.3765` edge `0.2432` maxDD `-41.1643`
- `market_context_high->metal_1h` score `-2.0411` n `135` status `ready` deltaP `-3.1836` edge `-0.0095` maxDD `-7.4828`
- `market_context_high->unknown_1h` score `-2.6785` n `135` status `ready` deltaP `1.8053` edge `-0.1176` maxDD `-17.0266`
- `market_context_high->crypto_alt_4h` score `-3.3636` n `124` status `ready` deltaP `12.9819` edge `0.2867` maxDD `-58.6918`
- `market_context_high->crypto_major_4h` score `-4.5711` n `124` status `ready` deltaP `5.9599` edge `0.1666` maxDD `-54.3896`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
