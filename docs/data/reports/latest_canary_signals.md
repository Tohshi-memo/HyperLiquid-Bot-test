# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T13:07:30.667772+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0084` n `12`; crypto_alt avg `-0.059` n `228`; crypto_major avg `-0.0364` n `8`; equity avg `-0.252` n `86`; fx avg `-0.002` n `6`; index avg `-0.0504` n `23`; metal avg `-0.0098` n `20`; unknown avg `-0.003` n `764`
- 1h: commodity avg `-0.0031` n `12`; crypto_alt avg `-0.4649` n `228`; crypto_major avg `-0.455` n `8`; equity avg `-0.772` n `86`; fx avg `-0.0118` n `6`; index avg `-0.1473` n `23`; metal avg `-0.017` n `20`; unknown avg `-0.2724` n `764`
- 4h: commodity avg `-0.0444` n `12`; crypto_alt avg `0.1082` n `228`; crypto_major avg `-0.0441` n `8`; equity avg `-0.2088` n `86`; fx avg `-0.0518` n `6`; index avg `-0.0994` n `23`; metal avg `0.0549` n `20`; unknown avg `-0.2109` n `764`
- 24h: commodity avg `-0.5273` n `12`; crypto_alt avg `-4.83` n `228`; crypto_major avg `-5.0279` n `8`; equity avg `-4.9041` n `85`; fx avg `-0.1696` n `6`; index avg `-1.0399` n `23`; metal avg `-1.2492` n `20`; unknown avg `0.0735` n `604`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1561`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1373`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
