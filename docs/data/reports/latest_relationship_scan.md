# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T03:09:07.011382+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11837`

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

- `market_context_high->crypto_major_24h` score `4.4642` n `73` status `ready` deltaP `15.6905` edge `0.3882` maxDD `-4.9964`
- `market_context_high->metal_24h` score `0.6214` n `73` status `ready` deltaP `4.8384` edge `0.0781` maxDD `-1.0192`
- `market_context_high->commodity_24h` score `0.5423` n `73` status `ready` deltaP `12.6469` edge `0.1442` maxDD `-4.666`
- `market_context_high->commodity_4h` score `0.5416` n `107` status `ready` deltaP `11.5897` edge `0.0529` maxDD `-2.4692`
- `market_context_high->unknown_1h` score `0.2879` n `107` status `ready` deltaP `7.7537` edge `-0.0018` maxDD `-0.7386`
- `market_context_high->index_1h` score `0.1161` n `107` status `ready` deltaP `8.0489` edge `0.0032` maxDD `-0.3584`
- `market_context_high->equity_1h` score `-0.0811` n `107` status `ready` deltaP `3.8937` edge `0.0239` maxDD `-1.8201`
- `market_context_high->fx_4h` score `-0.1198` n `107` status `ready` deltaP `5.8098` edge `0.002` maxDD `-0.3904`
- `market_context_high->index_24h` score `-0.1358` n `73` status `ready` deltaP `10.515` edge `-0.0445` maxDD `-0.9535`
- `market_context_high->equity_24h` score `-0.1628` n `73` status `ready` deltaP `12.1981` edge `-0.0393` maxDD `-3.1136`
- `market_context_high->metal_4h` score `-0.2652` n `107` status `ready` deltaP `7.3341` edge `-0.0039` maxDD `-2.6532`
- `market_context_high->crypto_major_4h` score `-0.3031` n `107` status `ready` deltaP `3.6358` edge `0.0537` maxDD `-4.3437`
- `market_context_high->metal_1h` score `-0.6016` n `107` status `ready` deltaP `-1.1025` edge `-0.003` maxDD `-1.3425`
- `market_context_high->fx_1h` score `-0.7315` n `107` status `ready` deltaP `-3.7929` edge `0.0005` maxDD `-0.2273`
- `market_context_high->commodity_1h` score `-0.7491` n `107` status `ready` deltaP `-5.2899` edge `0.0005` maxDD `-1.5684`
- `market_context_high->index_4h` score `-0.8898` n `107` status `ready` deltaP `-6.2529` edge `-0.004` maxDD `-0.8045`
- `market_context_high->crypto_major_1h` score `-0.9239` n `107` status `ready` deltaP `-3.0849` edge `-0.0023` maxDD `-3.6463`
- `market_context_high->unknown_24h` score `-1.1302` n `73` status `ready` deltaP `1.4221` edge `-0.0872` maxDD `-1.3741`
- `market_context_high->crypto_alt_1h` score `-1.268` n `107` status `ready` deltaP `-2.9716` edge `0.003` maxDD `-3.1082`
- `market_context_high->crypto_alt_4h` score `-1.7447` n `107` status `ready` deltaP `2.0117` edge `0.0278` maxDD `-11.1916`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
