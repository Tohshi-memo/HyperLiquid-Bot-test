# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T13:22:26.944209+00:00`
- Price records: `672`
- Market context records: `5458`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11444`

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

- `market_context_high->crypto_major_24h` score `3.8551` n `195` status `ready` deltaP `17.0673` edge `0.6615` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `2.47` n `198` status `ready` deltaP `14.7127` edge `0.337` maxDD `-14.0065`
- `market_context_high->equity_4h` score `2.0602` n `198` status `ready` deltaP `11.7978` edge `0.2569` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `1.8759` n `198` status `ready` deltaP `9.7961` edge `0.2551` maxDD `-9.46`
- `market_context_high->equity_1h` score `0.2352` n `199` status `ready` deltaP `7.564` edge `0.0657` maxDD `-5.0555`
- `market_context_high->equity_24h` score `0.1078` n `195` status `ready` deltaP `8.3066` edge `0.4615` maxDD `-31.6316`
- `market_context_high->index_1h` score `0.0791` n `199` status `ready` deltaP `6.1851` edge `0.0147` maxDD `-0.9472`
- `market_context_high->fx_24h` score `0.0296` n `195` status `ready` deltaP `9.6101` edge `0.0306` maxDD `-1.043`
- `market_context_high->metal_1h` score `-0.3265` n `199` status `ready` deltaP `3.662` edge `0.0159` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.5417` n `199` status `ready` deltaP `0.5612` edge `0.0` maxDD `-0.577`
- `market_context_high->crypto_alt_1h` score `-0.554` n `199` status `ready` deltaP `0.3581` edge `0.0476` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.6978` n `199` status `ready` deltaP `1.5451` edge `0.0561` maxDD `-6.9639`
- `market_context_high->index_4h` score `-0.9192` n `198` status `ready` deltaP `6.7843` edge `0.0391` maxDD `-2.874`
- `market_context_high->fx_4h` score `-1.0369` n `198` status `ready` deltaP `1.7261` edge `0.0046` maxDD `-1.5345`
- `market_context_high->commodity_1h` score `-1.3421` n `199` status `ready` deltaP `-1.8227` edge `-0.0049` maxDD `-3.5831`
- `market_context_high->index_24h` score `-1.9195` n `195` status `ready` deltaP `12.4759` edge `0.063` maxDD `-16.7147`
- `market_context_high->metal_4h` score `-2.5939` n `198` status `ready` deltaP `-7.8144` edge `-0.028` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.1788` n `198` status `ready` deltaP `-5.4432` edge `-0.0405` maxDD `-14.3822`
- `market_context_high->crypto_alt_24h` score `-6.955` n `195` status `ready` deltaP `8.3894` edge `0.2342` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.0005` n `195` status `ready` deltaP `-2.7804` edge `-0.1412` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
