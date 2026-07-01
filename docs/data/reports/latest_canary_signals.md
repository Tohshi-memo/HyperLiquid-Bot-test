# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T18:52:25.666904+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0555` n `12`; crypto_alt avg `-0.2301` n `228`; crypto_major avg `-0.1957` n `8`; equity avg `-0.2654` n `88`; fx avg `0.0023` n `6`; index avg `-0.0258` n `25`; metal avg `-0.0494` n `20`; unknown avg `0.4309` n `763`
- 1h: commodity avg `0.0355` n `12`; crypto_alt avg `-0.6381` n `228`; crypto_major avg `-0.2882` n `8`; equity avg `-0.4732` n `88`; fx avg `0.0016` n `6`; index avg `-0.03` n `25`; metal avg `-0.1054` n `20`; unknown avg `-0.6644` n `761`
- 4h: commodity avg `0.043` n `12`; crypto_alt avg `-0.3309` n `228`; crypto_major avg `0.5554` n `8`; equity avg `-0.2037` n `88`; fx avg `-0.0295` n `6`; index avg `-0.088` n `25`; metal avg `-0.2798` n `20`; unknown avg `0.0585` n `761`
- 24h: commodity avg `-0.5585` n `12`; crypto_alt avg `1.2698` n `228`; crypto_major avg `1.5336` n `8`; equity avg `-1.1189` n `88`; fx avg `-0.0074` n `6`; index avg `-0.4987` n `25`; metal avg `0.0597` n `20`; unknown avg `0.4192` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.062`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0585`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0515`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0488`, n `668`, weak_sample_signal
