# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T19:22:45.506602+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0884` n `12`; crypto_alt avg `-0.0539` n `229`; crypto_major avg `-0.0578` n `8`; equity avg `-0.1366` n `91`; fx avg `0.0077` n `6`; index avg `-0.0459` n `25`; metal avg `-0.0975` n `20`; unknown avg `0.0152` n `761`
- 1h: commodity avg `0.4155` n `12`; crypto_alt avg `-1.1051` n `229`; crypto_major avg `-1.1213` n `8`; equity avg `-0.9651` n `91`; fx avg `0.0122` n `6`; index avg `-0.1866` n `25`; metal avg `-0.4914` n `20`; unknown avg `0.5252` n `761`
- 4h: commodity avg `0.3742` n `12`; crypto_alt avg `-1.0612` n `229`; crypto_major avg `-0.8266` n `8`; equity avg `-0.0819` n `91`; fx avg `-0.0285` n `6`; index avg `0.0228` n `25`; metal avg `-0.3992` n `20`; unknown avg `0.065` n `753`
- 24h: commodity avg `0.8579` n `12`; crypto_alt avg `-2.1937` n `229`; crypto_major avg `-1.4122` n `8`; equity avg `-3.6384` n `91`; fx avg `-0.2385` n `6`; index avg `-0.7004` n `25`; metal avg `-0.6846` n `20`; unknown avg `-0.3373` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0657`, n `668`, weak_sample_signal
