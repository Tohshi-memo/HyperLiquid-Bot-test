# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T07:07:26.519159+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1425` n `12`; crypto_alt avg `0.1496` n `232`; crypto_major avg `0.1168` n `8`; equity avg `0.1275` n `132`; fx avg `0.0214` n `6`; index avg `0.0432` n `26`; metal avg `0.0605` n `20`; unknown avg `0.1859` n `790`
- 1h: commodity avg `-0.1387` n `12`; crypto_alt avg `0.0633` n `232`; crypto_major avg `-0.0548` n `8`; equity avg `0.0143` n `132`; fx avg `0.0129` n `6`; index avg `0.0476` n `26`; metal avg `0.0248` n `20`; unknown avg `0.9042` n `786`
- 4h: commodity avg `-0.1477` n `12`; crypto_alt avg `0.3004` n `232`; crypto_major avg `0.2099` n `8`; equity avg `0.1166` n `132`; fx avg `-0.1054` n `6`; index avg `0.0041` n `26`; metal avg `0.195` n `20`; unknown avg `0.7581` n `770`
- 24h: commodity avg `0.6742` n `12`; crypto_alt avg `-0.6122` n `232`; crypto_major avg `-1.5983` n `8`; equity avg `-2.4941` n `130`; fx avg `-0.1701` n `6`; index avg `-0.4527` n `26`; metal avg `-0.8764` n `20`; unknown avg `-0.1381` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0541`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0526`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0451`, n `668`, weak_sample_signal
