# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T14:37:30.491155+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9280`

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

- `market_context_high->equity_24h` score `6.961` n `34` status `ready` deltaP `11.7852` edge `0.7388` maxDD `-16.6495`
- `market_context_high->commodity_24h` score `1.962` n `34` status `ready` deltaP `4.1463` edge `0.1946` maxDD `-1.6995`
- `market_context_high->index_24h` score `0.9591` n `34` status `ready` deltaP `10.7128` edge `0.0978` maxDD `-2.3671`
- `market_context_high->fx_24h` score `0.6198` n `34` status `ready` deltaP `9.9877` edge `-0.0043` maxDD `-0.1843`
- `market_context_high->metal_1h` score `-0.3461` n `88` status `ready` deltaP `3.797` edge `0.0135` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.4945` n `88` status `ready` deltaP `0.4423` edge `0.0019` maxDD `-1.7935`
- `market_context_high->index_4h` score `-0.5122` n `88` status `ready` deltaP `3.8525` edge `0.0064` maxDD `-2.4871`
- `market_context_high->commodity_4h` score `-0.7753` n `88` status `ready` deltaP `-1.4689` edge `0.021` maxDD `-4.182`
- `market_context_high->metal_4h` score `-0.9213` n `88` status `ready` deltaP `0.4712` edge `0.0171` maxDD `-4.0688`
- `market_context_high->index_1h` score `-0.9309` n `88` status `ready` deltaP `-6.6072` edge `0.0078` maxDD `-0.9814`
- `market_context_high->fx_1h` score `-1.2953` n `88` status `ready` deltaP `-13.7588` edge `-0.0059` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.3811` n `88` status `ready` deltaP `-6.9066` edge `0.0526` maxDD `-8.0225`
- `market_context_high->crypto_alt_1h` score `-1.8493` n `88` status `ready` deltaP `1.2316` edge `-0.0474` maxDD `-10.8319`
- `market_context_high->metal_24h` score `-2.0104` n `34` status `ready` deltaP `-3.125` edge `-0.1816` maxDD `-1.4245`
- `market_context_high->fx_4h` score `-2.1178` n `88` status `ready` deltaP `-6.7628` edge `-0.0083` maxDD `-2.4506`
- `market_context_high->crypto_major_1h` score `-3.0864` n `88` status `ready` deltaP `-4.5114` edge `-0.1033` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-5.2516` n `88` status `ready` deltaP `0.4573` edge `-0.0627` maxDD `-24.9053`
- `market_context_high->crypto_major_24h` score `-6.4437` n `34` status `ready` deltaP `-6.5257` edge `-0.0304` maxDD `-30.3789`
- `market_context_high->crypto_alt_4h` score `-8.5584` n `88` status `ready` deltaP `2.7023` edge `-0.2194` maxDD `-34.2787`
- `market_context_high->crypto_alt_24h` score `-10.7381` n `34` status `ready` deltaP `-20.7312` edge `-0.2472` maxDD `-33.4213`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
