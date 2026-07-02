# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T04:37:29.126286+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.014` n `12`; crypto_alt avg `0.0325` n `228`; crypto_major avg `-0.0873` n `8`; equity avg `-0.0472` n `88`; fx avg `0.0111` n `6`; index avg `-0.0054` n `25`; metal avg `-0.0473` n `20`; unknown avg `-0.1285` n `763`
- 1h: commodity avg `0.0549` n `12`; crypto_alt avg `0.2042` n `228`; crypto_major avg `0.1121` n `8`; equity avg `-0.3373` n `88`; fx avg `-0.0046` n `6`; index avg `-0.1046` n `25`; metal avg `-0.0352` n `20`; unknown avg `0.8945` n `761`
- 4h: commodity avg `-0.0209` n `12`; crypto_alt avg `1.4287` n `228`; crypto_major avg `1.4092` n `8`; equity avg `-0.0441` n `88`; fx avg `-0.0263` n `6`; index avg `0.0318` n `25`; metal avg `0.3537` n `20`; unknown avg `-0.1723` n `759`
- 24h: commodity avg `-0.6274` n `12`; crypto_alt avg `1.5022` n `228`; crypto_major avg `1.0123` n `8`; equity avg `-1.6914` n `88`; fx avg `-0.0189` n `6`; index avg `-0.4407` n `25`; metal avg `1.1001` n `20`; unknown avg `24.9106` n `735`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1323`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
