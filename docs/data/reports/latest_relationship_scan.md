# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T12:07:34.559782+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8856`

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

- `market_context_high->unknown_4h` score `81.8805` n `135` status `ready` deltaP `5.4619` edge `6.8022` maxDD `-0.5521`
- `market_context_high->unknown_1h` score `14.964` n `135` status `ready` deltaP `1.069` edge `1.2888` maxDD `-1.5807`
- `market_context_high->index_24h` score `1.9421` n `132` status `ready` deltaP `26.7055` edge `0.0526` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.5098` n `135` status `ready` deltaP `11.2054` edge `0.0036` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.4493` n `135` status `ready` deltaP `13.0488` edge `0.0103` maxDD `-0.4545`
- `market_context_high->metal_1h` score `0.0553` n `135` status `ready` deltaP `10.6454` edge `0.0108` maxDD `-1.3073`
- `market_context_high->commodity_1h` score `-0.3141` n `135` status `ready` deltaP `1.9783` edge `0.0107` maxDD `-1.0053`
- `market_context_high->crypto_major_1h` score `-0.4482` n `135` status `ready` deltaP `6.1854` edge `0.0296` maxDD `-6.9306`
- `market_context_high->index_1h` score `-0.5601` n `135` status `ready` deltaP `-0.2129` edge `-0.0021` maxDD `-1.4631`
- `market_context_high->fx_24h` score `-0.703` n `132` status `ready` deltaP `7.3657` edge `0.018` maxDD `-1.2451`
- `market_context_high->metal_4h` score `-0.7141` n `135` status `ready` deltaP `9.0808` edge `0.002` maxDD `-4.6603`
- `market_context_high->commodity_4h` score `-0.7381` n `135` status `ready` deltaP `3.6405` edge `0.0361` maxDD `-1.0837`
- `market_context_high->metal_24h` score `-1.2153` n `132` status `ready` deltaP `13.6547` edge `0.0855` maxDD `-8.2244`
- `market_context_high->equity_1h` score `-1.3786` n `135` status `ready` deltaP `2.3397` edge `-0.0011` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.9444` n `135` status `ready` deltaP `-1.0413` edge `-0.006` maxDD `-12.2409`
- `market_context_high->equity_24h` score `-2.4782` n `132` status `ready` deltaP `7.2015` edge `0.0419` maxDD `-15.7143`
- `market_context_high->index_4h` score `-2.553` n `135` status `ready` deltaP `-3.8788` edge `-0.0247` maxDD `-5.6417`
- `market_context_high->crypto_major_4h` score `-3.5186` n `135` status `ready` deltaP `4.8792` edge `-0.0517` maxDD `-27.2215`
- `market_context_high->crypto_major_24h` score `-4.4463` n `132` status `ready` deltaP `-0.8443` edge `-0.0787` maxDD `-29.1905`
- `market_context_high->equity_4h` score `-4.8582` n `135` status `ready` deltaP `3.0048` edge `-0.1195` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
