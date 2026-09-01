# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T02:52:26.526703+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0048` n `12`; crypto_alt avg `0.1088` n `232`; crypto_major avg `0.1325` n `8`; equity avg `0.0315` n `130`; fx avg `-0.0039` n `6`; index avg `0.0063` n `26`; metal avg `0.0768` n `20`; unknown avg `-0.0559` n `792`
- 1h: commodity avg `0.054` n `12`; crypto_alt avg `-0.3096` n `232`; crypto_major avg `-0.0675` n `8`; equity avg `-0.1822` n `130`; fx avg `-0.0135` n `6`; index avg `-0.0389` n `26`; metal avg `-0.0211` n `20`; unknown avg `-0.0828` n `790`
- 4h: commodity avg `0.0884` n `12`; crypto_alt avg `0.3325` n `232`; crypto_major avg `-0.1738` n `8`; equity avg `-0.1109` n `130`; fx avg `0.0098` n `6`; index avg `0.0295` n `26`; metal avg `0.0021` n `20`; unknown avg `0.3463` n `790`
- 24h: commodity avg `0.3884` n `12`; crypto_alt avg `2.0811` n `231`; crypto_major avg `1.9297` n `8`; equity avg `1.4155` n `130`; fx avg `-0.0275` n `6`; index avg `0.1713` n `26`; metal avg `0.0301` n `20`; unknown avg `0.2622` n `751`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0566`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0511`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0489`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0464`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0452`, n `668`, weak_sample_signal
