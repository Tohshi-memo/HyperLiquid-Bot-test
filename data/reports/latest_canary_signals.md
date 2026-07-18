# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T16:37:30.027013+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0228` n `12`; crypto_alt avg `0.0526` n `230`; crypto_major avg `0.0755` n `8`; equity avg `0.0174` n `96`; fx avg `0.0` n `6`; index avg `-0.0017` n `25`; metal avg `-0.005` n `20`; unknown avg `-0.006` n `770`
- 1h: commodity avg `0.0111` n `12`; crypto_alt avg `0.089` n `230`; crypto_major avg `0.0799` n `8`; equity avg `-0.0363` n `96`; fx avg `-0.0382` n `6`; index avg `-0.0129` n `25`; metal avg `-0.0072` n `20`; unknown avg `-0.0529` n `770`
- 4h: commodity avg `-0.0044` n `12`; crypto_alt avg `-0.006` n `230`; crypto_major avg `0.1866` n `8`; equity avg `-0.0833` n `96`; fx avg `-0.0447` n `6`; index avg `-0.0157` n `25`; metal avg `-0.0464` n `20`; unknown avg `-0.0933` n `770`
- 24h: commodity avg `0.2912` n `12`; crypto_alt avg `-0.846` n `230`; crypto_major avg `0.1799` n `8`; equity avg `-0.9263` n `96`; fx avg `-0.1039` n `6`; index avg `-0.055` n `25`; metal avg `-0.0051` n `20`; unknown avg `0.0268` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
