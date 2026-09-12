# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T22:52:28.027951+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0105` n `12`; crypto_alt avg `0.0381` n `233`; crypto_major avg `0.0533` n `8`; equity avg `0.0178` n `136`; fx avg `-0.0024` n `6`; index avg `-0.0007` n `26`; metal avg `-0.0026` n `20`; unknown avg `0.0229` n `838`
- 1h: commodity avg `0.008` n `12`; crypto_alt avg `-0.0214` n `233`; crypto_major avg `0.0147` n `8`; equity avg `-0.0281` n `136`; fx avg `0.0004` n `6`; index avg `-0.0081` n `26`; metal avg `0.0019` n `20`; unknown avg `-0.1043` n `810`
- 4h: commodity avg `0.0047` n `12`; crypto_alt avg `-0.3168` n `233`; crypto_major avg `-0.1357` n `8`; equity avg `-0.29` n `136`; fx avg `-0.0029` n `6`; index avg `-0.0318` n `26`; metal avg `-0.0287` n `20`; unknown avg `0.2176` n `796`
- 24h: commodity avg `-0.0917` n `12`; crypto_alt avg `1.6933` n `233`; crypto_major avg `0.5095` n `8`; equity avg `-0.2544` n `136`; fx avg `-0.0185` n `6`; index avg `-0.0053` n `26`; metal avg `0.0048` n `20`; unknown avg `0.5356` n `720`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0544`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0497`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0477`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0455`, n `668`, weak_sample_signal
