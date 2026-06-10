# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T05:37:24.871137+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1394` n `12`; crypto_alt avg `0.1073` n `228`; crypto_major avg `0.1015` n `8`; equity avg `0.1372` n `74`; fx avg `0.0048` n `6`; index avg `0.1041` n `23`; metal avg `0.2355` n `18`; unknown avg `-0.0076` n `547`
- 1h: commodity avg `-0.4479` n `12`; crypto_alt avg `-0.0818` n `228`; crypto_major avg `-0.1444` n `8`; equity avg `0.1647` n `74`; fx avg `0.0231` n `6`; index avg `-0.0197` n `23`; metal avg `0.2979` n `18`; unknown avg `-0.3899` n `547`
- 4h: commodity avg `-0.5058` n `12`; crypto_alt avg `-1.1307` n `228`; crypto_major avg `-1.2162` n `8`; equity avg `-1.1756` n `74`; fx avg `0.0746` n `6`; index avg `-0.6404` n `23`; metal avg `-0.6916` n `18`; unknown avg `-0.743` n `547`
- 24h: commodity avg `-0.9055` n `12`; crypto_alt avg `-2.3526` n `228`; crypto_major avg `-4.5002` n `8`; equity avg `-4.0787` n `74`; fx avg `0.2087` n `6`; index avg `-1.9953` n `23`; metal avg `-3.2183` n `18`; unknown avg `0.415` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0584`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.055`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0479`, n `668`, weak_sample_signal
