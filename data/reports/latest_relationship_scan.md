# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T19:07:29.501166+00:00`
- Price records: `672`
- Market context records: `4962`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9536`

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

- `market_context_high->unknown_1h` score `18.6693` n `97` status `ready` deltaP `8.2798` edge `1.5465` maxDD `-1.674`
- `market_context_high->unknown_4h` score `12.1189` n `94` status `ready` deltaP `28.7137` edge `0.8699` maxDD `-1.7801`
- `market_context_high->crypto_major_4h` score `7.3203` n `94` status `ready` deltaP `21.7404` edge `0.5875` maxDD `-7.1265`
- `market_context_high->crypto_alt_4h` score `7.0478` n `94` status `ready` deltaP `22.1912` edge `0.5746` maxDD `-7.8181`
- `market_context_high->unknown_24h` score `5.7612` n `91` status `ready` deltaP `26.7991` edge `0.3357` maxDD `-1.4072`
- `market_context_high->equity_4h` score `1.7215` n `94` status `ready` deltaP `14.1314` edge `0.1874` maxDD `-6.3852`
- `market_context_high->metal_4h` score `1.5375` n `94` status `ready` deltaP `12.3281` edge `0.1205` maxDD `-1.9651`
- `market_context_high->crypto_major_1h` score `1.3612` n `97` status `ready` deltaP `8.6811` edge `0.1594` maxDD `-5.6406`
- `market_context_high->equity_1h` score `1.0923` n `97` status `ready` deltaP `10.3756` edge `0.0792` maxDD `-2.5875`
- `market_context_high->index_4h` score `0.9374` n `94` status `ready` deltaP `12.0135` edge `0.0442` maxDD `-0.6938`
- `market_context_high->crypto_alt_1h` score `0.7258` n `97` status `ready` deltaP `10.0932` edge `0.128` maxDD `-5.5126`
- `market_context_high->metal_1h` score `0.2168` n `97` status `ready` deltaP `5.8877` edge `0.0368` maxDD `-1.3057`
- `market_context_high->index_1h` score `-0.3465` n `97` status `ready` deltaP `2.71` edge `0.013` maxDD `-0.7054`
- `market_context_high->commodity_1h` score `-0.4196` n `97` status `ready` deltaP `0.7161` edge `0.0074` maxDD `-1.278`
- `market_context_high->commodity_4h` score `-1.0245` n `94` status `ready` deltaP `6.7138` edge `-0.0056` maxDD `-4.9624`
- `market_context_high->fx_4h` score `-1.116` n `94` status `ready` deltaP `-6.2306` edge `-0.0045` maxDD `-1.0967`
- `market_context_high->fx_1h` score `-1.4932` n `97` status `ready` deltaP `-8.9944` edge `-0.0045` maxDD `-0.4646`
- `market_context_high->fx_24h` score `-1.5245` n `91` status `ready` deltaP `-1.9974` edge `-0.0127` maxDD `-2.749`
- `market_context_high->commodity_24h` score `-3.9995` n `91` status `ready` deltaP `19.6485` edge `0.0466` maxDD `-27.5371`
- `market_context_high->metal_24h` score `-6.9632` n `91` status `ready` deltaP `-9.6879` edge `0.0298` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
