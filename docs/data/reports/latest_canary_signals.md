# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T18:52:18.092643+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0244` n `12`; crypto_alt avg `-0.0291` n `228`; crypto_major avg `-0.0879` n `8`; equity avg `0.0633` n `69`; fx avg `-0.0037` n `6`; index avg `0.0006` n `23`; metal avg `-0.0011` n `18`; unknown avg `0.951` n `421`
- 1h: commodity avg `0.0246` n `12`; crypto_alt avg `-0.0968` n `228`; crypto_major avg `-0.2637` n `8`; equity avg `0.0413` n `69`; fx avg `-0.0016` n `6`; index avg `-0.055` n `23`; metal avg `0.0101` n `18`; unknown avg `0.7826` n `421`
- 4h: commodity avg `0.1643` n `12`; crypto_alt avg `0.0461` n `228`; crypto_major avg `-0.2939` n `8`; equity avg `0.1439` n `69`; fx avg `-0.0081` n `6`; index avg `0.2649` n `23`; metal avg `-0.0519` n `18`; unknown avg `0.774` n `421`
- 24h: commodity avg `0.7021` n `12`; crypto_alt avg `-1.3914` n `228`; crypto_major avg `-0.7702` n `8`; equity avg `0.9385` n `69`; fx avg `-0.0116` n `6`; index avg `0.1388` n `23`; metal avg `-0.1356` n `18`; unknown avg `1.1859` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2321`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.179`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1487`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
