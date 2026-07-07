# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T23:13:04.913360+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.15` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0142` n `12`; crypto_alt avg `-0.0223` n `229`; crypto_major avg `0.0228` n `8`; equity avg `-0.1704` n `91`; fx avg `-0.0009` n `6`; index avg `-0.0204` n `25`; metal avg `0.0479` n `20`; unknown avg `-0.0635` n `763`
- 1h: commodity avg `0.0123` n `12`; crypto_alt avg `0.2871` n `229`; crypto_major avg `0.3214` n `8`; equity avg `-0.1027` n `91`; fx avg `0.0112` n `6`; index avg `-0.0404` n `25`; metal avg `0.0279` n `20`; unknown avg `0.0346` n `763`
- 4h: commodity avg `0.1762` n `12`; crypto_alt avg `-0.3793` n `229`; crypto_major avg `-0.1242` n `8`; equity avg `-0.2391` n `91`; fx avg `-0.0019` n `6`; index avg `-0.0375` n `25`; metal avg `-0.0619` n `20`; unknown avg `0.0614` n `761`
- 24h: commodity avg `0.9542` n `12`; crypto_alt avg `-2.809` n `229`; crypto_major avg `-1.8039` n `8`; equity avg `-3.5187` n `91`; fx avg `-0.2751` n `6`; index avg `-0.6279` n `25`; metal avg `-0.6303` n `20`; unknown avg `-0.0398` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
