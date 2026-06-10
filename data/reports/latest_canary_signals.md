# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T00:22:22.003824+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.3219` n `12`; crypto_alt avg `-0.131` n `228`; crypto_major avg `-0.2036` n `8`; equity avg `-0.1595` n `74`; fx avg `-0.0487` n `6`; index avg `-0.0581` n `23`; metal avg `0.0005` n `18`; unknown avg `-0.1024` n `547`
- 1h: commodity avg `0.2059` n `12`; crypto_alt avg `0.0972` n `228`; crypto_major avg `0.0082` n `8`; equity avg `0.5063` n `74`; fx avg `-0.1215` n `6`; index avg `0.1349` n `23`; metal avg `-0.0249` n `18`; unknown avg `-0.0936` n `547`
- 4h: commodity avg `0.5461` n `12`; crypto_alt avg `-0.3349` n `228`; crypto_major avg `-0.563` n `8`; equity avg `-0.0547` n `74`; fx avg `-0.0946` n `6`; index avg `0.073` n `23`; metal avg `-0.4884` n `18`; unknown avg `-0.2761` n `547`
- 24h: commodity avg `-0.322` n `12`; crypto_alt avg `-0.81` n `228`; crypto_major avg `-2.5784` n `8`; equity avg `-1.4838` n `74`; fx avg `-0.0922` n `6`; index avg `-0.5136` n `23`; metal avg `-1.5961` n `18`; unknown avg `-0.3831` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0649`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0617`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.054`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0413`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0408`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0389`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0371`, n `668`, weak_sample_signal
