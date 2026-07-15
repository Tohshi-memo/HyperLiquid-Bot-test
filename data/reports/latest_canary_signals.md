# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T04:15:59.610599+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0199` n `12`; crypto_alt avg `-0.0405` n `230`; crypto_major avg `-0.0042` n `8`; equity avg `-0.0215` n `93`; fx avg `0.007` n `6`; index avg `-0.0171` n `25`; metal avg `-0.0009` n `20`; unknown avg `0.1311` n `767`
- 1h: commodity avg `-0.0449` n `12`; crypto_alt avg `0.1232` n `230`; crypto_major avg `0.1348` n `8`; equity avg `0.2842` n `93`; fx avg `0.0252` n `6`; index avg `0.031` n `25`; metal avg `-0.0034` n `20`; unknown avg `0.1715` n `767`
- 4h: commodity avg `-0.0645` n `12`; crypto_alt avg `0.038` n `230`; crypto_major avg `0.1439` n `8`; equity avg `0.9983` n `93`; fx avg `0.0452` n `6`; index avg `0.067` n `25`; metal avg `-0.1144` n `20`; unknown avg `-0.1536` n `767`
- 24h: commodity avg `0.1281` n `12`; crypto_alt avg `1.9048` n `230`; crypto_major avg `3.3022` n `8`; equity avg `2.8826` n `92`; fx avg `0.1582` n `6`; index avg `0.7743` n `25`; metal avg `0.3818` n `20`; unknown avg `0.3269` n `740`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0543`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0532`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0474`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0441`, n `668`, weak_sample_signal
