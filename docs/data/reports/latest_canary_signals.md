# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T10:52:30.729348+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0184` n `12`; crypto_alt avg `0.0852` n `228`; crypto_major avg `0.0324` n `8`; equity avg `0.0286` n `79`; fx avg `0.0148` n `6`; index avg `-0.0035` n `23`; metal avg `-0.0202` n `20`; unknown avg `0.3509` n `722`
- 1h: commodity avg `0.0203` n `12`; crypto_alt avg `0.1632` n `228`; crypto_major avg `0.0671` n `8`; equity avg `0.0632` n `79`; fx avg `0.02` n `6`; index avg `0.0346` n `23`; metal avg `-0.0137` n `18`; unknown avg `0.3361` n `701`
- 4h: commodity avg `0.0448` n `12`; crypto_alt avg `0.4998` n `228`; crypto_major avg `0.6199` n `8`; equity avg `0.2312` n `79`; fx avg `0.0643` n `6`; index avg `0.0539` n `23`; metal avg `-0.1232` n `18`; unknown avg `0.2798` n `693`
- 24h: commodity avg `-0.1774` n `12`; crypto_alt avg `-0.366` n `228`; crypto_major avg `-0.2177` n `8`; equity avg `-0.1313` n `79`; fx avg `0.158` n `6`; index avg `0.0609` n `23`; metal avg `0.4529` n `18`; unknown avg `0.4559` n `637`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
