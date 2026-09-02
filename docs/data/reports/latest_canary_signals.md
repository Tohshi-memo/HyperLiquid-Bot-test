# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T03:52:25.405175+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0014` n `12`; crypto_alt avg `-0.159` n `232`; crypto_major avg `-0.0588` n `8`; equity avg `-0.0246` n `132`; fx avg `-0.0034` n `6`; index avg `-0.0063` n `26`; metal avg `0.0502` n `20`; unknown avg `0.048` n `792`
- 1h: commodity avg `-0.0335` n `12`; crypto_alt avg `0.1135` n `232`; crypto_major avg `0.293` n `8`; equity avg `-0.0551` n `132`; fx avg `-0.0129` n `6`; index avg `-0.0381` n `26`; metal avg `-0.0763` n `20`; unknown avg `0.4214` n `790`
- 4h: commodity avg `0.0156` n `12`; crypto_alt avg `0.179` n `232`; crypto_major avg `0.0655` n `8`; equity avg `-0.1902` n `132`; fx avg `-0.0647` n `6`; index avg `-0.0602` n `26`; metal avg `-0.2644` n `20`; unknown avg `2.2024` n `790`
- 24h: commodity avg `0.8385` n `12`; crypto_alt avg `-0.8783` n `232`; crypto_major avg `-1.8175` n `8`; equity avg `-2.4389` n `130`; fx avg `-0.0778` n `6`; index avg `-0.4384` n `26`; metal avg `-1.1812` n `20`; unknown avg `-0.0257` n `752`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0566`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.053`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0496`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0448`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0372`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0341`, n `668`, weak_sample_signal
