# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T13:22:29.565116+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0432` n `12`; crypto_alt avg `0.1682` n `231`; crypto_major avg `0.0741` n `8`; equity avg `-0.0489` n `127`; fx avg `0.0377` n `6`; index avg `-0.0024` n `26`; metal avg `0.0169` n `20`; unknown avg `-0.0323` n `792`
- 1h: commodity avg `0.0714` n `12`; crypto_alt avg `0.1997` n `231`; crypto_major avg `-0.0263` n `8`; equity avg `-0.138` n `127`; fx avg `0.0656` n `6`; index avg `-0.0224` n `26`; metal avg `-0.0558` n `20`; unknown avg `-0.1409` n `792`
- 4h: commodity avg `0.1726` n `12`; crypto_alt avg `-0.6621` n `231`; crypto_major avg `-0.8443` n `8`; equity avg `-0.3839` n `127`; fx avg `0.0589` n `6`; index avg `-0.0143` n `26`; metal avg `-0.0562` n `20`; unknown avg `0.1172` n `792`
- 24h: commodity avg `0.5047` n `12`; crypto_alt avg `2.0913` n `231`; crypto_major avg `2.6489` n `8`; equity avg `2.2061` n `127`; fx avg `-0.0303` n `6`; index avg `0.3238` n `26`; metal avg `-0.2949` n `20`; unknown avg `0.497` n `775`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
