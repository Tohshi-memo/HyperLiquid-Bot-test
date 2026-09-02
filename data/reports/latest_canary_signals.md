# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T14:52:38.820944+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1085` n `12`; crypto_alt avg `-0.0864` n `232`; crypto_major avg `-0.0361` n `8`; equity avg `-0.3088` n `133`; fx avg `-0.0015` n `6`; index avg `-0.032` n `26`; metal avg `-0.0156` n `20`; unknown avg `16.5372` n `791`
- 1h: commodity avg `0.2344` n `12`; crypto_alt avg `-0.4033` n `232`; crypto_major avg `-0.2268` n `8`; equity avg `0.1358` n `133`; fx avg `0.0098` n `6`; index avg `0.099` n `26`; metal avg `-0.0488` n `20`; unknown avg `0.2161` n `789`
- 4h: commodity avg `0.0491` n `12`; crypto_alt avg `0.6513` n `232`; crypto_major avg `1.0562` n `8`; equity avg `0.98` n `133`; fx avg `-0.1426` n `6`; index avg `0.2498` n `26`; metal avg `0.6431` n `20`; unknown avg `1.0291` n `789`
- 24h: commodity avg `0.7603` n `12`; crypto_alt avg `-1.5209` n `232`; crypto_major avg `-1.8033` n `8`; equity avg `-0.5634` n `132`; fx avg `-0.3527` n `6`; index avg `-0.1126` n `26`; metal avg `0.1427` n `20`; unknown avg `-0.245` n `751`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0521`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0462`, n `668`, weak_sample_signal
