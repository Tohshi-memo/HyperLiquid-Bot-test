# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T02:52:29.189606+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0095` n `12`; crypto_alt avg `0.0855` n `232`; crypto_major avg `0.048` n `8`; equity avg `0.0185` n `132`; fx avg `0.0088` n `6`; index avg `0.0128` n `26`; metal avg `-0.0151` n `20`; unknown avg `-0.1269` n `792`
- 1h: commodity avg `-0.1482` n `12`; crypto_alt avg `1.2328` n `232`; crypto_major avg `0.7814` n `8`; equity avg `0.1324` n `132`; fx avg `-0.0147` n `6`; index avg `0.0344` n `26`; metal avg `0.105` n `20`; unknown avg `3.366` n `790`
- 4h: commodity avg `0.0281` n `12`; crypto_alt avg `0.3363` n `232`; crypto_major avg `0.0417` n `8`; equity avg `-0.1302` n `132`; fx avg `-0.0764` n `6`; index avg `-0.0084` n `26`; metal avg `-0.1655` n `20`; unknown avg `-0.013` n `790`
- 24h: commodity avg `0.8541` n `12`; crypto_alt avg `-0.4962` n `232`; crypto_major avg `-1.7021` n `8`; equity avg `-2.163` n `130`; fx avg `-0.0413` n `6`; index avg `-0.3694` n `26`; metal avg `-1.0402` n `20`; unknown avg `-0.0549` n `752`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.06`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0444`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0441`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0426`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0346`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0333`, n `668`, weak_sample_signal
