# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T23:07:30.479519+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.15` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0093` n `12`; crypto_alt avg `0.0444` n `229`; crypto_major avg `0.0764` n `8`; equity avg `-0.0691` n `91`; fx avg `-0.0078` n `6`; index avg `0.0012` n `25`; metal avg `0.0462` n `20`; unknown avg `-0.0384` n `763`
- 1h: commodity avg `0.0172` n `12`; crypto_alt avg `0.3542` n `229`; crypto_major avg `0.3753` n `8`; equity avg `-0.0013` n `91`; fx avg `0.0043` n `6`; index avg `-0.0189` n `25`; metal avg `0.0262` n `20`; unknown avg `0.058` n `763`
- 4h: commodity avg `0.1811` n `12`; crypto_alt avg `-0.3132` n `229`; crypto_major avg `-0.0707` n `8`; equity avg `-0.1374` n `91`; fx avg `-0.0089` n `6`; index avg `-0.016` n `25`; metal avg `-0.0636` n `20`; unknown avg `0.0176` n `761`
- 24h: commodity avg `0.9594` n `12`; crypto_alt avg `-2.7461` n `229`; crypto_major avg `-1.7515` n `8`; equity avg `-3.4243` n `91`; fx avg `-0.2819` n `6`; index avg `-0.6073` n `25`; metal avg `-0.632` n `20`; unknown avg `-0.0914` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
