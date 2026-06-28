# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T01:58:35.590060+00:00`
- Price records: `672`
- Market context records: `4995`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10472`

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

- `market_context_high->unknown_1h` score `22.0374` n `93` status `ready` deltaP `4.5667` edge `1.8561` maxDD `-1.674`
- `market_context_high->crypto_major_4h` score `6.204` n `87` status `ready` deltaP `18.0964` edge `0.5449` maxDD `-7.8836`
- `market_context_high->unknown_24h` score `6.1631` n `74` status `ready` deltaP `29.467` edge `0.3514` maxDD `-1.4072`
- `market_context_high->crypto_alt_4h` score `5.16` n `87` status `ready` deltaP `12.5841` edge `0.4855` maxDD `-7.8181`
- `market_context_high->unknown_4h` score `1.5653` n `87` status `ready` deltaP `20.8894` edge `0.0934` maxDD `-5.5109`
- `market_context_high->metal_4h` score `1.1109` n `87` status `ready` deltaP `11.0352` edge `0.1269` maxDD `-1.9651`
- `market_context_high->equity_1h` score `0.8465` n `93` status `ready` deltaP `7.8874` edge `0.0753` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.8273` n `93` status `ready` deltaP `6.2536` edge `0.119` maxDD `-4.6734`
- `market_context_high->equity_4h` score `0.6591` n `87` status `ready` deltaP `5.6175` edge `0.1852` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.4306` n `87` status `ready` deltaP `6.0625` edge `0.0437` maxDD `-0.8587`
- `market_context_high->metal_1h` score `0.3604` n `93` status `ready` deltaP `6.2536` edge `0.038` maxDD `-1.3057`
- `market_context_high->crypto_alt_1h` score `0.168` n `93` status `ready` deltaP `4.961` edge `0.0907` maxDD `-5.5126`
- `market_context_high->fx_24h` score `-0.2503` n `74` status `ready` deltaP `5.9122` edge `0.0047` maxDD `-1.7626`
- `market_context_high->commodity_1h` score `-0.3275` n `93` status `ready` deltaP `1.5582` edge `0.0136` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.5814` n `93` status `ready` deltaP `1.9123` edge `0.0129` maxDD `-0.5946`
- `market_context_high->fx_4h` score `-0.8176` n `87` status `ready` deltaP `-1.032` edge `-0.0009` maxDD `-1.0967`
- `market_context_high->commodity_4h` score `-1.316` n `87` status `ready` deltaP `3.4343` edge `-0.0073` maxDD `-5.021`
- `market_context_high->fx_1h` score `-1.7725` n `93` status `ready` deltaP `-12.1483` edge `-0.0057` maxDD `-0.5482`
- `market_context_high->commodity_24h` score `-4.0138` n `74` status `ready` deltaP `7.1837` edge `-0.0516` maxDD `-27.5371`
- `market_context_high->metal_24h` score `-4.2246` n `74` status `ready` deltaP `-0.6944` edge `0.0085` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
