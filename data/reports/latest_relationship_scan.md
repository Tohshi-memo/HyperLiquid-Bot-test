# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T18:22:23.579331+00:00`
- Price records: `672`
- Market context records: `1143`
- Flow alert records: `5191`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8749`

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

- `market_context_high->crypto_major_24h` score `19.9817` n `151` status `ready` deltaP `43.1521` edge `1.4546` maxDD `-5.5043`
- `market_context_high->crypto_alt_24h` score `9.7569` n `151` status `ready` deltaP `19.5088` edge `0.8449` maxDD `-12.2838`
- `market_context_high->equity_24h` score `7.8552` n `151` status `ready` deltaP `18.988` edge `0.5966` maxDD `-4.8203`
- `market_context_high->index_24h` score `6.1445` n `151` status `ready` deltaP `17.5991` edge `0.4364` maxDD `-2.668`
- `market_context_high->metal_24h` score `5.716` n `151` status `ready` deltaP `-1.7477` edge `0.6547` maxDD `-6.3373`
- `market_context_high->equity_4h` score `2.3776` n `168` status `ready` deltaP `11.7088` edge `0.1864` maxDD `-3.6396`
- `market_context_high->index_4h` score `1.1081` n `168` status `ready` deltaP `9.0519` edge `0.1003` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.5601` n `168` status `ready` deltaP `8.0945` edge `0.0244` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.4899` n `168` status `ready` deltaP `3.7781` edge `0.0534` maxDD `-1.3546`
- `market_context_high->crypto_major_4h` score `0.3378` n `168` status `ready` deltaP `9.8287` edge `0.1699` maxDD `-8.3693`
- `market_context_high->fx_1h` score `0.14` n `168` status `ready` deltaP `8.3155` edge `0.0018` maxDD `-0.3124`
- `market_context_high->crypto_major_1h` score `0.1281` n `168` status `ready` deltaP `7.2819` edge `0.0387` maxDD `-4.1256`
- `market_context_high->metal_1h` score `-0.1837` n `168` status `ready` deltaP `7.1001` edge `-0.0016` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.1854` n `168` status `ready` deltaP `3.2435` edge `0.0472` maxDD `-3.4088`
- `market_context_high->fx_4h` score `-0.735` n `168` status `ready` deltaP `0.6315` edge `0.0012` maxDD `-1.6381`
- `market_context_high->crypto_alt_4h` score `-0.8034` n `168` status `ready` deltaP `7.063` edge `0.1464` maxDD `-16.7194`
- `market_context_high->commodity_1h` score `-0.8385` n `168` status `ready` deltaP `-2.9726` edge `-0.0069` maxDD `-3.7959`
- `market_context_high->metal_4h` score `-2.2903` n `168` status `ready` deltaP `7.4622` edge `-0.0452` maxDD `-9.2991`
- `market_context_high->unknown_24h` score `-3.0117` n `151` status `ready` deltaP `3.854` edge `-0.0037` maxDD `-10.1706`
- `market_context_high->commodity_4h` score `-3.3633` n `168` status `ready` deltaP `-12.95` edge `-0.0281` maxDD `-13.0076`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
