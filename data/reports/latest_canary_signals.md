# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T18:22:28.291616+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.019` n `12`; crypto_alt avg `-0.0348` n `233`; crypto_major avg `-0.0521` n `8`; equity avg `-0.0275` n `134`; fx avg `-0.0069` n `6`; index avg `-0.0061` n `26`; metal avg `0.0091` n `20`; unknown avg `1.2608` n `797`
- 1h: commodity avg `0.0913` n `12`; crypto_alt avg `-0.2028` n `233`; crypto_major avg `-0.0286` n `8`; equity avg `0.0233` n `134`; fx avg `-0.0173` n `6`; index avg `-0.0104` n `26`; metal avg `-0.0471` n `20`; unknown avg `3.4113` n `795`
- 4h: commodity avg `-0.1472` n `12`; crypto_alt avg `-0.3779` n `233`; crypto_major avg `-0.2468` n `8`; equity avg `-0.0484` n `134`; fx avg `0.0236` n `6`; index avg `-0.0695` n `26`; metal avg `0.1008` n `20`; unknown avg `0.0286` n `789`
- 24h: commodity avg `0.212` n `12`; crypto_alt avg `-0.9741` n `233`; crypto_major avg `-0.5417` n `8`; equity avg `-0.6504` n `134`; fx avg `-0.0756` n `6`; index avg `-0.2466` n `26`; metal avg `0.4419` n `20`; unknown avg `7.5423` n `699`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
