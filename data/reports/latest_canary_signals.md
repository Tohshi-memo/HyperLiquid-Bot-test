# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T15:22:30.945474+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0211` n `12`; crypto_alt avg `0.0387` n `230`; crypto_major avg `0.0219` n `8`; equity avg `0.0583` n `102`; fx avg `0.004` n `6`; index avg `-0.0127` n `25`; metal avg `0.0142` n `20`; unknown avg `-0.0479` n `782`
- 1h: commodity avg `-0.0055` n `12`; crypto_alt avg `0.1211` n `230`; crypto_major avg `0.097` n `8`; equity avg `0.0813` n `102`; fx avg `0.0221` n `6`; index avg `0.0206` n `25`; metal avg `0.0276` n `20`; unknown avg `1.3252` n `782`
- 4h: commodity avg `-0.0993` n `12`; crypto_alt avg `0.0588` n `230`; crypto_major avg `0.0602` n `8`; equity avg `-0.0665` n `102`; fx avg `-0.054` n `6`; index avg `-0.0226` n `25`; metal avg `0.0251` n `20`; unknown avg `1.0891` n `782`
- 24h: commodity avg `-1.1056` n `12`; crypto_alt avg `0.3341` n `230`; crypto_major avg `0.1434` n `8`; equity avg `0.9219` n `102`; fx avg `-0.1532` n `6`; index avg `0.2174` n `25`; metal avg `0.2445` n `20`; unknown avg `1.4347` n `766`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
