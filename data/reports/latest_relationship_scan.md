# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-06T22:37:15.868366+00:00`
- Price records: `494`
- Market context records: `587`
- Flow alert records: `1660`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `807`

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

- `market_context_high->crypto_alt_24h` score `4.6579` n `146` status `ready` deltaP `7.104` edge `0.3456` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `3.2651` n `146` status `ready` deltaP `10.1225` edge `0.238` maxDD `-1.3382`
- `market_context_high->fx_4h` score `0.0941` n `146` status `ready` deltaP `11.8057` edge `0.0205` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.2843` n `146` status `ready` deltaP `2.5283` edge `0.0045` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.6019` n `146` status `ready` deltaP `1.6489` edge `0.0363` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6404` n `146` status `ready` deltaP `0.8766` edge `-0.0026` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.2066` n `146` status `ready` deltaP `-4.5625` edge `-0.0098` maxDD `-2.1602`
- `market_context_high->equity_1h` score `-1.209` n `146` status `ready` deltaP `-1.5925` edge `-0.0091` maxDD `-4.4826`
- `market_context_high->crypto_alt_1h` score `-1.28` n `146` status `ready` deltaP `4.9958` edge `-0.0085` maxDD `-8.1842`
- `market_context_high->crypto_major_1h` score `-1.893` n `146` status `ready` deltaP `4.2829` edge `-0.014` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-2.1705` n `146` status `ready` deltaP `2.8801` edge `0.0569` maxDD `-15.2248`
- `market_context_high->index_24h` score `-2.2189` n `146` status `ready` deltaP `-6.2548` edge `0.0563` maxDD `-5.9609`
- `market_context_high->index_4h` score `-2.2677` n `146` status `ready` deltaP `0.0896` edge `-0.0373` maxDD `-6.5149`
- `market_context_high->crypto_major_4h` score `-2.9367` n `146` status `ready` deltaP `11.6668` edge `0.0481` maxDD `-22.648`
- `market_context_high->metal_1h` score `-3.2981` n `146` status `ready` deltaP `-4.6072` edge `-0.0482` maxDD `-9.0076`
- `market_context_high->equity_4h` score `-3.3567` n `146` status `ready` deltaP `-3.7079` edge `-0.0398` maxDD `-10.5498`
- `market_context_high->commodity_4h` score `-3.6784` n `146` status `ready` deltaP `-6.4707` edge `0.0867` maxDD `-13.0076`
- `market_context_high->equity_24h` score `-4.2385` n `146` status `ready` deltaP `-10.1905` edge `-0.0248` maxDD `-10.5047`
- `market_context_high->fx_24h` score `-4.452` n `146` status `ready` deltaP `-4.2278` edge `-0.0254` maxDD `-21.0414`
- `market_context_high->unknown_4h` score `-5.0925` n `146` status `ready` deltaP `0.9371` edge `-0.2428` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
