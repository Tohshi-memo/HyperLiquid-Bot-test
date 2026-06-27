# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T07:22:31.375134+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0231` n `12`; crypto_alt avg `0.181` n `228`; crypto_major avg `0.1252` n `8`; equity avg `-0.0249` n `88`; fx avg `0.0118` n `6`; index avg `-0.0055` n `23`; metal avg `-0.0165` n `20`; unknown avg `-0.4349` n `764`
- 1h: commodity avg `0.0478` n `12`; crypto_alt avg `0.3084` n `228`; crypto_major avg `0.3024` n `8`; equity avg `0.1638` n `88`; fx avg `0.0097` n `6`; index avg `0.023` n `23`; metal avg `-0.0054` n `20`; unknown avg `-0.3828` n `764`
- 4h: commodity avg `0.0243` n `12`; crypto_alt avg `-0.194` n `228`; crypto_major avg `-0.0957` n `8`; equity avg `0.0897` n `88`; fx avg `0.0149` n `6`; index avg `-0.0057` n `23`; metal avg `-0.0087` n `20`; unknown avg `-0.6007` n `732`
- 24h: commodity avg `-0.0747` n `12`; crypto_alt avg `0.9267` n `228`; crypto_major avg `0.5435` n `8`; equity avg `1.3192` n `87`; fx avg `0.0607` n `6`; index avg `0.0156` n `23`; metal avg `0.645` n `20`; unknown avg `-0.598` n `716`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2037`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1609`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
