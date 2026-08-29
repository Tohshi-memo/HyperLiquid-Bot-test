# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T18:52:26.636266+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11330`

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

- `news_risk_high->unknown_24h` score `30.5984` n `61` status `ready` deltaP `4.0556` edge `2.6202` maxDD `-4.1232`
- `news_risk_high->crypto_alt_24h` score `16.702` n `61` status `ready` deltaP `30.0006` edge `1.5294` maxDD `-22.3391`
- `risk_on_high->crypto_alt_4h` score `12.7687` n `32` status `ready` deltaP `47.1799` edge `0.7554` maxDD `-0.1367`
- `risk_on_and_context->crypto_alt_4h` score `12.7687` n `32` status `ready` deltaP `47.1799` edge `0.7554` maxDD `-0.1367`
- `market_context_high->unknown_24h` score `11.1475` n `104` status `ready` deltaP `20.9535` edge `0.8625` maxDD `-3.1917`
- `risk_on_high->crypto_major_4h` score `8.2409` n `32` status `ready` deltaP `38.7957` edge `0.4557` maxDD `-1.208`
- `risk_on_and_context->crypto_major_4h` score `8.2409` n `32` status `ready` deltaP `38.7957` edge `0.4557` maxDD `-1.208`
- `news_risk_high->unknown_4h` score `5.7304` n `70` status `ready` deltaP `8.1664` edge `0.4821` maxDD `-1.7205`
- `market_context_high->metal_24h` score `4.6982` n `104` status `ready` deltaP `34.415` edge `0.264` maxDD `-3.1535`
- `risk_on_high->metal_4h` score `2.9709` n `32` status `ready` deltaP `32.5457` edge `0.0392` maxDD `-0.0208`
- `risk_on_and_context->metal_4h` score `2.9709` n `32` status `ready` deltaP `32.5457` edge `0.0392` maxDD `-0.0208`
- `news_risk_high->unknown_1h` score `2.5988` n `70` status `ready` deltaP `1.7793` edge `0.2404` maxDD `-0.8558`
- `market_context_high->unknown_4h` score `2.4092` n `132` status `ready` deltaP `19.3136` edge `0.1152` maxDD `-0.7887`
- `risk_on_high->unknown_4h` score `2.0887` n `32` status `ready` deltaP `33.6128` edge `-0.0417` maxDD `-0.3325`
- `risk_on_and_context->unknown_4h` score `2.0887` n `32` status `ready` deltaP `33.6128` edge `-0.0417` maxDD `-0.3325`
- `news_risk_high->fx_4h` score `1.5316` n `70` status `ready` deltaP `34.4991` edge `0.0213` maxDD `-0.3953`
- `risk_on_high->metal_1h` score `1.3666` n `42` status `ready` deltaP `18.8837` edge `0.0094` maxDD `-0.0463`
- `risk_on_and_context->metal_1h` score `1.3666` n `42` status `ready` deltaP `18.8837` edge `0.0094` maxDD `-0.0463`
- `market_context_high->crypto_major_4h` score `0.8807` n `132` status `ready` deltaP `21.6555` edge `0.2741` maxDD `-20.9394`
- `risk_on_high->equity_4h` score `0.7283` n `32` status `ready` deltaP `4.9543` edge `0.0526` maxDD `-0.3281`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
