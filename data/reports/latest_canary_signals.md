# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T22:07:27.815788+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0636` n `13`; crypto_alt avg `-0.2723` n `239`; crypto_major avg `-0.15` n `8`; equity avg `0.0634` n `160`; fx avg `0.0123` n `6`; index avg `0.0006` n `27`; metal avg `-0.0117` n `20`; unknown avg `20.4365` n `1249`
- 1h: commodity avg `-0.0732` n `13`; crypto_alt avg `-0.2124` n `239`; crypto_major avg `-0.0512` n `8`; equity avg `0.4576` n `160`; fx avg `0.0123` n `6`; index avg `0.0166` n `27`; metal avg `0.0348` n `20`; unknown avg `1.2035` n `1241`
- 4h: commodity avg `-0.2919` n `13`; crypto_alt avg `-0.5149` n `239`; crypto_major avg `-0.0479` n `8`; equity avg `0.5808` n `160`; fx avg `0.0069` n `6`; index avg `0.1032` n `27`; metal avg `0.3038` n `20`; unknown avg `1.6067` n `1205`
- 24h: commodity avg `-0.4902` n `13`; crypto_alt avg `2.6892` n `239`; crypto_major avg `0.3323` n `8`; equity avg `5.3622` n `160`; fx avg `-0.0862` n `6`; index avg `0.6681` n `27`; metal avg `0.7864` n `20`; unknown avg `8.0816` n `1064`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1669`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1479`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1372`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1337`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1331`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
