# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T06:52:30.419116+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0268` n `12`; crypto_alt avg `0.1922` n `232`; crypto_major avg `0.152` n `8`; equity avg `-0.0364` n `133`; fx avg `0.0009` n `6`; index avg `-0.0082` n `26`; metal avg `0.0011` n `20`; unknown avg `0.0721` n `793`
- 1h: commodity avg `-0.0323` n `12`; crypto_alt avg `0.1673` n `232`; crypto_major avg `0.0054` n `8`; equity avg `-0.1934` n `133`; fx avg `-0.0368` n `6`; index avg `-0.0344` n `26`; metal avg `-0.0519` n `20`; unknown avg `-0.1063` n `755`
- 4h: commodity avg `-0.07` n `12`; crypto_alt avg `-0.7195` n `232`; crypto_major avg `-0.2112` n `8`; equity avg `-0.0315` n `133`; fx avg `-0.0368` n `6`; index avg `0.0314` n `26`; metal avg `-0.1297` n `20`; unknown avg `0.5394` n `755`
- 24h: commodity avg `-0.0245` n `12`; crypto_alt avg `1.749` n `232`; crypto_major avg `3.6117` n `8`; equity avg `1.6852` n `133`; fx avg `-0.0702` n `6`; index avg `0.3223` n `26`; metal avg `0.4101` n `20`; unknown avg `1.7023` n `730`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
