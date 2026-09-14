# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T03:22:30.230631+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.7246` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.7086` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0419` n `12`; crypto_alt avg `0.1633` n `233`; crypto_major avg `0.1899` n `8`; equity avg `-0.0601` n `136`; fx avg `-0.0144` n `6`; index avg `-0.0262` n `27`; metal avg `0.0146` n `20`; unknown avg `-0.03` n `894`
- 1h: commodity avg `0.1034` n `12`; crypto_alt avg `0.389` n `233`; crypto_major avg `0.7328` n `8`; equity avg `-0.0578` n `136`; fx avg `-0.0044` n `6`; index avg `-0.0252` n `27`; metal avg `-0.0495` n `20`; unknown avg `0.8781` n `892`
- 4h: commodity avg `0.0677` n `12`; crypto_alt avg `1.8121` n `233`; crypto_major avg `1.7559` n `8`; equity avg `0.0473` n `136`; fx avg `0.0175` n `6`; index avg `-0.0567` n `27`; metal avg `0.0313` n `20`; unknown avg `19.466` n `768`
- 24h: commodity avg `0.7628` n `12`; crypto_alt avg `-0.3305` n `233`; crypto_major avg `-0.0242` n `8`; equity avg `-1.3859` n `136`; fx avg `0.062` n `6`; index avg `-0.3049` n `26`; metal avg `-0.0995` n `20`; unknown avg `1.9172` n `682`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `-0.1345`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
