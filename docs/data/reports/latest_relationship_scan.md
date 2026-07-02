# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T03:37:34.433874+00:00`
- Price records: `672`
- Market context records: `5416`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11492`

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

- `market_context_high->crypto_major_4h` score `4.0569` n `205` status `ready` deltaP `17.0732` edge `0.4535` maxDD `-14.0065`
- `market_context_high->crypto_major_24h` score `3.697` n `194` status `ready` deltaP `19.0668` edge `0.635` maxDD `-29.6555`
- `market_context_high->crypto_alt_4h` score `3.219` n `205` status `ready` deltaP `12.5305` edge `0.3488` maxDD `-9.46`
- `market_context_high->equity_4h` score `2.533` n `205` status `ready` deltaP `12.6525` edge `0.2906` maxDD `-7.4425`
- `market_context_high->equity_1h` score `0.4332` n `205` status `ready` deltaP `7.9093` edge `0.0799` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.1262` n `205` status `ready` deltaP `6.6241` edge `0.0157` maxDD `-0.9472`
- `market_context_high->crypto_major_1h` score `0.0406` n `205` status `ready` deltaP `4.3245` edge `0.0991` maxDD `-6.9639`
- `market_context_high->fx_24h` score `0.0223` n `194` status `ready` deltaP `9.0743` edge `0.0309` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `-0.0299` n `205` status `ready` deltaP `1.9293` edge `0.0808` maxDD `-5.0257`
- `market_context_high->fx_1h` score `-0.4392` n `205` status `ready` deltaP `-0.9537` edge `-0.001` maxDD `-0.5823`
- `market_context_high->equity_24h` score `-0.5132` n `194` status `ready` deltaP `8.0327` edge `0.4874` maxDD `-40.0306`
- `market_context_high->metal_1h` score `-0.5682` n `205` status `ready` deltaP `1.3305` edge `0.0113` maxDD `-2.0682`
- `market_context_high->index_4h` score `-0.9313` n `205` status `ready` deltaP `6.7073` edge `0.0386` maxDD `-2.874`
- `market_context_high->fx_4h` score `-1.2779` n `205` status `ready` deltaP `-0.6707` edge `0.0009` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.4423` n `205` status `ready` deltaP `-2.8713` edge `-0.0066` maxDD `-3.5563`
- `market_context_high->index_24h` score `-1.6619` n `194` status `ready` deltaP `12.8275` edge `0.0746` maxDD `-12.5551`
- `market_context_high->metal_4h` score `-2.5494` n `205` status `ready` deltaP `-6.5244` edge `-0.0309` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.1989` n `205` status `ready` deltaP `-6.3719` edge `-0.0436` maxDD `-14.1062`
- `market_context_high->crypto_alt_24h` score `-6.5465` n `194` status `ready` deltaP `10.3307` edge `0.2553` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.127` n `194` status `ready` deltaP `-4.9435` edge `-0.143` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
