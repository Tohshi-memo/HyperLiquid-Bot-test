# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-04T09:52:30.903860+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4040`

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

- `news_risk_high->crypto_alt_4h` score `0.1977` n `146` status `ready` deltaP `8.2192` edge `0.2342` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4215` n `146` status `ready` deltaP `2.631` edge `0.0512` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7269` n `146` status `ready` deltaP `-2.9714` edge `-0.0033` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.852` n `146` status `ready` deltaP `1.6467` edge `-0.002` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.3421` n `146` status `ready` deltaP `-5.5471` edge `-0.0129` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.4701` n `146` status `ready` deltaP `-7.622` edge `-0.0125` maxDD `-1.6794`
- `news_risk_high->index_24h` score `-1.7955` n `146` status `ready` deltaP `0.509` edge `0.0506` maxDD `-7.402`
- `news_risk_high->index_4h` score `-1.8295` n `146` status `ready` deltaP `0.2318` edge `-0.006` maxDD `-4.0745`
- `news_risk_high->metal_24h` score `-2.014` n `146` status `ready` deltaP `9.1729` edge `0.1292` maxDD `-16.6552`
- `news_risk_high->fx_24h` score `-2.3586` n `146` status `ready` deltaP `-17.8534` edge `-0.0125` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.4331` n `146` status `ready` deltaP `-9.6752` edge `-0.0016` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.5909` n `146` status `ready` deltaP `-5.5881` edge `-0.0273` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.0617` n `146` status `ready` deltaP `-6.958` edge `-0.0362` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.8556` n `146` status `ready` deltaP `-12.475` edge `-0.0027` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.6502` n `146` status `ready` deltaP `-4.0991` edge `-0.0397` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.6049` n `146` status `ready` deltaP `-11.3348` edge `-0.0729` maxDD `-24.1554`
- `news_risk_high->crypto_alt_24h` score `-7.9284` n `146` status `ready` deltaP `17.8059` edge `0.5643` maxDD `-118.6236`
- `news_risk_high->equity_24h` score `-10.118` n `146` status `ready` deltaP `15.3753` edge `0.5047` maxDD `-102.3626`
- `news_risk_high->equity_4h` score `-11.2132` n `146` status `ready` deltaP `-0.5304` edge `-0.0948` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.2979` n `146` status `ready` deltaP `-20.7834` edge `-0.0602` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
