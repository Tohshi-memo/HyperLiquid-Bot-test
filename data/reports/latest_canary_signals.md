# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T06:52:33.658935+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0053` n `12`; crypto_alt avg `0.0077` n `228`; crypto_major avg `0.0023` n `8`; equity avg `0.0262` n `74`; fx avg `-0.003` n `6`; index avg `0.0079` n `23`; metal avg `0.0109` n `18`; unknown avg `0.1652` n `643`
- 1h: commodity avg `-0.0479` n `12`; crypto_alt avg `-0.1172` n `228`; crypto_major avg `-0.1581` n `8`; equity avg `0.0465` n `74`; fx avg `-0.0112` n `6`; index avg `0.0015` n `23`; metal avg `-0.0008` n `18`; unknown avg `1.6007` n `625`
- 4h: commodity avg `-0.1189` n `12`; crypto_alt avg `-0.3463` n `228`; crypto_major avg `-0.4792` n `8`; equity avg `0.0072` n `74`; fx avg `0.0017` n `6`; index avg `0.0044` n `23`; metal avg `0.012` n `18`; unknown avg `-0.0569` n `625`
- 24h: commodity avg `-0.6483` n `12`; crypto_alt avg `0.7386` n `228`; crypto_major avg `0.9532` n `8`; equity avg `0.7254` n `74`; fx avg `-0.0191` n `6`; index avg `0.2298` n `23`; metal avg `0.3274` n `18`; unknown avg `-0.4818` n `599`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0655`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0637`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0628`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
