# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-07T01:37:27.959326+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4148`

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

- `news_risk_high->equity_4h` score `1.0529` n `68` status `ready` deltaP `8.5724` edge `0.1559` maxDD `-4.2454`
- `news_risk_high->index_4h` score `0.7825` n `68` status `ready` deltaP `13.6926` edge `0.0217` maxDD `-0.4888`
- `news_risk_high->index_24h` score `0.3507` n `68` status `ready` deltaP `9.6712` edge `0.1473` maxDD `-6.6786`
- `news_risk_high->index_1h` score `0.0495` n `68` status `ready` deltaP `7.2561` edge `0.0033` maxDD `-0.2931`
- `news_risk_high->fx_4h` score `-0.1455` n `68` status `ready` deltaP `3.3806` edge `0.0034` maxDD `-0.2336`
- `news_risk_high->equity_1h` score `-0.1774` n `68` status `ready` deltaP `-1.9197` edge `0.045` maxDD `-1.396`
- `news_risk_high->fx_24h` score `-0.2044` n `68` status `ready` deltaP `-3.8807` edge `0.0531` maxDD `-0.2073`
- `news_risk_high->fx_1h` score `-0.285` n `68` status `ready` deltaP `0.0705` edge `0.0016` maxDD `-0.0888`
- `news_risk_high->metal_1h` score `-0.4775` n `68` status `ready` deltaP `-2.8179` edge `-0.0067` maxDD `-0.5256`
- `news_risk_high->metal_4h` score `-1.2085` n `68` status `ready` deltaP `-3.6137` edge `-0.0403` maxDD `-1.5773`
- `news_risk_high->crypto_major_4h` score `-1.59` n `68` status `ready` deltaP `-6.0796` edge `-0.0029` maxDD `-8.5004`
- `news_risk_high->commodity_1h` score `-2.1756` n `68` status `ready` deltaP `-14.7323` edge `-0.0045` maxDD `-1.2868`
- `news_risk_high->crypto_major_1h` score `-2.3082` n `68` status `ready` deltaP `-9.2198` edge `-0.037` maxDD `-4.1772`
- `news_risk_high->crypto_alt_1h` score `-2.4995` n `68` status `ready` deltaP `-5.8295` edge `-0.0519` maxDD `-5.4024`
- `news_risk_high->crypto_alt_4h` score `-2.7338` n `68` status `ready` deltaP `-7.2991` edge `-0.0398` maxDD `-13.9624`
- `news_risk_high->metal_24h` score `-3.5009` n `68` status `ready` deltaP `-2.3897` edge `-0.2433` maxDD `-8.5019`
- `news_risk_high->equity_24h` score `-3.6483` n `68` status `ready` deltaP `24.0604` edge `0.5305` maxDD `-86.0244`
- `news_risk_high->commodity_4h` score `-4.7039` n `68` status `ready` deltaP `-32.9089` edge `-0.0128` maxDD `-4.1171`
- `news_risk_high->commodity_24h` score `-10.4478` n `68` status `ready` deltaP `-30.5759` edge `-0.0989` maxDD `-28.0997`
- `news_risk_high->crypto_major_24h` score `-13.3909` n `68` status `ready` deltaP `-28.9624` edge `-0.0725` maxDD `-50.6925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
