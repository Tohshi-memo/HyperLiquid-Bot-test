# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T02:22:25.980917+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0168` n `12`; crypto_alt avg `0.6575` n `231`; crypto_major avg `0.7408` n `8`; equity avg `0.0985` n `122`; fx avg `-0.0224` n `6`; index avg `0.051` n `25`; metal avg `0.0903` n `20`; unknown avg `-0.002` n `793`
- 1h: commodity avg `0.0905` n `12`; crypto_alt avg `-0.4148` n `231`; crypto_major avg `0.0464` n `8`; equity avg `-0.7955` n `122`; fx avg `-0.0518` n `6`; index avg `-0.0744` n `25`; metal avg `0.1671` n `20`; unknown avg `0.3719` n `793`
- 4h: commodity avg `-0.2116` n `12`; crypto_alt avg `-1.837` n `231`; crypto_major avg `-0.8558` n `8`; equity avg `-0.97` n `122`; fx avg `-0.0926` n `6`; index avg `-0.0547` n `25`; metal avg `0.1061` n `20`; unknown avg `0.6776` n `793`
- 24h: commodity avg `-0.3865` n `12`; crypto_alt avg `2.6662` n `231`; crypto_major avg `0.7825` n `8`; equity avg `-0.5504` n `122`; fx avg `-0.2175` n `6`; index avg `-0.0057` n `25`; metal avg `0.1993` n `20`; unknown avg `6.1945` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
