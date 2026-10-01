# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T13:33:58.081347+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0263` n `13`; crypto_alt avg `0.3033` n `234`; crypto_major avg `0.2263` n `8`; equity avg `-0.017` n `142`; fx avg `-0.0017` n `6`; index avg `0.0155` n `26`; metal avg `-0.0607` n `20`; unknown avg `118.2671` n `975`
- 1h: commodity avg `0.0256` n `13`; crypto_alt avg `-0.2615` n `234`; crypto_major avg `-0.339` n `8`; equity avg `-0.1889` n `142`; fx avg `-0.0093` n `6`; index avg `-0.0483` n `26`; metal avg `-0.1793` n `20`; unknown avg `4.3235` n `973`
- 4h: commodity avg `-0.0664` n `13`; crypto_alt avg `-0.7493` n `234`; crypto_major avg `-0.1797` n `8`; equity avg `-0.2657` n `142`; fx avg `-0.0549` n `6`; index avg `0.0028` n `26`; metal avg `0.1049` n `20`; unknown avg `1.9869` n `967`
- 24h: commodity avg `-0.2544` n `13`; crypto_alt avg `-1.3965` n `234`; crypto_major avg `-0.6437` n `8`; equity avg `0.0225` n `142`; fx avg `0.0421` n `6`; index avg `0.0615` n `26`; metal avg `-0.1949` n `20`; unknown avg `772.1036` n `794`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.168`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.146`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
