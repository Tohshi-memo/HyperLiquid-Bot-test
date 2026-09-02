# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T04:52:25.028737+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0086` n `12`; crypto_alt avg `0.1705` n `232`; crypto_major avg `0.0719` n `8`; equity avg `0.026` n `132`; fx avg `-0.0154` n `6`; index avg `-0.0001` n `26`; metal avg `0.0058` n `20`; unknown avg `0.81` n `792`
- 1h: commodity avg `-0.0368` n `12`; crypto_alt avg `0.3454` n `232`; crypto_major avg `0.0232` n `8`; equity avg `-0.0184` n `132`; fx avg `-0.0361` n `6`; index avg `-0.0175` n `26`; metal avg `0.0491` n `20`; unknown avg `0.022` n `790`
- 4h: commodity avg `-0.2336` n `12`; crypto_alt avg `0.8276` n `232`; crypto_major avg `0.3532` n `8`; equity avg `-0.2839` n `132`; fx avg `-0.0561` n `6`; index avg `-0.087` n `26`; metal avg `-0.1235` n `20`; unknown avg `0.0305` n `790`
- 24h: commodity avg `0.7247` n `12`; crypto_alt avg `-0.5158` n `232`; crypto_major avg `-1.6788` n `8`; equity avg `-2.5141` n `130`; fx avg `-0.1232` n `6`; index avg `-0.458` n `26`; metal avg `-1.0237` n `20`; unknown avg `-0.4202` n `752`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0578`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0528`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0476`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0398`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0381`, n `668`, weak_sample_signal
