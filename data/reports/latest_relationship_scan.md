# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-03T04:52:27.276526+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4572`

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

- `news_risk_high->crypto_alt_4h` score `0.1735` n `146` status `ready` deltaP `5.3229` edge `0.2504` maxDD `-14.0916`
- `news_risk_high->crypto_alt_24h` score `-0.1271` n `128` status `ready` deltaP `22.6562` edge `0.8666` maxDD `-71.3817`
- `news_risk_high->crypto_alt_1h` score `-0.4713` n `146` status `ready` deltaP `1.5831` edge `0.0518` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.5953` n `146` status `ready` deltaP `-0.5762` edge `-0.0024` maxDD `-0.6065`
- `news_risk_high->metal_24h` score `-0.8288` n `128` status `ready` deltaP `12.8472` edge `0.1337` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-0.9035` n `146` status `ready` deltaP `1.1976` edge `-0.0033` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.2087` n `146` status `ready` deltaP `-2.8963` edge `-0.0105` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.2922` n `146` status `ready` deltaP `-5.098` edge `-0.0095` maxDD `-3.1082`
- `news_risk_high->equity_24h` score `-1.8492` n `128` status `ready` deltaP `17.7951` edge `0.6538` maxDD `-67.0937`
- `news_risk_high->index_24h` score `-2.07` n `128` status `ready` deltaP `-2.0833` edge `0.0327` maxDD `-7.402`
- `news_risk_high->index_4h` score `-2.1492` n `146` status `ready` deltaP `-4.3414` edge `-0.0165` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.39` n `146` status `ready` deltaP `-9.0764` edge `-0.002` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.5059` n `128` status `ready` deltaP `-19.9653` edge `-0.0173` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.7023` n `146` status `ready` deltaP `-6.9354` edge `-0.0326` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.2307` n `146` status `ready` deltaP `-8.1556` edge `-0.0423` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.7892` n `146` status `ready` deltaP `-12.1701` edge `0.0008` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.9081` n `146` status `ready` deltaP `-7.7577` edge `-0.0368` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.0694` n `146` status `ready` deltaP `-14.2312` edge `-0.0923` maxDD `-24.1554`
- `news_risk_high->crypto_major_24h` score `-8.9423` n `128` status `ready` deltaP `-12.7604` edge `0.0715` maxDD `-47.1967`
- `news_risk_high->commodity_24h` score `-11.4221` n `128` status `ready` deltaP `-24.3924` edge `-0.0795` maxDD `-34.4447`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
