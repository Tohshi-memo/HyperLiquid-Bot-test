# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T01:52:31.326675+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0276` n `12`; crypto_alt avg `-0.1109` n `230`; crypto_major avg `-0.2662` n `8`; equity avg `0.1449` n `93`; fx avg `0.0105` n `6`; index avg `-0.0173` n `25`; metal avg `-0.0405` n `20`; unknown avg `0.0344` n `767`
- 1h: commodity avg `-0.0569` n `12`; crypto_alt avg `-0.0396` n `230`; crypto_major avg `-0.4488` n `8`; equity avg `0.0683` n `93`; fx avg `0.0207` n `6`; index avg `-0.052` n `25`; metal avg `-0.1147` n `20`; unknown avg `0.2037` n `767`
- 4h: commodity avg `0.1085` n `12`; crypto_alt avg `0.1828` n `230`; crypto_major avg `-0.2925` n `8`; equity avg `0.5811` n `93`; fx avg `0.0467` n `6`; index avg `0.0731` n `25`; metal avg `-0.0699` n `20`; unknown avg `-0.3914` n `765`
- 24h: commodity avg `0.2155` n `12`; crypto_alt avg `1.7122` n `230`; crypto_major avg `2.6806` n `8`; equity avg `1.6626` n `92`; fx avg `0.0725` n `6`; index avg `0.4554` n `25`; metal avg `0.5834` n `20`; unknown avg `0.1692` n `740`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0565`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0547`, n `668`, weak_sample_signal
