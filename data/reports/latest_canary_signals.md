# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T06:52:28.224638+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0026` n `12`; crypto_alt avg `0.0166` n `228`; crypto_major avg `0.1503` n `8`; equity avg `0.0812` n `88`; fx avg `-0.0038` n `6`; index avg `0.006` n `23`; metal avg `0.059` n `20`; unknown avg `-0.0347` n `765`
- 1h: commodity avg `-0.075` n `12`; crypto_alt avg `-0.7367` n `228`; crypto_major avg `-0.794` n `8`; equity avg `-0.1413` n `88`; fx avg `0.0553` n `6`; index avg `-0.0298` n `23`; metal avg `-0.0959` n `20`; unknown avg `5.8586` n `745`
- 4h: commodity avg `-0.1257` n `12`; crypto_alt avg `-0.0445` n `228`; crypto_major avg `-0.4599` n `8`; equity avg `0.0282` n `88`; fx avg `-0.009` n `6`; index avg `-0.01` n `23`; metal avg `-0.1301` n `20`; unknown avg `0.0723` n `745`
- 24h: commodity avg `-0.0932` n `12`; crypto_alt avg `-1.0709` n `228`; crypto_major avg `-0.8282` n `8`; equity avg `0.4406` n `88`; fx avg `0.1214` n `6`; index avg `-0.0218` n `23`; metal avg `-0.8845` n `20`; unknown avg `-0.1956` n `745`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
