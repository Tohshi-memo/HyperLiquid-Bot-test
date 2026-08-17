# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T10:22:38.257156+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0211` n `12`; crypto_alt avg `-0.1104` n `230`; crypto_major avg `-0.0385` n `8`; equity avg `0.0123` n `114`; fx avg `-0.0049` n `6`; index avg `0.0112` n `25`; metal avg `0.026` n `20`; unknown avg `-0.0008` n `792`
- 1h: commodity avg `0.0904` n `12`; crypto_alt avg `-0.1278` n `230`; crypto_major avg `-0.0315` n `8`; equity avg `0.0173` n `114`; fx avg `0.0242` n `6`; index avg `0.0046` n `25`; metal avg `0.012` n `20`; unknown avg `-0.0453` n `792`
- 4h: commodity avg `0.2082` n `12`; crypto_alt avg `-0.3939` n `230`; crypto_major avg `-0.2453` n `8`; equity avg `0.179` n `114`; fx avg `0.0117` n `6`; index avg `0.0088` n `25`; metal avg `-0.0395` n `20`; unknown avg `-0.0319` n `792`
- 24h: commodity avg `-0.0329` n `12`; crypto_alt avg `-0.3174` n `230`; crypto_major avg `0.5688` n `8`; equity avg `1.1838` n `114`; fx avg `-0.0171` n `6`; index avg `0.1412` n `25`; metal avg `0.1641` n `20`; unknown avg `-0.0649` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1662`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1518`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1417`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1369`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
