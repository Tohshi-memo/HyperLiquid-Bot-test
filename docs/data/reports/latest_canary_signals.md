# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T04:37:24.425857+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0258` n `12`; crypto_alt avg `0.1596` n `232`; crypto_major avg `0.1271` n `8`; equity avg `0.032` n `132`; fx avg `-0.0137` n `6`; index avg `0.0028` n `26`; metal avg `0.0169` n `20`; unknown avg `1.5022` n `792`
- 1h: commodity avg `-0.044` n `12`; crypto_alt avg `0.0124` n `232`; crypto_major avg `-0.1074` n `8`; equity avg `-0.0689` n `132`; fx avg `-0.0242` n `6`; index avg `-0.0236` n `26`; metal avg `0.0936` n `20`; unknown avg `0.0332` n `790`
- 4h: commodity avg `-0.1778` n `12`; crypto_alt avg `0.4366` n `232`; crypto_major avg `0.1621` n `8`; equity avg `-0.4409` n `132`; fx avg `-0.0504` n `6`; index avg `-0.1022` n `26`; metal avg `-0.171` n `20`; unknown avg `0.0148` n `790`
- 24h: commodity avg `0.7697` n `12`; crypto_alt avg `-0.8024` n `232`; crypto_major avg `-1.8219` n `8`; equity avg `-2.5796` n `130`; fx avg `-0.0994` n `6`; index avg `-0.463` n `26`; metal avg `-1.0506` n `20`; unknown avg `-0.5043` n `752`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.058`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0522`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0484`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0375`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0373`, n `668`, weak_sample_signal
