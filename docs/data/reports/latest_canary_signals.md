# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T11:07:31.178930+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.014` n `13`; crypto_alt avg `-0.0813` n `235`; crypto_major avg `-0.0038` n `8`; equity avg `-0.0018` n `143`; fx avg `0.0002` n `6`; index avg `0.0017` n `26`; metal avg `0.0023` n `20`; unknown avg `-0.0316` n `982`
- 1h: commodity avg `-0.0067` n `13`; crypto_alt avg `0.1461` n `235`; crypto_major avg `0.0625` n `8`; equity avg `0.0148` n `143`; fx avg `-0.0016` n `6`; index avg `0.0072` n `26`; metal avg `0.0018` n `20`; unknown avg `-0.0554` n `982`
- 4h: commodity avg `0.0281` n `13`; crypto_alt avg `0.2074` n `235`; crypto_major avg `0.0521` n `8`; equity avg `0.0252` n `143`; fx avg `-0.0137` n `6`; index avg `0.0049` n `26`; metal avg `-0.0055` n `20`; unknown avg `1.293` n `966`
- 24h: commodity avg `0.734` n `13`; crypto_alt avg `-1.8371` n `235`; crypto_major avg `-2.4551` n `8`; equity avg `0.1393` n `142`; fx avg `0.0268` n `6`; index avg `0.1182` n `26`; metal avg `-0.3212` n `20`; unknown avg `-0.3056` n `874`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1943`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1838`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1529`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1512`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
