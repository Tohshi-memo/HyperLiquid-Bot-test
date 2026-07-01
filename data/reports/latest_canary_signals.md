# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T02:22:33.809009+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.05` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0409` n `12`; crypto_alt avg `0.4499` n `228`; crypto_major avg `0.4746` n `8`; equity avg `0.1837` n `88`; fx avg `-0.0162` n `6`; index avg `0.0546` n `23`; metal avg `0.1097` n `20`; unknown avg `0.5499` n `765`
- 1h: commodity avg `-0.0147` n `12`; crypto_alt avg `0.9604` n `228`; crypto_major avg `0.9679` n `8`; equity avg `-0.2156` n `88`; fx avg `-0.0113` n `6`; index avg `-0.0862` n `23`; metal avg `-0.1434` n `20`; unknown avg `2.5675` n `765`
- 4h: commodity avg `-0.0518` n `12`; crypto_alt avg `0.1732` n `228`; crypto_major avg `0.4281` n `8`; equity avg `-0.7877` n `88`; fx avg `0.0721` n `6`; index avg `-0.266` n `23`; metal avg `-0.4559` n `20`; unknown avg `-0.3504` n `765`
- 24h: commodity avg `0.0601` n `12`; crypto_alt avg `-0.9981` n `228`; crypto_major avg `-0.6236` n `8`; equity avg `0.5361` n `88`; fx avg `0.143` n `6`; index avg `0.0243` n `23`; metal avg `0.0885` n `20`; unknown avg `6.9717` n `735`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1198`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0603`, n `668`, weak_sample_signal
