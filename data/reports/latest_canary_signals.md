# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T07:52:23.364726+00:00`
- Correlation status: `ready`
- Asset price records: `531`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.29` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.2178` n `12`; crypto_alt avg `0.0142` n `228`; crypto_major avg `0.0426` n `8`; equity avg `-0.0598` n `65`; fx avg `-0.0128` n `4`; index avg `0.0169` n `23`; metal avg `0.1415` n `18`; unknown avg `-0.0099` n `358`
- 1h: commodity avg `-0.4242` n `12`; crypto_alt avg `0.3693` n `228`; crypto_major avg `0.4361` n `8`; equity avg `0.2385` n `65`; fx avg `-0.0255` n `4`; index avg `0.08` n `23`; metal avg `0.4946` n `18`; unknown avg `0.1563` n `358`
- 4h: commodity avg `-0.764` n `12`; crypto_alt avg `1.9723` n `228`; crypto_major avg `1.2231` n `8`; equity avg `0.7045` n `65`; fx avg `-0.0993` n `4`; index avg `0.2566` n `23`; metal avg `1.2173` n `18`; unknown avg `0.5251` n `356`
- 24h: commodity avg `-2.2682` n `7`; crypto_alt avg `1.3973` n `223`; crypto_major avg `-0.4326` n `7`; equity avg `1.8968` n `47`; fx avg `-0.0862` n `4`; index avg `1.6402` n `6`; metal avg `2.371` n `7`; unknown avg `0.9454` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1308`, n `527`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1223`, n `527`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1031`, n `523`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0945`, n `527`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0924`, n `523`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0824`, n `523`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0819`, n `523`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0763`, n `523`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0719`, n `523`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0637`, n `527`, weak_sample_signal
