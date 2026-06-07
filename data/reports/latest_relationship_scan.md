# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T04:52:26.931553+00:00`
- Price records: `672`
- Market context records: `3145`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8008`

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

- `market_context_high->commodity_24h` score `14.2726` n `109` status `ready` deltaP `47.5965` edge `0.9149` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `11.9483` n `109` status `ready` deltaP `22.1537` edge `0.8968` maxDD `-1.9039`
- `market_context_high->crypto_alt_24h` score `11.3591` n `109` status `ready` deltaP `12.046` edge `2.3736` maxDD `-71.142`
- `market_context_high->index_24h` score `6.5779` n `109` status `ready` deltaP `31.2563` edge `0.8904` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.6489` n `109` status `ready` deltaP `12.4395` edge `1.3547` maxDD `-53.663`
- `market_context_high->commodity_4h` score `2.779` n `146` status `ready` deltaP `18.0275` edge `0.1572` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `0.1666` n `146` status `ready` deltaP `4.2819` edge `0.0276` maxDD `-1.7142`
- `market_context_high->crypto_alt_1h` score `-0.3712` n `146` status `ready` deltaP `6.3551` edge `0.123` maxDD `-14.7034`
- `market_context_high->fx_24h` score `-0.4057` n `109` status `ready` deltaP `6.0079` edge `-0.0011` maxDD `-0.4876`
- `market_context_high->index_1h` score `-0.5164` n `146` status `ready` deltaP `3.5518` edge `0.0164` maxDD `-4.5023`
- `market_context_high->equity_1h` score `-0.8184` n `146` status `ready` deltaP `3.4882` edge `0.0204` maxDD `-8.8863`
- `market_context_high->crypto_major_1h` score `-0.9515` n `146` status `ready` deltaP `3.5251` edge `0.0808` maxDD `-15.1032`
- `market_context_high->index_4h` score `-1.1212` n `146` status `ready` deltaP `12.0239` edge `0.067` maxDD `-17.6057`
- `market_context_high->fx_1h` score `-1.1516` n `146` status `ready` deltaP `-11.0676` edge `-0.0056` maxDD `-0.7941`
- `market_context_high->fx_4h` score `-1.4883` n `146` status `ready` deltaP `-14.0745` edge `-0.0085` maxDD `-1.4115`
- `market_context_high->unknown_4h` score `-1.5853` n `146` status `ready` deltaP `6.0015` edge `0.0501` maxDD `-14.7778`
- `market_context_high->metal_1h` score `-2.054` n `146` status `ready` deltaP `-4.1547` edge `-0.0041` maxDD `-7.4828`
- `market_context_high->equity_4h` score `-2.7706` n `146` status `ready` deltaP `13.9283` edge `0.0825` maxDD `-36.7784`
- `market_context_high->crypto_alt_4h` score `-2.8486` n `146` status `ready` deltaP `19.4244` edge `0.4376` maxDD `-58.6918`
- `market_context_high->unknown_1h` score `-3.1765` n `146` status `ready` deltaP `1.6098` edge `-0.0728` maxDD `-14.2111`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
