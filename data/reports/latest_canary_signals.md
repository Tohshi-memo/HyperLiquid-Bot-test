# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T08:52:17.832683+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0043` n `12`; crypto_alt avg `0.0274` n `228`; crypto_major avg `0.0129` n `8`; equity avg `-0.0409` n `65`; fx avg `-0.0008` n `5`; index avg `-0.0072` n `23`; metal avg `0.0022` n `18`; unknown avg `-0.0255` n `376`
- 1h: commodity avg `-0.0395` n `12`; crypto_alt avg `0.3792` n `228`; crypto_major avg `0.1517` n `8`; equity avg `0.1821` n `65`; fx avg `-0.0008` n `5`; index avg `0.0285` n `23`; metal avg `-0.0156` n `18`; unknown avg `-0.0959` n `376`
- 4h: commodity avg `0.049` n `12`; crypto_alt avg `-0.0951` n `228`; crypto_major avg `-0.0317` n `8`; equity avg `0.1211` n `65`; fx avg `0.0195` n `5`; index avg `0.0532` n `23`; metal avg `0.0189` n `18`; unknown avg `-0.2027` n `355`
- 24h: commodity avg `-0.0075` n `12`; crypto_alt avg `3.925` n `228`; crypto_major avg `2.4195` n `8`; equity avg `2.8521` n `65`; fx avg `-0.0186` n `5`; index avg `1.2147` n `23`; metal avg `-0.0661` n `18`; unknown avg `0.5604` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
