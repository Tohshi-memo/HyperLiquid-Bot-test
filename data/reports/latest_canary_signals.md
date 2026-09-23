# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T00:22:40.280320+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0396` n `12`; crypto_alt avg `0.3796` n `234`; crypto_major avg `0.5706` n `8`; equity avg `0.0731` n `140`; fx avg `-0.03` n `6`; index avg `-0.0078` n `26`; metal avg `-0.007` n `20`; unknown avg `-0.0651` n `945`
- 1h: commodity avg `0.0874` n `12`; crypto_alt avg `-0.041` n `234`; crypto_major avg `0.164` n `8`; equity avg `-0.0126` n `140`; fx avg `-0.0666` n `6`; index avg `-0.024` n `26`; metal avg `-0.0233` n `20`; unknown avg `0.084` n `937`
- 4h: commodity avg `0.0878` n `12`; crypto_alt avg `1.802` n `234`; crypto_major avg `0.7838` n `8`; equity avg `0.1977` n `140`; fx avg `-0.057` n `6`; index avg `-0.0067` n `26`; metal avg `0.0305` n `20`; unknown avg `-0.0684` n `936`
- 24h: commodity avg `0.1512` n `12`; crypto_alt avg `3.1188` n `234`; crypto_major avg `0.7638` n `8`; equity avg `0.4921` n `140`; fx avg `-0.2558` n `6`; index avg `0.0339` n `26`; metal avg `0.1873` n `20`; unknown avg `1.2631` n `836`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
