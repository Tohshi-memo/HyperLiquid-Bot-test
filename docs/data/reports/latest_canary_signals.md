# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T01:37:32.765419+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0346` n `12`; crypto_alt avg `-0.2432` n `234`; crypto_major avg `-0.3191` n `8`; equity avg `-0.1317` n `140`; fx avg `-0.0382` n `6`; index avg `-0.026` n `26`; metal avg `0.0089` n `20`; unknown avg `0.3609` n `945`
- 1h: commodity avg `0.0087` n `12`; crypto_alt avg `-0.085` n `234`; crypto_major avg `-0.0575` n `8`; equity avg `-0.1941` n `140`; fx avg `-0.0253` n `6`; index avg `-0.0472` n `26`; metal avg `-0.1346` n `20`; unknown avg `-0.0188` n `943`
- 4h: commodity avg `0.0614` n `12`; crypto_alt avg `0.845` n `234`; crypto_major avg `0.3982` n `8`; equity avg `-0.0914` n `140`; fx avg `-0.0853` n `6`; index avg `-0.0691` n `26`; metal avg `-0.1135` n `20`; unknown avg `0.6459` n `936`
- 24h: commodity avg `0.0997` n `12`; crypto_alt avg `2.7828` n `234`; crypto_major avg `1.3445` n `8`; equity avg `0.5308` n `140`; fx avg `-0.2433` n `6`; index avg `0.0036` n `26`; metal avg `0.1049` n `20`; unknown avg `0.827` n `836`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1306`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
