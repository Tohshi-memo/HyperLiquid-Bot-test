# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T19:31:07.431918+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14856`

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

- `news_risk_high->unknown_4h` score `13.4461` n `51` status `ready` deltaP `24.1063` edge `0.9644` maxDD `-0.0348`
- `risk_on_high->unknown_1h` score `4.0221` n `37` status `ready` deltaP `-8.6624` edge `0.6183` maxDD `-1.5916`
- `risk_on_and_context->unknown_1h` score `4.0221` n `37` status `ready` deltaP `-8.6624` edge `0.6183` maxDD `-1.5916`
- `news_risk_high->unknown_1h` score `3.2033` n `51` status `ready` deltaP `16.9337` edge `0.1845` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.0047` n `51` status `ready` deltaP `35.6438` edge `0.0262` maxDD `-0.0746`
- `risk_on_high->equity_4h` score `2.7656` n `36` status `ready` deltaP `2.0495` edge `0.2598` maxDD `-0.773`
- `risk_on_and_context->equity_4h` score `2.7656` n `36` status `ready` deltaP `2.0495` edge `0.2598` maxDD `-0.773`
- `news_risk_high->equity_4h` score `2.6154` n `51` status `ready` deltaP `22.9645` edge `0.1419` maxDD `-2.164`
- `risk_on_high->metal_4h` score `2.2417` n `36` status `ready` deltaP `29.895` edge `-0.0037` maxDD `-0.0367`
- `risk_on_and_context->metal_4h` score `2.2417` n `36` status `ready` deltaP `29.895` edge `-0.0037` maxDD `-0.0367`
- `news_risk_high->fx_1h` score `1.1883` n `51` status `ready` deltaP `16.3966` edge `0.0067` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `0.9944` n `143` status `ready` deltaP `6.6088` edge `0.0837` maxDD `-1.5916`
- `market_context_high->crypto_alt_4h` score `0.866` n `132` status `ready` deltaP `8.9847` edge `0.1587` maxDD `-7.0478`
- `news_risk_high->equity_1h` score `0.6911` n `51` status `ready` deltaP `15.9475` edge `0.0187` maxDD `-0.9128`
- `market_context_high->commodity_24h` score `0.6402` n `109` status `ready` deltaP `-1.631` edge `0.1117` maxDD `-0.7984`
- `risk_on_high->index_4h` score `0.5531` n `36` status `ready` deltaP `11.2635` edge `0.0438` maxDD `-0.1719`
- `risk_on_and_context->index_4h` score `0.5531` n `36` status `ready` deltaP `11.2635` edge `0.0438` maxDD `-0.1719`
- `news_risk_high->index_4h` score `0.4645` n `51` status `ready` deltaP `8.9759` edge `0.0186` maxDD `-0.1788`
- `risk_on_high->fx_4h` score `0.3296` n `36` status `ready` deltaP `11.2974` edge `0.003` maxDD `-0.2177`
- `risk_on_and_context->fx_4h` score `0.3296` n `36` status `ready` deltaP `11.2974` edge `0.003` maxDD `-0.2177`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
