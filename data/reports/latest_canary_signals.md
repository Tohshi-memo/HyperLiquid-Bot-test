# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T07:52:31.522446+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.006` n `12`; crypto_alt avg `0.137` n `229`; crypto_major avg `0.1806` n `8`; equity avg `0.0464` n `88`; fx avg `0.0009` n `6`; index avg `0.013` n `25`; metal avg `-0.0007` n `20`; unknown avg `-0.0376` n `765`
- 1h: commodity avg `0.0026` n `12`; crypto_alt avg `-0.1068` n `229`; crypto_major avg `0.1206` n `8`; equity avg `-0.0317` n `88`; fx avg `0.0003` n `6`; index avg `-0.0333` n `25`; metal avg `-0.0054` n `20`; unknown avg `0.2601` n `765`
- 4h: commodity avg `-0.0243` n `12`; crypto_alt avg `-0.3634` n `229`; crypto_major avg `-0.0713` n `8`; equity avg `0.0621` n `88`; fx avg `-0.0084` n `6`; index avg `-0.0151` n `25`; metal avg `0.0187` n `20`; unknown avg `0.2426` n `745`
- 24h: commodity avg `-0.032` n `12`; crypto_alt avg `1.5482` n `229`; crypto_major avg `2.2469` n `8`; equity avg `0.4015` n `88`; fx avg `0.0005` n `6`; index avg `-0.0328` n `25`; metal avg `-0.1929` n `20`; unknown avg `4.9862` n `733`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
