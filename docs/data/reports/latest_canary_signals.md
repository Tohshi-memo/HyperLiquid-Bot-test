# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T23:22:27.095391+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0109` n `12`; crypto_alt avg `-0.0908` n `232`; crypto_major avg `-0.0156` n `8`; equity avg `-0.0297` n `132`; fx avg `-0.0029` n `6`; index avg `-0.005` n `26`; metal avg `-0.0221` n `20`; unknown avg `-0.2152` n `792`
- 1h: commodity avg `-0.0193` n `12`; crypto_alt avg `0.108` n `232`; crypto_major avg `0.2345` n `8`; equity avg `0.0042` n `132`; fx avg `-0.0037` n `6`; index avg `0.0035` n `26`; metal avg `-0.0111` n `20`; unknown avg `-0.1423` n `790`
- 4h: commodity avg `0.0785` n `12`; crypto_alt avg `-0.3024` n `232`; crypto_major avg `-0.2019` n `8`; equity avg `-0.2906` n `132`; fx avg `0.02` n `6`; index avg `-0.0033` n `26`; metal avg `-0.0488` n `20`; unknown avg `-0.1246` n `772`
- 24h: commodity avg `0.8748` n `12`; crypto_alt avg `-0.6032` n `232`; crypto_major avg `-1.8236` n `8`; equity avg `-2.1092` n `130`; fx avg `0.0515` n `6`; index avg `-0.3337` n `26`; metal avg `-0.871` n `20`; unknown avg `-0.4722` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.061`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0442`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0424`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0391`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0334`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0314`, n `668`, weak_sample_signal
