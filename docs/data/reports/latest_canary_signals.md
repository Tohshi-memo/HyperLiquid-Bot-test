# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T18:52:26.636266+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0071` n `12`; crypto_alt avg `0.089` n `231`; crypto_major avg `0.1059` n `8`; equity avg `0.0262` n `128`; fx avg `-0.0016` n `6`; index avg `0.0039` n `26`; metal avg `0.0054` n `20`; unknown avg `-0.1496` n `792`
- 1h: commodity avg `-0.0037` n `12`; crypto_alt avg `0.3077` n `231`; crypto_major avg `0.2681` n `8`; equity avg `0.0303` n `128`; fx avg `-0.0119` n `6`; index avg `-0.0015` n `26`; metal avg `0.0078` n `20`; unknown avg `-0.045` n `792`
- 4h: commodity avg `-0.0061` n `12`; crypto_alt avg `-0.1367` n `231`; crypto_major avg `0.1733` n `8`; equity avg `0.0205` n `128`; fx avg `-0.0078` n `6`; index avg `0.0044` n `26`; metal avg `0.0386` n `20`; unknown avg `-0.3325` n `786`
- 24h: commodity avg `0.0456` n `12`; crypto_alt avg `1.7103` n `231`; crypto_major avg `1.9065` n `8`; equity avg `0.4682` n `128`; fx avg `-0.0413` n `6`; index avg `0.0592` n `26`; metal avg `0.1631` n `20`; unknown avg `0.2063` n `728`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2263`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1389`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1318`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0609`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0582`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.057`, n `668`, weak_sample_signal
