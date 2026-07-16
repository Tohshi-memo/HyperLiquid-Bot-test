# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T20:37:31.725070+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0394` n `12`; crypto_alt avg `0.0046` n `230`; crypto_major avg `-0.0175` n `8`; equity avg `0.0233` n `94`; fx avg `0.0029` n `6`; index avg `-0.0048` n `25`; metal avg `-0.0015` n `20`; unknown avg `-0.0349` n `768`
- 1h: commodity avg `0.0547` n `12`; crypto_alt avg `0.0167` n `230`; crypto_major avg `-0.0761` n `8`; equity avg `0.0135` n `94`; fx avg `-0.0072` n `6`; index avg `0.0504` n `25`; metal avg `0.0157` n `20`; unknown avg `-0.1476` n `768`
- 4h: commodity avg `0.0829` n `12`; crypto_alt avg `-0.6012` n `230`; crypto_major avg `-0.859` n `8`; equity avg `-0.5651` n `94`; fx avg `0.0008` n `6`; index avg `-0.1212` n `25`; metal avg `-0.2511` n `20`; unknown avg `-0.167` n `768`
- 24h: commodity avg `-0.3161` n `12`; crypto_alt avg `-1.0909` n `230`; crypto_major avg `-2.0816` n `8`; equity avg `-3.8312` n `94`; fx avg `-0.1583` n `6`; index avg `-0.5448` n `25`; metal avg `-0.8573` n `20`; unknown avg `-0.375` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
