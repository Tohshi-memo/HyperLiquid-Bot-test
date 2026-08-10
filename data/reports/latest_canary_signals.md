# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T22:37:26.237456+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0052` n `12`; crypto_alt avg `-0.0826` n `230`; crypto_major avg `-0.0931` n `8`; equity avg `-0.0294` n `113`; fx avg `0.0006` n `6`; index avg `-0.007` n `25`; metal avg `-0.0012` n `20`; unknown avg `1.2107` n `785`
- 1h: commodity avg `-0.0488` n `12`; crypto_alt avg `-0.1629` n `230`; crypto_major avg `-0.3466` n `8`; equity avg `-0.0713` n `113`; fx avg `0.0075` n `6`; index avg `-0.0212` n `25`; metal avg `-0.0193` n `20`; unknown avg `1.0992` n `785`
- 4h: commodity avg `-0.0711` n `12`; crypto_alt avg `-0.3082` n `230`; crypto_major avg `0.0611` n `8`; equity avg `-0.3745` n `113`; fx avg `0.0107` n `6`; index avg `-0.0226` n `25`; metal avg `0.1046` n `20`; unknown avg `3.9857` n `785`
- 24h: commodity avg `0.8608` n `12`; crypto_alt avg `-1.2243` n `230`; crypto_major avg `-0.9792` n `8`; equity avg `-1.625` n `113`; fx avg `0.2639` n `6`; index avg `-0.0562` n `25`; metal avg `0.3616` n `20`; unknown avg `103.5956` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1869`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1777`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1721`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1657`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1532`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1456`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
