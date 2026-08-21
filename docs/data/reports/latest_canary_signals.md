# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T21:22:30.645740+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0051` n `12`; crypto_alt avg `0.2193` n `230`; crypto_major avg `0.377` n `8`; equity avg `0.0` n `121`; fx avg `0.0133` n `6`; index avg `-0.0006` n `25`; metal avg `-0.0232` n `20`; unknown avg `-0.1223` n `793`
- 1h: commodity avg `0.0173` n `12`; crypto_alt avg `0.9358` n `230`; crypto_major avg `1.0973` n `8`; equity avg `0.0129` n `121`; fx avg `0.0116` n `6`; index avg `-0.0056` n `25`; metal avg `-0.029` n `20`; unknown avg `-0.1466` n `793`
- 4h: commodity avg `-0.0627` n `12`; crypto_alt avg `1.122` n `230`; crypto_major avg `1.3619` n `8`; equity avg `0.1283` n `121`; fx avg `0.0134` n `6`; index avg `-0.0215` n `25`; metal avg `-0.085` n `20`; unknown avg `-0.3345` n `793`
- 24h: commodity avg `0.1637` n `12`; crypto_alt avg `7.8443` n `230`; crypto_major avg `5.8066` n `8`; equity avg `0.9742` n `121`; fx avg `-0.0731` n `6`; index avg `0.0932` n `25`; metal avg `0.5074` n `20`; unknown avg `1.1967` n `777`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2163`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1868`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1857`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1799`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
