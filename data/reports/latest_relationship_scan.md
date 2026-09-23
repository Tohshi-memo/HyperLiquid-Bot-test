# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T20:08:02.046762+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9739`

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

- `market_context_high->unknown_1h` score `77.6539` n `47` status `ready` deltaP `9.8166` edge `6.4128` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `33.2361` n `46` status `ready` deltaP `19.4369` edge `2.6557` maxDD `-0.5817`
- `market_context_high->equity_24h` score `19.0075` n `46` status `ready` deltaP `16.8328` edge `1.4818` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `16.22` n `46` status `ready` deltaP `14.4097` edge `1.2556` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `8.5425` n `96` status `ready` deltaP `-3.2986` edge `1.4197` maxDD `-46.1999`
- `market_context_high->index_24h` score `6.4235` n `46` status `ready` deltaP `25.8605` edge `0.3716` maxDD `-0.03`
- `news_risk_high->crypto_major_4h` score `4.438` n `103` status `ready` deltaP `16.9755` edge `0.3144` maxDD `-2.619`
- `news_risk_high->crypto_alt_4h` score `4.2358` n `103` status `ready` deltaP `12.4023` edge `0.3701` maxDD `-5.9838`
- `news_risk_high->crypto_alt_24h` score `3.329` n `96` status `ready` deltaP `-5.382` edge `0.8014` maxDD `-32.7147`
- `news_risk_high->commodity_24h` score `2.8266` n `96` status `ready` deltaP `26.7361` edge `0.1752` maxDD `-2.431`
- `news_risk_high->crypto_alt_1h` score `2.4334` n `103` status `ready` deltaP `12.8583` edge `0.1661` maxDD `-1.5895`
- `market_context_high->index_4h` score `2.3533` n `47` status `ready` deltaP `28.0812` edge `0.0243` maxDD `-0.2323`
- `news_risk_high->crypto_major_1h` score `2.0241` n `103` status `ready` deltaP `15.7026` edge `0.1075` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.4308` n `103` status `ready` deltaP `21.3948` edge `0.0402` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.2316` n `96` status `ready` deltaP `29.1667` edge `0.1224` maxDD `-1.7159`
- `market_context_high->metal_24h` score `1.0795` n `46` status `ready` deltaP `19.837` edge `-0.0189` maxDD `-0.2042`
- `market_context_high->equity_4h` score `0.996` n `47` status `ready` deltaP `8.7603` edge `0.0664` maxDD `-1.3444`
- `market_context_high->index_1h` score `0.6852` n `47` status `ready` deltaP `11.6161` edge `0.0075` maxDD `-0.2275`
- `news_risk_high->metal_1h` score `0.6194` n `103` status `ready` deltaP `15.2026` edge `0.0096` maxDD `-0.7468`
- `news_risk_high->metal_24h` score `0.5327` n `96` status `ready` deltaP `16.6667` edge `0.0416` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
