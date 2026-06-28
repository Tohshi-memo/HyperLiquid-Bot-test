# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T02:37:30.853893+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0173` n `12`; crypto_alt avg `0.1028` n `228`; crypto_major avg `0.0978` n `8`; equity avg `-0.019` n `88`; fx avg `-0.0095` n `6`; index avg `-0.0183` n `23`; metal avg `-0.004` n `20`; unknown avg `14.7834` n `764`
- 1h: commodity avg `0.0196` n `12`; crypto_alt avg `0.0226` n `228`; crypto_major avg `-0.1247` n `8`; equity avg `-0.01` n `88`; fx avg `-0.0085` n `6`; index avg `-0.0038` n `23`; metal avg `0.0068` n `20`; unknown avg `14.8223` n `748`
- 4h: commodity avg `0.3203` n `12`; crypto_alt avg `-0.0417` n `228`; crypto_major avg `-0.4054` n `8`; equity avg `-0.1391` n `88`; fx avg `-0.0342` n `6`; index avg `-0.0437` n `23`; metal avg `0.0336` n `20`; unknown avg `14.8086` n `748`
- 24h: commodity avg `0.5205` n `12`; crypto_alt avg `-1.024` n `228`; crypto_major avg `-1.4324` n `8`; equity avg `0.0025` n `88`; fx avg `-0.0118` n `6`; index avg `-0.1311` n `23`; metal avg `-0.0503` n `20`; unknown avg `5.8777` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.216`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1779`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
