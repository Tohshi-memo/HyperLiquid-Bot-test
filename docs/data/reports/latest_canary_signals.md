# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T07:52:59.430348+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0324` n `12`; crypto_alt avg `0.0153` n `230`; crypto_major avg `-0.0634` n `8`; equity avg `0.1949` n `120`; fx avg `-0.0187` n `6`; index avg `0.0175` n `25`; metal avg `-0.0427` n `20`; unknown avg `0.0294` n `789`
- 1h: commodity avg `-0.0318` n `12`; crypto_alt avg `0.0494` n `230`; crypto_major avg `0.0234` n `8`; equity avg `0.8271` n `120`; fx avg `-0.0121` n `6`; index avg `0.0631` n `25`; metal avg `0.0143` n `20`; unknown avg `0.0167` n `789`
- 4h: commodity avg `-0.0268` n `12`; crypto_alt avg `-0.015` n `230`; crypto_major avg `0.0299` n `8`; equity avg `0.7711` n `120`; fx avg `-0.0196` n `6`; index avg `0.1247` n `25`; metal avg `-0.0471` n `20`; unknown avg `-0.0197` n `757`
- 24h: commodity avg `0.3039` n `12`; crypto_alt avg `0.4009` n `230`; crypto_major avg `0.1682` n `8`; equity avg `-2.1269` n `120`; fx avg `-0.1689` n `6`; index avg `-0.2857` n `25`; metal avg `-0.5555` n `20`; unknown avg `-0.2436` n `757`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1463`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
