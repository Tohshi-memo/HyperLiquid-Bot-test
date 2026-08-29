# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T20:07:24.289339+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0097` n `12`; crypto_alt avg `0.0713` n `231`; crypto_major avg `0.0533` n `8`; equity avg `0.0144` n `128`; fx avg `0.0067` n `6`; index avg `0.0082` n `26`; metal avg `0.0012` n `20`; unknown avg `0.3973` n `792`
- 1h: commodity avg `-0.0246` n `12`; crypto_alt avg `-0.0023` n `231`; crypto_major avg `-0.0142` n `8`; equity avg `0.1085` n `128`; fx avg `0.0021` n `6`; index avg `0.0229` n `26`; metal avg `-0.0059` n `20`; unknown avg `0.8921` n `792`
- 4h: commodity avg `-0.0135` n `12`; crypto_alt avg `-0.0029` n `231`; crypto_major avg `0.1945` n `8`; equity avg `0.1726` n `128`; fx avg `-0.0143` n `6`; index avg `0.0352` n `26`; metal avg `0.0235` n `20`; unknown avg `-0.0993` n `792`
- 24h: commodity avg `-0.0136` n `12`; crypto_alt avg `1.1295` n `231`; crypto_major avg `1.4623` n `8`; equity avg `0.4298` n `128`; fx avg `-0.0458` n `6`; index avg `0.0918` n `26`; metal avg `0.1398` n `20`; unknown avg `0.2001` n `728`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2299`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1471`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0572`, n `668`, weak_sample_signal
