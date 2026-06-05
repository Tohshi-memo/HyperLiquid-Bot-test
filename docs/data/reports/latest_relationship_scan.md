# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T13:52:27.833102+00:00`
- Price records: `672`
- Market context records: `2975`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6954`

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

- `market_context_high->crypto_alt_24h` score `16.1538` n `108` status `ready` deltaP `8.4491` edge `1.6815` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `10.1933` n `108` status `ready` deltaP `37.1528` edge `0.6269` maxDD `-1.0113`
- `market_context_high->unknown_24h` score `9.7301` n `108` status `ready` deltaP `15.8565` edge `0.7516` maxDD `-1.7175`
- `market_context_high->equity_24h` score `7.0419` n `108` status `ready` deltaP `16.3194` edge `0.6784` maxDD `-12.6963`
- `market_context_high->index_24h` score `3.9724` n `108` status `ready` deltaP `16.2616` edge `0.3207` maxDD `-2.5127`
- `market_context_high->equity_4h` score `2.9377` n `109` status `ready` deltaP `15.7725` edge `0.1786` maxDD `-0.7819`
- `market_context_high->index_4h` score `1.9764` n `109` status `ready` deltaP `19.88` edge `0.111` maxDD `-1.9733`
- `market_context_high->equity_1h` score `1.2278` n `109` status `ready` deltaP `8.3627` edge `0.0799` maxDD `-1.0004`
- `market_context_high->crypto_alt_4h` score `0.8495` n `109` status `ready` deltaP `22.2967` edge `0.4164` maxDD `-30.8239`
- `market_context_high->commodity_4h` score `0.7553` n `109` status `ready` deltaP `11.7951` edge `0.0901` maxDD `-3.4185`
- `market_context_high->index_1h` score `0.6493` n `109` status `ready` deltaP `9.0535` edge `0.0329` maxDD `-0.7983`
- `market_context_high->crypto_alt_1h` score `0.2796` n `109` status `ready` deltaP `9.9517` edge `0.133` maxDD `-10.747`
- `market_context_high->crypto_major_1h` score `0.1041` n `109` status `ready` deltaP `10.1934` edge `0.099` maxDD `-9.622`
- `market_context_high->fx_1h` score `-0.3503` n `109` status `ready` deltaP `-0.401` edge `0.0042` maxDD `-0.1244`
- `market_context_high->unknown_4h` score `-0.4967` n `109` status `ready` deltaP `0.9216` edge `0.0578` maxDD `-3.7602`
- `market_context_high->commodity_1h` score `-0.5852` n `109` status `ready` deltaP `-1.4874` edge `-0.004` maxDD `-3.2219`
- `market_context_high->metal_1h` score `-0.7466` n `109` status `ready` deltaP `-2.0519` edge `0.0067` maxDD `-3.4325`
- `market_context_high->unknown_1h` score `-0.8855` n `109` status `ready` deltaP `3.2687` edge `-0.0225` maxDD `-3.1801`
- `market_context_high->fx_4h` score `-1.4323` n `109` status `ready` deltaP `-6.4179` edge `0.0013` maxDD `-0.5631`
- `market_context_high->crypto_major_4h` score `-1.7676` n `109` status `ready` deltaP `8.9898` edge `0.226` maxDD `-33.6701`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
