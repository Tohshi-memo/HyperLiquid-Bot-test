# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T11:37:26.641128+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0176` n `12`; crypto_alt avg `0.428` n `233`; crypto_major avg `0.1841` n `8`; equity avg `-0.0014` n `134`; fx avg `0.0026` n `6`; index avg `0.0042` n `26`; metal avg `-0.0226` n `20`; unknown avg `2.56` n `798`
- 1h: commodity avg `0.0677` n `12`; crypto_alt avg `0.1232` n `233`; crypto_major avg `-0.1199` n `8`; equity avg `-0.1378` n `134`; fx avg `0.013` n `6`; index avg `-0.0291` n `26`; metal avg `-0.0217` n `20`; unknown avg `15.5878` n `796`
- 4h: commodity avg `0.2231` n `12`; crypto_alt avg `-0.4452` n `233`; crypto_major avg `-0.6556` n `8`; equity avg `-0.7354` n `134`; fx avg `0.0259` n `6`; index avg `-0.1935` n `26`; metal avg `-0.1474` n `20`; unknown avg `2.0351` n `790`
- 24h: commodity avg `-0.0333` n `12`; crypto_alt avg `-0.0084` n `232`; crypto_major avg `0.9301` n `8`; equity avg `0.2279` n `134`; fx avg `-0.0892` n `6`; index avg `-0.1522` n `26`; metal avg `-0.117` n `20`; unknown avg `1.6393` n `689`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
