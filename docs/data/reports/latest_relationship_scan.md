# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T19:52:26.592336+00:00`
- Price records: `672`
- Market context records: `5589`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11423`

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

- `market_context_high->equity_24h` score `3.8167` n `174` status `ready` deltaP `15.0084` edge `0.7259` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `1.1825` n `204` status `ready` deltaP `11.8633` edge `0.2487` maxDD `-14.0065`
- `market_context_high->fx_24h` score `1.0326` n `174` status `ready` deltaP `19.3547` edge `0.0544` maxDD `-1.457`
- `market_context_high->equity_4h` score `0.6119` n `204` status `ready` deltaP `6.5937` edge `0.1709` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `0.5199` n `204` status `ready` deltaP `6.8867` edge `0.1615` maxDD `-9.46`
- `market_context_high->crypto_major_24h` score `0.0757` n `174` status `ready` deltaP `12.4102` edge `0.3776` maxDD `-29.6555`
- `market_context_high->equity_1h` score `-0.1862` n `216` status `ready` deltaP `6.0629` edge `0.0364` maxDD `-5.0555`
- `market_context_high->fx_1h` score `-0.2761` n `216` status `ready` deltaP `1.594` edge `0.0008` maxDD `-0.4122`
- `market_context_high->index_1h` score `-0.3283` n `216` status `ready` deltaP `2.2622` edge `0.0069` maxDD `-0.9472`
- `market_context_high->crypto_major_1h` score `-0.4154` n `216` status `ready` deltaP `3.7037` edge `0.0466` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.5981` n `216` status `ready` deltaP `-1.3889` edge `0.0001` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.6352` n `216` status `ready` deltaP `0.7236` edge `0.0384` maxDD `-5.0257`
- `market_context_high->fx_4h` score `-0.8139` n `204` status `ready` deltaP `3.9455` edge `0.0087` maxDD `-0.8928`
- `market_context_high->commodity_1h` score `-1.1963` n `216` status `ready` deltaP `-2.301` edge `-0.0078` maxDD `-3.7906`
- `market_context_high->index_4h` score `-1.5173` n `204` status `ready` deltaP `2.9979` edge `0.0145` maxDD `-2.874`
- `market_context_high->index_24h` score `-2.2416` n `174` status `ready` deltaP `11.1291` edge `0.0371` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.9871` n `204` status `ready` deltaP `-12.8109` edge `-0.0592` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-4.1543` n `204` status `ready` deltaP `-4.9259` edge `-0.0458` maxDD `-14.071`
- `market_context_high->metal_24h` score `-8.0068` n `174` status `ready` deltaP `-8.3273` edge `-0.2349` maxDD `-32.8874`
- `market_context_high->crypto_alt_24h` score `-10.028` n `174` status `ready` deltaP `2.1971` edge `0.0194` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
