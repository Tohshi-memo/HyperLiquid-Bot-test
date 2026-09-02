# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T05:37:24.680572+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0385` n `12`; crypto_alt avg `0.0278` n `232`; crypto_major avg `0.0355` n `8`; equity avg `0.0825` n `132`; fx avg `-0.0` n `6`; index avg `0.0084` n `26`; metal avg `0.0807` n `20`; unknown avg `0.0224` n `792`
- 1h: commodity avg `0.0587` n `12`; crypto_alt avg `0.3882` n `232`; crypto_major avg `0.2595` n `8`; equity avg `0.2261` n `132`; fx avg `-0.0312` n `6`; index avg `0.0341` n `26`; metal avg `0.1515` n `20`; unknown avg `0.8981` n `790`
- 4h: commodity avg `-0.1941` n `12`; crypto_alt avg `1.4486` n `232`; crypto_major avg `0.8625` n `8`; equity avg `0.1012` n `132`; fx avg `-0.0526` n `6`; index avg `-0.0195` n `26`; metal avg `0.1607` n `20`; unknown avg `0.3498` n `790`
- 24h: commodity avg `0.8424` n `12`; crypto_alt avg `-0.6556` n `232`; crypto_major avg `-1.811` n `8`; equity avg `-2.3998` n `130`; fx avg `-0.0939` n `6`; index avg `-0.459` n `26`; metal avg `-0.9554` n `20`; unknown avg `-0.399` n `752`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.061`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0559`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0514`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0475`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0461`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.045`, n `668`, weak_sample_signal
