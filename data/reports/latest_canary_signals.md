# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T06:37:29.323971+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.015` n `13`; crypto_alt avg `-0.0753` n `239`; crypto_major avg `-0.0518` n `8`; equity avg `0.1262` n `166`; fx avg `0.0283` n `6`; index avg `0.0195` n `27`; metal avg `-0.0595` n `20`; unknown avg `1.1762` n `1262`
- 1h: commodity avg `0.0279` n `13`; crypto_alt avg `-0.3328` n `239`; crypto_major avg `-0.5839` n `8`; equity avg `-0.3495` n `166`; fx avg `0.0169` n `6`; index avg `-0.0449` n `27`; metal avg `-0.2296` n `20`; unknown avg `325.8709` n `1228`
- 4h: commodity avg `0.0059` n `13`; crypto_alt avg `0.7094` n `239`; crypto_major avg `0.1631` n `8`; equity avg `-0.4683` n `166`; fx avg `0.0532` n `6`; index avg `-0.0394` n `27`; metal avg `-0.479` n `20`; unknown avg `-0.2721` n `1208`
- 24h: commodity avg `-1.1217` n `13`; crypto_alt avg `0.6689` n `239`; crypto_major avg `0.0151` n `8`; equity avg `4.3479` n `166`; fx avg `-0.2279` n `6`; index avg `0.6621` n `27`; metal avg `-0.3138` n `20`; unknown avg `305.6953` n `1034`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
