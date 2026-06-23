# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T23:22:38.332448+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0092` n `12`; crypto_alt avg `0.103` n `228`; crypto_major avg `0.074` n `8`; equity avg `0.228` n `86`; fx avg `-0.0008` n `6`; index avg `0.0819` n `23`; metal avg `0.027` n `20`; unknown avg `0.0728` n `764`
- 1h: commodity avg `-0.0425` n `12`; crypto_alt avg `-0.4167` n `228`; crypto_major avg `-0.1136` n `8`; equity avg `-0.2822` n `86`; fx avg `-0.0035` n `6`; index avg `-0.0408` n `23`; metal avg `-0.0663` n `20`; unknown avg `0.1081` n `756`
- 4h: commodity avg `-0.0889` n `12`; crypto_alt avg `0.3647` n `228`; crypto_major avg `0.4843` n `8`; equity avg `0.0224` n `86`; fx avg `-0.0214` n `6`; index avg `0.0604` n `23`; metal avg `-0.1357` n `20`; unknown avg `0.3444` n `756`
- 24h: commodity avg `-0.4682` n `12`; crypto_alt avg `-2.0373` n `228`; crypto_major avg `-2.973` n `8`; equity avg `-3.2049` n `86`; fx avg `-0.1979` n `6`; index avg `-0.8716` n `23`; metal avg `-1.3133` n `20`; unknown avg `0.6805` n `588`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.127`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
