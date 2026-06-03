# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T09:07:27.109644+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.09` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.046` n `12`; crypto_alt avg `-0.1042` n `228`; crypto_major avg `-0.0319` n `8`; equity avg `-0.1225` n `72`; fx avg `0.0307` n `6`; index avg `0.0189` n `23`; metal avg `0.1769` n `18`; unknown avg `-0.3109` n `420`
- 1h: commodity avg `0.2701` n `12`; crypto_alt avg `-0.014` n `228`; crypto_major avg `-0.18` n `8`; equity avg `-0.0787` n `72`; fx avg `0.0118` n `6`; index avg `-0.0186` n `23`; metal avg `0.1419` n `18`; unknown avg `0.7325` n `420`
- 4h: commodity avg `0.7909` n `12`; crypto_alt avg `0.6767` n `228`; crypto_major avg `0.198` n `8`; equity avg `-0.1396` n `72`; fx avg `0.0685` n `6`; index avg `-0.0373` n `23`; metal avg `-0.3527` n `18`; unknown avg `1.0059` n `410`
- 24h: commodity avg `1.8727` n `12`; crypto_alt avg `-1.0621` n `228`; crypto_major avg `-3.246` n `8`; equity avg `0.5947` n `72`; fx avg `0.0629` n `6`; index avg `0.8434` n `23`; metal avg `-1.5574` n `18`; unknown avg `1.2615` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0609`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0545`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0545`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0488`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0475`, n `668`, weak_sample_signal
