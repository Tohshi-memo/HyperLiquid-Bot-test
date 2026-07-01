# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T18:37:27.440713+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.5313` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0236` n `12`; crypto_alt avg `-0.1789` n `228`; crypto_major avg `-0.0622` n `8`; equity avg `-0.0899` n `88`; fx avg `0.0031` n `6`; index avg `0.0038` n `25`; metal avg `0.0018` n `20`; unknown avg `0.0292` n `761`
- 1h: commodity avg `0.0504` n `12`; crypto_alt avg `-0.3205` n `228`; crypto_major avg `-0.0532` n `8`; equity avg `-0.174` n `88`; fx avg `-0.0041` n `6`; index avg `-0.0131` n `25`; metal avg `-0.1048` n `20`; unknown avg `-0.4767` n `761`
- 4h: commodity avg `-0.0608` n `12`; crypto_alt avg `0.0101` n `228`; crypto_major avg `1.0529` n `8`; equity avg `-0.1517` n `88`; fx avg `-0.0177` n `6`; index avg `-0.0892` n `25`; metal avg `-0.4784` n `20`; unknown avg `0.0886` n `761`
- 24h: commodity avg `-0.4363` n `12`; crypto_alt avg `1.796` n `228`; crypto_major avg `2.1103` n `8`; equity avg `-0.7962` n `88`; fx avg `-0.0079` n `6`; index avg `-0.4658` n `25`; metal avg `0.1892` n `20`; unknown avg `0.0915` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0604`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.058`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0524`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0523`, n `668`, weak_sample_signal
