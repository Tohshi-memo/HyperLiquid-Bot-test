# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T18:22:28.943775+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.007` n `12`; crypto_alt avg `-0.1488` n `229`; crypto_major avg `-0.1706` n `8`; equity avg `-0.0366` n `88`; fx avg `0.0` n `6`; index avg `-0.0032` n `25`; metal avg `0.0035` n `20`; unknown avg `0.0304` n `765`
- 1h: commodity avg `-0.0165` n `12`; crypto_alt avg `0.0796` n `229`; crypto_major avg `0.2479` n `8`; equity avg `0.0027` n `88`; fx avg `-0.0051` n `6`; index avg `0.0206` n `25`; metal avg `0.0155` n `20`; unknown avg `-0.3451` n `765`
- 4h: commodity avg `0.005` n `12`; crypto_alt avg `0.9485` n `229`; crypto_major avg `0.7607` n `8`; equity avg `0.0286` n `88`; fx avg `0.013` n `6`; index avg `-0.0246` n `25`; metal avg `0.035` n `20`; unknown avg `0.0053` n `765`
- 24h: commodity avg `-0.0069` n `12`; crypto_alt avg `1.46` n `229`; crypto_major avg `1.7459` n `8`; equity avg `0.142` n `88`; fx avg `-0.0171` n `6`; index avg `-0.081` n `25`; metal avg `0.0511` n `20`; unknown avg `0.8132` n `741`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0657`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
