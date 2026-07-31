# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T09:07:36.111206+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0953` n `12`; crypto_alt avg `-0.1262` n `230`; crypto_major avg `-0.0449` n `8`; equity avg `0.2476` n `102`; fx avg `-0.0992` n `6`; index avg `0.0292` n `25`; metal avg `-0.0051` n `20`; unknown avg `-0.0129` n `780`
- 1h: commodity avg `0.1532` n `12`; crypto_alt avg `-0.3644` n `230`; crypto_major avg `-0.0779` n `8`; equity avg `0.523` n `102`; fx avg `-0.0904` n `6`; index avg `0.038` n `25`; metal avg `-0.0647` n `20`; unknown avg `0.01` n `780`
- 4h: commodity avg `0.1979` n `12`; crypto_alt avg `-0.1044` n `230`; crypto_major avg `-0.5142` n `8`; equity avg `0.1689` n `102`; fx avg `-0.1886` n `6`; index avg `0.0185` n `25`; metal avg `-0.194` n `20`; unknown avg `-0.0749` n `747`
- 24h: commodity avg `-0.1902` n `12`; crypto_alt avg `-0.2804` n `230`; crypto_major avg `0.0894` n `8`; equity avg `8.8657` n `102`; fx avg `-0.2977` n `6`; index avg `1.2933` n `25`; metal avg `0.2333` n `20`; unknown avg `-0.0137` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0638`, n `668`, weak_sample_signal
