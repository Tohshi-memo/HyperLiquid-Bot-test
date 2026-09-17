# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T14:37:31.660844+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0286` n `12`; crypto_alt avg `-0.0712` n `234`; crypto_major avg `0.1071` n `8`; equity avg `0.1065` n `138`; fx avg `-0.0081` n `6`; index avg `0.0126` n `26`; metal avg `-0.0141` n `20`; unknown avg `0.128` n `917`
- 1h: commodity avg `0.1302` n `12`; crypto_alt avg `1.0682` n `234`; crypto_major avg `1.1685` n `8`; equity avg `0.1105` n `138`; fx avg `-0.039` n `6`; index avg `0.0256` n `26`; metal avg `0.0519` n `20`; unknown avg `1.9053` n `895`
- 4h: commodity avg `0.0284` n `12`; crypto_alt avg `1.0807` n `234`; crypto_major avg `1.4475` n `8`; equity avg `0.5669` n `138`; fx avg `-0.0939` n `6`; index avg `0.1692` n `26`; metal avg `0.3953` n `20`; unknown avg `1.5868` n `891`
- 24h: commodity avg `-0.4142` n `12`; crypto_alt avg `4.8716` n `234`; crypto_major avg `3.1617` n `8`; equity avg `1.6783` n `138`; fx avg `0.0078` n `6`; index avg `0.2768` n `26`; metal avg `0.2837` n `20`; unknown avg `0.6641` n `711`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
