# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T15:22:27.124719+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.38` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `-2.0291` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0139` n `12`; crypto_alt avg `-0.0245` n `230`; crypto_major avg `0.0462` n `8`; equity avg `0.1244` n `113`; fx avg `0.0016` n `6`; index avg `0.0058` n `25`; metal avg `0.0332` n `20`; unknown avg `-0.0113` n `786`
- 1h: commodity avg `0.0645` n `12`; crypto_alt avg `-0.0308` n `230`; crypto_major avg `0.0416` n `8`; equity avg `0.2279` n `113`; fx avg `-0.005` n `6`; index avg `-0.0021` n `25`; metal avg `-0.0658` n `20`; unknown avg `-0.0232` n `786`
- 4h: commodity avg `0.0231` n `12`; crypto_alt avg `-0.4659` n `230`; crypto_major avg `-0.7406` n `8`; equity avg `1.2885` n `113`; fx avg `0.007` n `6`; index avg `0.1299` n `25`; metal avg `-0.0758` n `20`; unknown avg `0.062` n `786`
- 24h: commodity avg `0.2103` n `12`; crypto_alt avg `-0.6171` n `230`; crypto_major avg `0.6634` n `8`; equity avg `3.0533` n `113`; fx avg `0.0356` n `6`; index avg `0.3134` n `25`; metal avg `0.2903` n `20`; unknown avg `-0.0688` n `769`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2283`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2105`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1974`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1961`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1575`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1552`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1494`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1409`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1262`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
