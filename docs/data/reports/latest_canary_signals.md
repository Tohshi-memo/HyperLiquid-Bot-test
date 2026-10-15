# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T11:37:24.868933+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0023` n `13`; crypto_alt avg `0.2156` n `236`; crypto_major avg `0.2261` n `8`; equity avg `0.3222` n `151`; fx avg `0.0052` n `6`; index avg `0.0476` n `26`; metal avg `0.0369` n `20`; unknown avg `0.3838` n `1136`
- 1h: commodity avg `0.0216` n `13`; crypto_alt avg `0.0926` n `236`; crypto_major avg `0.1057` n `8`; equity avg `0.115` n `151`; fx avg `0.0314` n `6`; index avg `0.0233` n `26`; metal avg `0.0508` n `20`; unknown avg `-0.0836` n `1134`
- 4h: commodity avg `0.0672` n `13`; crypto_alt avg `0.3373` n `236`; crypto_major avg `0.0257` n `8`; equity avg `-0.088` n `151`; fx avg `0.0148` n `6`; index avg `0.0186` n `26`; metal avg `0.1678` n `20`; unknown avg `4.4612` n `1038`
- 24h: commodity avg `-0.377` n `13`; crypto_alt avg `-4.522` n `236`; crypto_major avg `-3.3824` n `8`; equity avg `-5.6586` n `151`; fx avg `0.0806` n `6`; index avg `-0.9042` n `26`; metal avg `-0.3383` n `20`; unknown avg `1.9931` n `957`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1191`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1034`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0968`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0871`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0814`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0704`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
