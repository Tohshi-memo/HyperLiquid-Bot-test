# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T23:22:33.339842+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0677` n `12`; crypto_alt avg `-0.0822` n `230`; crypto_major avg `-0.0608` n `8`; equity avg `-0.0032` n `102`; fx avg `-0.0266` n `6`; index avg `0.0039` n `25`; metal avg `-0.0031` n `20`; unknown avg `-0.0432` n `782`
- 1h: commodity avg `0.0684` n `12`; crypto_alt avg `-0.0783` n `230`; crypto_major avg `0.004` n `8`; equity avg `-0.0313` n `102`; fx avg `-0.0466` n `6`; index avg `0.0145` n `25`; metal avg `-0.0072` n `20`; unknown avg `1.8662` n `782`
- 4h: commodity avg `-0.0835` n `12`; crypto_alt avg `0.3427` n `230`; crypto_major avg `0.4806` n `8`; equity avg `0.2357` n `102`; fx avg `-0.0175` n `6`; index avg `0.0085` n `25`; metal avg `0.0277` n `20`; unknown avg `0.2146` n `782`
- 24h: commodity avg `-0.1419` n `12`; crypto_alt avg `-0.4824` n `230`; crypto_major avg `-0.8475` n `8`; equity avg `-0.0995` n `102`; fx avg `-0.0739` n `6`; index avg `-0.0001` n `25`; metal avg `0.0354` n `20`; unknown avg `-0.0132` n `765`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
