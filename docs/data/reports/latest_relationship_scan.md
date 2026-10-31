# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T22:22:25.713730+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6579`

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

- `market_context_high->unknown_24h` score `3488.3828` n `89` status `ready` deltaP `-11.2886` edge `290.8168` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `120.1837` n `89` status `ready` deltaP `1.1852` edge `10.0207` maxDD `-0.3966`
- `news_risk_high->unknown_1h` score `77.3716` n `108` status `ready` deltaP `-5.1951` edge `6.5109` maxDD `-0.9571`
- `news_risk_high->crypto_alt_24h` score `18.6657` n `83` status `ready` deltaP `44.639` edge `1.263` maxDD `-0.0763`
- `market_context_high->equity_24h` score `10.6843` n `89` status `ready` deltaP `23.1254` edge `1.0119` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `5.55` n `108` status `ready` deltaP `21.0366` edge `0.4609` maxDD `-7.4246`
- `market_context_high->index_24h` score `4.9765` n `89` status `ready` deltaP `43.9822` edge `0.1398` maxDD `-0.1315`
- `market_context_high->metal_4h` score `1.4846` n `89` status `ready` deltaP `18.4656` edge `0.0431` maxDD `-0.7323`
- `market_context_high->commodity_4h` score `0.8402` n `89` status `ready` deltaP `17.342` edge `0.0654` maxDD `-0.5298`
- `news_risk_high->crypto_alt_1h` score `0.8361` n `108` status `ready` deltaP `8.8767` edge `0.1059` maxDD `-3.9659`
- `market_context_high->metal_1h` score `0.8152` n `89` status `ready` deltaP `11.6464` edge `0.0193` maxDD `-0.3209`
- `market_context_high->fx_4h` score `0.5317` n `89` status `ready` deltaP `12.2722` edge `0.0016` maxDD `-0.1285`
- `market_context_high->fx_1h` score `0.4691` n `89` status `ready` deltaP `11.7994` edge `-0.0001` maxDD `-0.1407`
- `market_context_high->equity_4h` score `0.4457` n `89` status `ready` deltaP `1.0756` edge `0.1893` maxDD `-4.48`
- `market_context_high->equity_1h` score `0.3974` n `89` status `ready` deltaP `5.0562` edge `0.1048` maxDD `-2.3383`
- `market_context_high->crypto_major_1h` score `0.2326` n `89` status `ready` deltaP `7.4531` edge `0.0829` maxDD `-5.2213`
- `market_context_high->commodity_1h` score `-0.4303` n `89` status `ready` deltaP `-2.7367` edge `0.0145` maxDD `-0.4475`
- `market_context_high->metal_24h` score `-0.4362` n `89` status `ready` deltaP `7.5257` edge `0.1586` maxDD `-10.5088`
- `market_context_high->index_1h` score `-0.5497` n `89` status `ready` deltaP `1.2363` edge `0.0018` maxDD `-1.1344`
- `market_context_high->crypto_major_4h` score `-0.6329` n `89` status `ready` deltaP `14.0055` edge `0.0995` maxDD `-14.5879`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
