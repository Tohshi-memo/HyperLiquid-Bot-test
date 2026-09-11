# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T02:07:25.179279+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0393` n `12`; crypto_alt avg `-0.061` n `233`; crypto_major avg `-0.0403` n `8`; equity avg `-0.0198` n `136`; fx avg `-0.0071` n `6`; index avg `0.0194` n `26`; metal avg `-0.013` n `20`; unknown avg `-0.0667` n `794`
- 1h: commodity avg `0.0936` n `12`; crypto_alt avg `-0.3699` n `233`; crypto_major avg `-0.1967` n `8`; equity avg `-0.1875` n `136`; fx avg `0.0112` n `6`; index avg `-0.0323` n `26`; metal avg `-0.0906` n `20`; unknown avg `-0.3142` n `794`
- 4h: commodity avg `-0.2082` n `12`; crypto_alt avg `-0.688` n `233`; crypto_major avg `-0.5807` n `8`; equity avg `-0.0457` n `136`; fx avg `-0.0329` n `6`; index avg `0.0275` n `26`; metal avg `-0.0116` n `20`; unknown avg `1494.1649` n `754`
- 24h: commodity avg `1.1395` n `12`; crypto_alt avg `-1.6356` n `233`; crypto_major avg `-1.9767` n `8`; equity avg `-1.625` n `136`; fx avg `0.1293` n `6`; index avg `-0.2825` n `26`; metal avg `-1.3175` n `20`; unknown avg `-1.1948` n `683`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.136`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
