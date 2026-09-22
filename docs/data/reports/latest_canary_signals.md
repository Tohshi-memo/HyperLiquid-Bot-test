# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T22:52:28.257846+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0099` n `12`; crypto_alt avg `0.2763` n `234`; crypto_major avg `0.1391` n `8`; equity avg `-0.0393` n `140`; fx avg `0.0011` n `6`; index avg `-0.0064` n `26`; metal avg `-0.0051` n `20`; unknown avg `-0.0607` n `945`
- 1h: commodity avg `-0.0263` n `12`; crypto_alt avg `0.6205` n `234`; crypto_major avg `0.124` n `8`; equity avg `0.0902` n `140`; fx avg `0.0182` n `6`; index avg `0.01` n `26`; metal avg `0.0323` n `20`; unknown avg `0.5629` n `942`
- 4h: commodity avg `-0.0673` n `12`; crypto_alt avg `1.3053` n `234`; crypto_major avg `0.1561` n `8`; equity avg `0.2287` n `140`; fx avg `-0.022` n `6`; index avg `0.0205` n `26`; metal avg `0.0516` n `20`; unknown avg `0.254` n `906`
- 24h: commodity avg `0.1492` n `12`; crypto_alt avg `2.9654` n `234`; crypto_major avg `0.501` n `8`; equity avg `0.8504` n `140`; fx avg `-0.2791` n `6`; index avg `0.0984` n `26`; metal avg `0.2153` n `20`; unknown avg `1.6277` n `836`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1249`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
