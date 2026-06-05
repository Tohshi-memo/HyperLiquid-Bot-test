# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T14:22:28.127694+00:00`
- Price records: `672`
- Market context records: `2977`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6956`

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

- `market_context_high->crypto_alt_24h` score `15.8828` n `106` status `ready` deltaP `7.7306` edge `1.6637` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `10.6839` n `106` status `ready` deltaP `38.8823` edge `0.6492` maxDD `-0.7805`
- `market_context_high->unknown_24h` score `9.8925` n `106` status `ready` deltaP `15.9067` edge `0.7648` maxDD `-1.7175`
- `market_context_high->equity_24h` score `6.9318` n `106` status `ready` deltaP `16.1425` edge `0.6704` maxDD `-12.6963`
- `market_context_high->index_24h` score `4.0499` n `106` status `ready` deltaP `16.1196` edge `0.3281` maxDD `-2.5127`
- `market_context_high->equity_4h` score `2.9019` n `107` status `ready` deltaP `15.5801` edge `0.1769` maxDD `-0.7819`
- `market_context_high->index_4h` score `2.0951` n `107` status `ready` deltaP `20.4182` edge `0.1173` maxDD `-1.9733`
- `market_context_high->equity_1h` score `1.2704` n `107` status `ready` deltaP `8.761` edge `0.0808` maxDD `-1.0004`
- `market_context_high->commodity_4h` score `1.0062` n `107` status `ready` deltaP `13.0813` edge `0.1065` maxDD `-2.8438`
- `market_context_high->index_1h` score `0.8095` n `107` status `ready` deltaP `10.1852` edge `0.0387` maxDD `-0.7983`
- `market_context_high->crypto_alt_4h` score `0.6105` n `107` status `ready` deltaP `21.9156` edge `0.3883` maxDD `-30.8239`
- `market_context_high->crypto_alt_1h` score `0.1562` n `107` status `ready` deltaP `9.5137` edge `0.1201` maxDD `-10.747`
- `market_context_high->crypto_major_1h` score `-0.0251` n `107` status `ready` deltaP `9.7039` edge `0.0857` maxDD `-9.622`
- `market_context_high->commodity_1h` score `-0.2902` n `107` status `ready` deltaP `-0.5442` edge `0.0086` maxDD `-1.707`
- `market_context_high->fx_1h` score `-0.4097` n `107` status `ready` deltaP `-0.9933` edge `0.0032` maxDD `-0.1244`
- `market_context_high->unknown_4h` score `-0.8584` n `107` status `ready` deltaP `0.0299` edge `0.0336` maxDD `-3.7602`
- `market_context_high->unknown_1h` score `-1.0438` n `107` status `ready` deltaP `2.745` edge `-0.0322` maxDD `-3.1801`
- `market_context_high->metal_1h` score `-1.2574` n `107` status `ready` deltaP `-2.7814` edge `0.0025` maxDD `-3.4325`
- `market_context_high->fx_4h` score `-1.501` n `107` status `ready` deltaP `-7.1419` edge `0.0004` maxDD `-0.5631`
- `market_context_high->crypto_major_4h` score `-2.0185` n `107` status `ready` deltaP `8.3343` edge `0.1982` maxDD `-33.6701`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
