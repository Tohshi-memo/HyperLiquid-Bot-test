# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T04:47:49.885084+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.01` n `12`; crypto_alt avg `-0.0707` n `230`; crypto_major avg `-0.0752` n `8`; equity avg `-0.1176` n `114`; fx avg `0.0012` n `6`; index avg `-0.0221` n `25`; metal avg `0.0118` n `20`; unknown avg `0.0622` n `793`
- 1h: commodity avg `-0.0248` n `12`; crypto_alt avg `0.138` n `230`; crypto_major avg `0.0637` n `8`; equity avg `-0.0202` n `114`; fx avg `0.0206` n `6`; index avg `0.0004` n `25`; metal avg `0.0066` n `20`; unknown avg `0.1505` n `793`
- 4h: commodity avg `0.0667` n `12`; crypto_alt avg `-1.0021` n `230`; crypto_major avg `-0.4677` n `8`; equity avg `-1.6297` n `114`; fx avg `0.0124` n `6`; index avg `-0.3053` n `25`; metal avg `-0.3076` n `20`; unknown avg `0.2622` n `793`
- 24h: commodity avg `0.6428` n `12`; crypto_alt avg `-1.4603` n `230`; crypto_major avg `0.0111` n `8`; equity avg `-1.0542` n `114`; fx avg `0.0119` n `6`; index avg `-0.2941` n `25`; metal avg `-0.1891` n `20`; unknown avg `0.0799` n `776`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.2044`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1943`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1582`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
