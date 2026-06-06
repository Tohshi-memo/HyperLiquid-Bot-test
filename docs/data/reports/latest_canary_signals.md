# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T13:52:27.178699+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0357` n `12`; crypto_alt avg `-0.0517` n `228`; crypto_major avg `0.0095` n `8`; equity avg `-0.017` n `74`; fx avg `-0.0018` n `6`; index avg `0.0192` n `23`; metal avg `0.0116` n `18`; unknown avg `0.7441` n `513`
- 1h: commodity avg `0.0779` n `12`; crypto_alt avg `-0.1562` n `228`; crypto_major avg `-0.5113` n `8`; equity avg `-0.1026` n `74`; fx avg `0.0053` n `6`; index avg `0.0676` n `23`; metal avg `-0.0037` n `18`; unknown avg `-0.0158` n `415`
- 4h: commodity avg `0.1645` n `12`; crypto_alt avg `0.1207` n `228`; crypto_major avg `-0.1739` n `8`; equity avg `0.5667` n `74`; fx avg `0.0115` n `6`; index avg `0.4928` n `23`; metal avg `0.0457` n `18`; unknown avg `0.1244` n `411`
- 24h: commodity avg `-0.6456` n `12`; crypto_alt avg `-2.6753` n `228`; crypto_major avg `-2.3293` n `8`; equity avg `-4.1163` n `74`; fx avg `-0.1976` n `6`; index avg `-2.3176` n `23`; metal avg `-2.7327` n `18`; unknown avg `-1.0276` n `400`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
