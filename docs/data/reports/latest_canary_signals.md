# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T19:22:26.089892+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0195` n `12`; crypto_alt avg `-0.0839` n `228`; crypto_major avg `-0.0359` n `8`; equity avg `0.129` n `88`; fx avg `0.0007` n `6`; index avg `0.0168` n `25`; metal avg `-0.031` n `20`; unknown avg `-0.1066` n `763`
- 1h: commodity avg `-0.0451` n `12`; crypto_alt avg `-0.3077` n `228`; crypto_major avg `-0.1234` n `8`; equity avg `-0.0823` n `88`; fx avg `0.0056` n `6`; index avg `0.0082` n `25`; metal avg `-0.0087` n `20`; unknown avg `-0.0548` n `761`
- 4h: commodity avg `-0.0216` n `12`; crypto_alt avg `-0.5842` n `228`; crypto_major avg `0.1063` n `8`; equity avg `-0.6318` n `88`; fx avg `-0.0046` n `6`; index avg `-0.1227` n `25`; metal avg `-0.1603` n `20`; unknown avg `-0.1756` n `761`
- 24h: commodity avg `-0.5475` n `12`; crypto_alt avg `1.5874` n `228`; crypto_major avg `1.8558` n `8`; equity avg `-0.9737` n `88`; fx avg `0.0045` n `6`; index avg `-0.4761` n `25`; metal avg `0.1958` n `20`; unknown avg `0.4328` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.059`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0547`, n `668`, weak_sample_signal
