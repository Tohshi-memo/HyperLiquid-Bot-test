# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T23:52:31.574605+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0193` n `12`; crypto_alt avg `0.1356` n `233`; crypto_major avg `0.0849` n `8`; equity avg `0.0111` n `130`; fx avg `0.0006` n `6`; index avg `0.0025` n `26`; metal avg `-0.0043` n `20`; unknown avg `0.2815` n `835`
- 1h: commodity avg `-0.0183` n `12`; crypto_alt avg `0.2521` n `233`; crypto_major avg `0.1558` n `8`; equity avg `0.0054` n `136`; fx avg `-0.0016` n `6`; index avg `0.0008` n `26`; metal avg `-0.0076` n `20`; unknown avg `0.5329` n `836`
- 4h: commodity avg `-0.0179` n `12`; crypto_alt avg `0.2338` n `233`; crypto_major avg `0.2581` n `8`; equity avg `-0.1` n `136`; fx avg `-0.0045` n `6`; index avg `-0.0142` n `26`; metal avg `-0.0384` n `20`; unknown avg `12.6898` n `796`
- 24h: commodity avg `-0.0612` n `12`; crypto_alt avg `1.4282` n `233`; crypto_major avg `0.2526` n `8`; equity avg `-0.2877` n `136`; fx avg `-0.0063` n `6`; index avg `-0.0012` n `26`; metal avg `0.0` n `20`; unknown avg `0.64` n `724`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0587`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0527`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.05`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0477`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0422`, n `668`, weak_sample_signal
