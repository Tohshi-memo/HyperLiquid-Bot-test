# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T14:52:29.676531+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.033` n `12`; crypto_alt avg `-0.3455` n `229`; crypto_major avg `-0.3042` n `8`; equity avg `-0.8639` n `88`; fx avg `0.0004` n `6`; index avg `-0.1386` n `25`; metal avg `-0.0048` n `20`; unknown avg `0.2609` n `763`
- 1h: commodity avg `-0.0994` n `12`; crypto_alt avg `-1.1126` n `229`; crypto_major avg `-0.9775` n `8`; equity avg `-2.2927` n `88`; fx avg `0.0038` n `6`; index avg `-0.3863` n `25`; metal avg `-0.2935` n `20`; unknown avg `0.2901` n `763`
- 4h: commodity avg `-0.0023` n `12`; crypto_alt avg `-0.0111` n `229`; crypto_major avg `0.7316` n `8`; equity avg `-0.4886` n `88`; fx avg `0.0059` n `6`; index avg `-0.0642` n `25`; metal avg `0.601` n `20`; unknown avg `-0.3207` n `763`
- 24h: commodity avg `-0.2103` n `12`; crypto_alt avg `1.6325` n `228`; crypto_major avg `3.0154` n `8`; equity avg `-1.7281` n `88`; fx avg `-0.0477` n `6`; index avg `-0.4359` n `25`; metal avg `0.5522` n `20`; unknown avg `1.3905` n `739`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
