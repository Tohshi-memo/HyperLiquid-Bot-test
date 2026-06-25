# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T20:52:30.307058+00:00`
- Price records: `672`
- Market context records: `4759`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7476`

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

- `market_context_high->unknown_1h` score `7.0857` n `134` status `ready` deltaP `12.5302` edge `0.5487` maxDD `-1.674`
- `market_context_high->unknown_4h` score `6.4707` n `131` status `ready` deltaP `14.8901` edge `0.561` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `2.9604` n `119` status `ready` deltaP `14.63` edge `0.2415` maxDD `-4.7201`
- `market_context_high->index_4h` score `-0.3964` n `131` status `ready` deltaP `7.4043` edge `0.0067` maxDD `-5.5505`
- `market_context_high->equity_4h` score `-0.4338` n `131` status `ready` deltaP `7.4066` edge `0.0636` maxDD `-8.8203`
- `market_context_high->commodity_1h` score `-0.4944` n `134` status `ready` deltaP `1.955` edge `0.0212` maxDD `-2.0345`
- `market_context_high->commodity_4h` score `-0.5678` n `131` status `ready` deltaP `8.6122` edge `0.0282` maxDD `-7.6725`
- `market_context_high->fx_4h` score `-0.6539` n `131` status `ready` deltaP `-0.2304` edge `-0.0005` maxDD `-1.5439`
- `market_context_high->equity_1h` score `-0.8805` n `134` status `ready` deltaP `-1.0479` edge `-0.0171` maxDD `-5.1038`
- `market_context_high->fx_1h` score `-1.1026` n `134` status `ready` deltaP `-3.4252` edge `-0.0041` maxDD `-0.8626`
- `market_context_high->index_1h` score `-1.5954` n `134` status `ready` deltaP `-3.5906` edge `-0.0086` maxDD `-2.6999`
- `market_context_high->metal_1h` score `-2.465` n `134` status `ready` deltaP `-2.6745` edge `-0.0693` maxDD `-14.9779`
- `market_context_high->commodity_24h` score `-2.4719` n `119` status `ready` deltaP `17.7258` edge `0.0758` maxDD `-27.5371`
- `market_context_high->crypto_alt_1h` score `-2.9109` n `134` status `ready` deltaP `-1.4903` edge `-0.0654` maxDD `-19.8288`
- `market_context_high->crypto_major_1h` score `-3.3597` n `134` status `ready` deltaP `-0.8893` edge `-0.0817` maxDD `-24.7815`
- `market_context_high->fx_24h` score `-4.0362` n `119` status `ready` deltaP `-15.2618` edge `-0.0207` maxDD `-4.1125`
- `market_context_high->crypto_alt_4h` score `-5.3768` n `131` status `ready` deltaP `2.517` edge `-0.039` maxDD `-48.0361`
- `market_context_high->index_24h` score `-6.7887` n `119` status `ready` deltaP `-10.6633` edge `-0.114` maxDD `-22.1174`
- `market_context_high->crypto_major_4h` score `-8.1474` n `131` status `ready` deltaP `3.2791` edge `-0.1433` maxDD `-68.5143`
- `market_context_high->metal_4h` score `-8.297` n `131` status `ready` deltaP `5.2597` edge `-0.2747` maxDD `-61.2596`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
