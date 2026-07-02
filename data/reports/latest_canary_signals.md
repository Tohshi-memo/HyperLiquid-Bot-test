# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T01:37:30.173967+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0288` n `12`; crypto_alt avg `0.3714` n `228`; crypto_major avg `0.5394` n `8`; equity avg `0.061` n `88`; fx avg `-0.012` n `6`; index avg `0.0886` n `25`; metal avg `0.0021` n `20`; unknown avg `0.0867` n `763`
- 1h: commodity avg `-0.0549` n `12`; crypto_alt avg `0.9238` n `228`; crypto_major avg `0.9252` n `8`; equity avg `0.523` n `88`; fx avg `-0.0209` n `6`; index avg `0.2071` n `25`; metal avg `0.2074` n `20`; unknown avg `-0.2966` n `763`
- 4h: commodity avg `-0.139` n `12`; crypto_alt avg `-0.2962` n `228`; crypto_major avg `-0.5452` n `8`; equity avg `-0.0054` n `88`; fx avg `0.0094` n `6`; index avg `0.0618` n `25`; metal avg `0.291` n `20`; unknown avg `29.2567` n `763`
- 24h: commodity avg `-0.6584` n `12`; crypto_alt avg `2.8584` n `228`; crypto_major avg `2.0243` n `8`; equity avg `-0.9399` n `88`; fx avg `-0.0463` n `6`; index avg `-0.2708` n `25`; metal avg `0.8509` n `20`; unknown avg `25.2288` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1313`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
