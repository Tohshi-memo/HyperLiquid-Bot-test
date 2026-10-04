# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T21:07:24.983714+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0114` n `13`; crypto_alt avg `-0.0154` n `235`; crypto_major avg `0.0546` n `8`; equity avg `0.0212` n `144`; fx avg `-0.0099` n `6`; index avg `0.0075` n `26`; metal avg `-0.0011` n `20`; unknown avg `-0.112` n `1072`
- 1h: commodity avg `-0.0034` n `13`; crypto_alt avg `-0.0607` n `235`; crypto_major avg `0.3375` n `8`; equity avg `0.0651` n `144`; fx avg `-0.0023` n `6`; index avg `0.0143` n `26`; metal avg `0.0111` n `20`; unknown avg `5.7881` n `1072`
- 4h: commodity avg `0.0443` n `13`; crypto_alt avg `0.1822` n `235`; crypto_major avg `0.3528` n `8`; equity avg `0.0816` n `144`; fx avg `-0.0016` n `6`; index avg `0.0204` n `26`; metal avg `0.0185` n `20`; unknown avg `3.3573` n `1060`
- 24h: commodity avg `-0.0923` n `13`; crypto_alt avg `0.8669` n `235`; crypto_major avg `1.3496` n `8`; equity avg `0.2618` n `144`; fx avg `0.0072` n `6`; index avg `0.0025` n `26`; metal avg `0.0109` n `20`; unknown avg `1.5101` n `1020`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2134`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1907`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1797`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1511`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.145`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
