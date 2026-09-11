# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T11:52:26.656891+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0687` n `12`; crypto_alt avg `0.3338` n `233`; crypto_major avg `0.2441` n `8`; equity avg `0.0797` n `136`; fx avg `-0.0096` n `6`; index avg `0.0207` n `26`; metal avg `0.0074` n `20`; unknown avg `0.1943` n `796`
- 1h: commodity avg `0.0479` n `12`; crypto_alt avg `-0.0191` n `233`; crypto_major avg `-0.0976` n `8`; equity avg `-0.0349` n `136`; fx avg `-0.0177` n `6`; index avg `0.0132` n `26`; metal avg `-0.0548` n `20`; unknown avg `-0.094` n `794`
- 4h: commodity avg `-0.3612` n `12`; crypto_alt avg `-0.8707` n `233`; crypto_major avg `-0.4595` n `8`; equity avg `0.1367` n `136`; fx avg `-0.1034` n `6`; index avg `0.0824` n `26`; metal avg `-0.0338` n `20`; unknown avg `-0.1565` n `788`
- 24h: commodity avg `0.1573` n `12`; crypto_alt avg `-1.8493` n `233`; crypto_major avg `-1.6634` n `8`; equity avg `-0.6726` n `136`; fx avg `-0.0927` n `6`; index avg `-0.0297` n `26`; metal avg `-0.4111` n `20`; unknown avg `1.1697` n `683`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
