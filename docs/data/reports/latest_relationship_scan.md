# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T12:07:46.851266+00:00`
- Price records: `672`
- Market context records: `5453`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11440`

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

- `market_context_high->crypto_major_24h` score `3.4733` n `190` status `ready` deltaP `17.2606` edge `0.6284` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `2.8348` n `197` status `ready` deltaP `15.2826` edge `0.3636` maxDD `-14.0065`
- `market_context_high->equity_4h` score `2.3879` n `197` status `ready` deltaP `12.3831` edge `0.2803` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `2.1631` n `197` status `ready` deltaP `10.3558` edge `0.2753` maxDD `-9.46`
- `market_context_high->equity_24h` score `1.302` n `190` status `ready` deltaP `9.693` edge `0.5264` maxDD `-30.2682`
- `market_context_high->equity_1h` score `0.5015` n `199` status `ready` deltaP `8.1628` edge `0.0839` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.1788` n `190` status `ready` deltaP `10.6853` edge `0.0332` maxDD `-0.8294`
- `market_context_high->index_1h` score `0.1558` n `199` status `ready` deltaP `6.7839` edge `0.0171` maxDD `-0.9472`
- `market_context_high->metal_1h` score `-0.2557` n `199` status `ready` deltaP `3.9614` edge `0.0198` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.3297` n `199` status `ready` deltaP `0.9569` edge `0.0623` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.4435` n `199` status `ready` deltaP `2.1439` edge `0.0733` maxDD `-6.9639`
- `market_context_high->fx_1h` score `-0.5656` n `199` status `ready` deltaP `0.2618` edge `0.0` maxDD `-0.577`
- `market_context_high->index_4h` score `-0.8468` n `197` status `ready` deltaP `7.3132` edge `0.0416` maxDD `-2.874`
- `market_context_high->fx_4h` score `-1.0865` n `197` status `ready` deltaP `1.211` edge `0.0039` maxDD `-1.5345`
- `market_context_high->commodity_1h` score `-1.3672` n `199` status `ready` deltaP `-2.1221` edge `-0.005` maxDD `-3.5831`
- `market_context_high->index_24h` score `-1.4061` n `190` status `ready` deltaP `14.2708` edge `0.0775` maxDD `-15.2324`
- `market_context_high->metal_4h` score `-2.6057` n `197` status `ready` deltaP `-7.9671` edge `-0.0285` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.2938` n `197` status `ready` deltaP `-6.3861` edge `-0.0438` maxDD `-14.3822`
- `market_context_high->metal_24h` score `-7.2572` n `190` status `ready` deltaP `-4.2379` edge `-0.1644` maxDD `-33.021`
- `market_context_high->crypto_alt_24h` score `-7.2765` n `190` status `ready` deltaP `8.2859` edge `0.2081` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
