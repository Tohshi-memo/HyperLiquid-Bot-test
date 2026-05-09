# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T19:46:51.486670+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.64` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0004` n `12`; crypto_alt avg `0.0317` n `228`; crypto_major avg `0.0002` n `8`; equity avg `-0.0096` n `65`; fx avg `-0.0006` n `5`; index avg `-0.0146` n `23`; metal avg `0.0128` n `18`; unknown avg `-0.1203` n `376`
- 1h: commodity avg `0.0209` n `12`; crypto_alt avg `0.0227` n `228`; crypto_major avg `-0.0178` n `8`; equity avg `-0.0283` n `65`; fx avg `-0.0066` n `5`; index avg `-0.0115` n `23`; metal avg `0.02` n `18`; unknown avg `-0.0982` n `376`
- 4h: commodity avg `0.0527` n `12`; crypto_alt avg `0.8075` n `228`; crypto_major avg `0.3718` n `8`; equity avg `0.147` n `65`; fx avg `-0.0185` n `5`; index avg `0.0286` n `23`; metal avg `0.0946` n `18`; unknown avg `-0.2264` n `376`
- 24h: commodity avg `0.2704` n `12`; crypto_alt avg `0.6659` n `228`; crypto_major avg `0.3924` n `8`; equity avg `1.0407` n `65`; fx avg `-0.033` n `5`; index avg `0.38` n `23`; metal avg `-0.1869` n `18`; unknown avg `0.1846` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
