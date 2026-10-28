# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T15:52:35.917922+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8520`

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

- `market_context_high->unknown_24h` score `1415.1172` n `139` status `ready` deltaP `-3.2287` edge `118.0407` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `22.128` n `149` status `ready` deltaP `4.385` edge `1.83` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.5121` n `139` status `ready` deltaP `25.0949` edge `0.0275` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.1757` n `149` status `ready` deltaP `7.269` edge `0.002` maxDD `-0.1986`
- `market_context_high->fx_4h` score `-0.0093` n `149` status `ready` deltaP `7.9913` edge `0.0058` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.0808` n `149` status `ready` deltaP `8.4767` edge `0.0078` maxDD `-1.3073`
- `market_context_high->crypto_major_1h` score `-0.2759` n `149` status `ready` deltaP `7.5785` edge `0.0424` maxDD `-6.9306`
- `market_context_high->commodity_4h` score `-0.3786` n `149` status `ready` deltaP `7.3539` edge `0.0413` maxDD `-1.0837`
- `market_context_high->fx_24h` score `-0.4284` n `139` status `ready` deltaP `12.1653` edge `0.0212` maxDD `-1.2451`
- `market_context_high->commodity_1h` score `-0.7039` n `149` status `ready` deltaP `-0.9394` edge `0.006` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.7282` n `149` status `ready` deltaP `-3.3246` edge `-0.0029` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.7434` n `149` status `ready` deltaP `9.0563` edge `-0.0016` maxDD `-4.6603`
- `market_context_high->equity_1h` score `-1.3844` n `149` status `ready` deltaP `1.2388` edge `0.0055` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.5478` n `149` status `ready` deltaP `2.8955` edge `0.0186` maxDD `-12.2409`
- `market_context_high->equity_24h` score `-2.8077` n `139` status `ready` deltaP `6.6385` edge `0.0182` maxDD `-15.7143`
- `market_context_high->metal_24h` score `-2.82` n `139` status `ready` deltaP `2.6891` edge `0.03` maxDD `-8.6344`
- `market_context_high->index_4h` score `-2.9872` n `149` status `ready` deltaP `-8.7218` edge `-0.0286` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.177` n `139` status `ready` deltaP `1.4263` edge `0.0689` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.3678` n `149` status `ready` deltaP `4.119` edge `-0.0273` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.2937` n `149` status `ready` deltaP `-2.7152` edge `-0.1372` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
