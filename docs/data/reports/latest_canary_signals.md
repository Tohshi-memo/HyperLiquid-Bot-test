# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T19:52:29.082890+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0015` n `12`; crypto_alt avg `0.0189` n `233`; crypto_major avg `0.0085` n `8`; equity avg `-0.0053` n `136`; fx avg `-0.0001` n `6`; index avg `0.0028` n `26`; metal avg `0.0088` n `20`; unknown avg `0.7551` n `838`
- 1h: commodity avg `0.0044` n `12`; crypto_alt avg `-0.2989` n `233`; crypto_major avg `-0.2375` n `8`; equity avg `-0.1851` n `136`; fx avg `0.0` n `6`; index avg `-0.0168` n `26`; metal avg `0.0021` n `20`; unknown avg `13.3673` n `836`
- 4h: commodity avg `0.0824` n `12`; crypto_alt avg `-0.5132` n `233`; crypto_major avg `-0.5786` n `8`; equity avg `-0.2153` n `136`; fx avg `-0.0024` n `6`; index avg `-0.0283` n `26`; metal avg `0.01` n `20`; unknown avg `0.0995` n `782`
- 24h: commodity avg `-0.2042` n `12`; crypto_alt avg `0.9057` n `233`; crypto_major avg `-0.327` n `8`; equity avg `-0.1824` n `136`; fx avg `-0.0396` n `6`; index avg `0.0021` n `26`; metal avg `0.0413` n `20`; unknown avg `3.416` n `710`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.062`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0572`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0561`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0548`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.048`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0434`, n `668`, weak_sample_signal
