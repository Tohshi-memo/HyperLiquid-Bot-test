# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T16:22:31.778543+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0018` n `12`; crypto_alt avg `-0.0291` n `229`; crypto_major avg `-0.1917` n `8`; equity avg `-0.0314` n `88`; fx avg `-0.0207` n `6`; index avg `-0.0027` n `25`; metal avg `-0.005` n `20`; unknown avg `-0.0501` n `763`
- 1h: commodity avg `0.0117` n `12`; crypto_alt avg `-0.0887` n `229`; crypto_major avg `-0.0666` n `8`; equity avg `-0.037` n `88`; fx avg `-0.0077` n `6`; index avg `-0.0092` n `25`; metal avg `-0.0158` n `20`; unknown avg `0.0354` n `695`
- 4h: commodity avg `-0.0026` n `12`; crypto_alt avg `0.3519` n `229`; crypto_major avg `0.5224` n `8`; equity avg `-0.0339` n `88`; fx avg `-0.1009` n `6`; index avg `0.0208` n `25`; metal avg `-0.0053` n `20`; unknown avg `0.0942` n `695`
- 24h: commodity avg `-0.0308` n `12`; crypto_alt avg `-1.831` n `229`; crypto_major avg `-0.9708` n `8`; equity avg `0.2115` n `88`; fx avg `-0.1075` n `6`; index avg `0.072` n `25`; metal avg `0.0518` n `20`; unknown avg `-0.158` n `663`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
