# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T02:07:35.160161+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0138` n `12`; crypto_alt avg `-0.3116` n `234`; crypto_major avg `-0.3652` n `8`; equity avg `-0.088` n `137`; fx avg `-0.0029` n `6`; index avg `-0.0231` n `27`; metal avg `-0.102` n `20`; unknown avg `0.4986` n `917`
- 1h: commodity avg `0.1792` n `12`; crypto_alt avg `0.0145` n `234`; crypto_major avg `0.1035` n `8`; equity avg `-0.1811` n `137`; fx avg `0.0341` n `6`; index avg `-0.0546` n `27`; metal avg `-0.1033` n `20`; unknown avg `0.4577` n `917`
- 4h: commodity avg `0.0566` n `12`; crypto_alt avg `1.6408` n `234`; crypto_major avg `0.946` n `8`; equity avg `0.5523` n `137`; fx avg `0.049` n `6`; index avg `0.1158` n `27`; metal avg `0.2183` n `20`; unknown avg `1.3519` n `813`
- 24h: commodity avg `-0.4973` n `12`; crypto_alt avg `2.384` n `234`; crypto_major avg `1.5291` n `8`; equity avg `1.6139` n `137`; fx avg `-0.0048` n `6`; index avg `0.1525` n `27`; metal avg `-0.0335` n `20`; unknown avg `1.4179` n `715`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1292`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
