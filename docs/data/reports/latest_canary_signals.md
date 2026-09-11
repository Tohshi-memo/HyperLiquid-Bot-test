# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T18:22:39.991092+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.29` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.9991` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.7723` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.6593` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.1082` n `12`; crypto_alt avg `0.1575` n `233`; crypto_major avg `0.1172` n `8`; equity avg `-0.095` n `136`; fx avg `-0.0038` n `6`; index avg `-0.0275` n `26`; metal avg `-0.0506` n `20`; unknown avg `0.0073` n `806`
- 1h: commodity avg `0.128` n `12`; crypto_alt avg `-0.6804` n `233`; crypto_major avg `-0.7549` n `8`; equity avg `-0.1766` n `136`; fx avg `-0.0017` n `6`; index avg `-0.0236` n `26`; metal avg `-0.1015` n `20`; unknown avg `8.7905` n `772`
- 4h: commodity avg `-0.0277` n `12`; crypto_alt avg `-1.7245` n `233`; crypto_major avg `-2.0168` n `8`; equity avg `-0.3575` n `136`; fx avg `0.0053` n `6`; index avg `-0.0177` n `26`; metal avg `-0.2445` n `20`; unknown avg `2.6342` n `752`
- 24h: commodity avg `-0.495` n `12`; crypto_alt avg `0.549` n `233`; crypto_major avg `1.2549` n `8`; equity avg `0.5646` n `136`; fx avg `-0.1492` n `6`; index avg `0.3277` n `26`; metal avg `0.1354` n `20`; unknown avg `5.1063` n `666`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0604`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
