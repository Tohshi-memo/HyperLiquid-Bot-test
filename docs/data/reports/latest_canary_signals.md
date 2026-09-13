# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T02:22:26.278653+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0169` n `12`; crypto_alt avg `-0.1123` n `233`; crypto_major avg `-0.0212` n `8`; equity avg `-0.0123` n `136`; fx avg `0.0056` n `6`; index avg `-0.0042` n `26`; metal avg `0.0007` n `20`; unknown avg `0.0151` n `814`
- 1h: commodity avg `-0.0242` n `12`; crypto_alt avg `-0.107` n `233`; crypto_major avg `-0.0889` n `8`; equity avg `-0.0807` n `136`; fx avg `0.0033` n `6`; index avg `-0.0111` n `26`; metal avg `-0.0039` n `20`; unknown avg `-0.0257` n `812`
- 4h: commodity avg `-0.0554` n `12`; crypto_alt avg `0.3269` n `233`; crypto_major avg `-0.0447` n `8`; equity avg `-0.0858` n `136`; fx avg `0.0019` n `6`; index avg `-0.0215` n `26`; metal avg `-0.0017` n `20`; unknown avg `3.5892` n `806`
- 24h: commodity avg `-0.0423` n `12`; crypto_alt avg `0.8369` n `233`; crypto_major avg `0.1423` n `8`; equity avg `-0.4588` n `136`; fx avg `-0.0147` n `6`; index avg `-0.0368` n `26`; metal avg `0.0305` n `20`; unknown avg `0.1034` n `706`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0578`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0515`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.047`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0455`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0452`, n `668`, weak_sample_signal
