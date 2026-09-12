# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T15:22:25.169207+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0057` n `12`; crypto_alt avg `0.0204` n `233`; crypto_major avg `-0.0612` n `8`; equity avg `-0.0051` n `136`; fx avg `0.0023` n `6`; index avg `0.0008` n `26`; metal avg `0.0039` n `20`; unknown avg `0.2148` n `838`
- 1h: commodity avg `-0.0139` n `12`; crypto_alt avg `0.1684` n `233`; crypto_major avg `-0.0293` n `8`; equity avg `-0.0054` n `136`; fx avg `0.0052` n `6`; index avg `0.0067` n `26`; metal avg `0.0018` n `20`; unknown avg `5.3711` n `836`
- 4h: commodity avg `-0.0279` n `12`; crypto_alt avg `0.3515` n `233`; crypto_major avg `0.1683` n `8`; equity avg `0.0138` n `136`; fx avg `0.0064` n `6`; index avg `0.0078` n `26`; metal avg `0.0395` n `20`; unknown avg `1.785` n `824`
- 24h: commodity avg `-0.1863` n `12`; crypto_alt avg `-0.5398` n `233`; crypto_major avg `-1.4405` n `8`; equity avg `-0.3576` n `136`; fx avg `-0.0074` n `6`; index avg `-0.0106` n `26`; metal avg `-0.0817` n `20`; unknown avg `11.1525` n `694`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.06`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0553`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0539`, n `668`, weak_sample_signal
