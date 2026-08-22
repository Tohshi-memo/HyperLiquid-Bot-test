# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T13:37:24.979326+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0067` n `12`; crypto_alt avg `-0.102` n `230`; crypto_major avg `-0.1427` n `8`; equity avg `-0.0032` n `121`; fx avg `-0.0035` n `6`; index avg `-0.0007` n `25`; metal avg `0.0071` n `20`; unknown avg `-0.0386` n `794`
- 1h: commodity avg `-0.048` n `12`; crypto_alt avg `-0.5223` n `230`; crypto_major avg `-0.4611` n `8`; equity avg `-0.0151` n `121`; fx avg `-0.0042` n `6`; index avg `-0.0108` n `25`; metal avg `0.0147` n `20`; unknown avg `-0.0553` n `794`
- 4h: commodity avg `-0.0648` n `12`; crypto_alt avg `-0.8272` n `230`; crypto_major avg `-0.5421` n `8`; equity avg `-0.0761` n `121`; fx avg `0.0107` n `6`; index avg `0.0014` n `25`; metal avg `0.0322` n `20`; unknown avg `0.0074` n `794`
- 24h: commodity avg `-0.1169` n `12`; crypto_alt avg `1.3921` n `230`; crypto_major avg `3.3039` n `8`; equity avg `-0.5891` n `121`; fx avg `0.073` n `6`; index avg `-0.0075` n `25`; metal avg `-0.1049` n `20`; unknown avg `0.7804` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1647`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.152`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1382`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
