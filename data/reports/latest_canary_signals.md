# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T21:07:27.914499+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0023` n `12`; crypto_alt avg `-0.128` n `230`; crypto_major avg `-0.0099` n `8`; equity avg `0.0162` n `114`; fx avg `-0.001` n `6`; index avg `0.0001` n `25`; metal avg `0.006` n `20`; unknown avg `0.0216` n `791`
- 1h: commodity avg `0.0241` n `12`; crypto_alt avg `-0.3777` n `230`; crypto_major avg `-0.1638` n `8`; equity avg `0.0126` n `114`; fx avg `-0.0013` n `6`; index avg `-0.0069` n `25`; metal avg `-0.0247` n `20`; unknown avg `0.4092` n `791`
- 4h: commodity avg `0.0479` n `12`; crypto_alt avg `-0.5019` n `230`; crypto_major avg `-0.3946` n `8`; equity avg `0.0282` n `114`; fx avg `0.0002` n `6`; index avg `-0.0003` n `25`; metal avg `-0.0213` n `20`; unknown avg `0.2146` n `791`
- 24h: commodity avg `0.0765` n `12`; crypto_alt avg `-0.5719` n `230`; crypto_major avg `-0.1743` n `8`; equity avg `0.298` n `114`; fx avg `-0.0024` n `6`; index avg `0.0398` n `25`; metal avg `0.0321` n `20`; unknown avg `0.0893` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.219`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1883`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1686`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1626`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1582`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1579`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1458`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1404`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1321`, n `668`, weak_sample_signal
