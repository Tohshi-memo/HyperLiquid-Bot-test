# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-17T08:37:31.792063+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9372`

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

- `market_context_high->crypto_alt_4h` score `7.3694` n `134` status `ready` deltaP `17.5896` edge `0.5883` maxDD `-4.9825`
- `risk_on_high->commodity_24h` score `7.0461` n `54` status `ready` deltaP `38.5017` edge `0.3305` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.0461` n `54` status `ready` deltaP `38.5017` edge `0.3305` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `6.5315` n `60` status `ready` deltaP `36.5345` edge `0.386` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `6.5315` n `60` status `ready` deltaP `36.5345` edge `0.386` maxDD `-4.1548`
- `market_context_high->crypto_major_4h` score `6.1642` n `134` status `ready` deltaP `24.0967` edge `0.4852` maxDD `-5.906`
- `risk_on_high->crypto_alt_4h` score `4.663` n `60` status `ready` deltaP `15.5996` edge `0.3363` maxDD `-2.1371`
- `risk_on_and_context->crypto_alt_4h` score `4.663` n `60` status `ready` deltaP `15.5996` edge `0.3363` maxDD `-2.1371`
- `market_context_high->crypto_alt_1h` score `1.1982` n `146` status `ready` deltaP `10.5734` edge `0.1358` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `1.1259` n `146` status `ready` deltaP `8.6683` edge `0.1166` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.3483` n `134` status `ready` deltaP `12.4135` edge `0.0508` maxDD `-1.6961`
- `risk_on_high->index_1h` score `0.0555` n `72` status `ready` deltaP `5.7057` edge `0.005` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.0555` n `72` status `ready` deltaP `5.7057` edge `0.005` maxDD `-0.7394`
- `risk_on_high->crypto_major_1h` score `-0.0167` n `72` status `ready` deltaP `7.3935` edge `0.0208` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.0167` n `72` status `ready` deltaP `7.3935` edge `0.0208` maxDD `-3.7781`
- `market_context_high->index_1h` score `-0.183` n `146` status `ready` deltaP `7.0756` edge `0.0042` maxDD `-1.3195`
- `market_context_high->metal_1h` score `-0.3003` n `146` status `ready` deltaP `7.9382` edge `0.009` maxDD `-0.9556`
- `market_context_high->equity_1h` score `-0.5095` n `146` status `ready` deltaP `7.6577` edge `0.0346` maxDD `-7.0778`
- `risk_on_high->metal_1h` score `-0.5211` n `72` status `ready` deltaP `0.3659` edge `0.0039` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.5211` n `72` status `ready` deltaP `0.3659` edge `0.0039` maxDD `-0.8513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
