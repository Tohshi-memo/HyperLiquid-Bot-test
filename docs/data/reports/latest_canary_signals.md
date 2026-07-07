# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T07:37:25.692871+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0069` n `12`; crypto_alt avg `-0.2869` n `229`; crypto_major avg `-0.393` n `8`; equity avg `-0.1109` n `91`; fx avg `0.0043` n `6`; index avg `-0.0102` n `25`; metal avg `0.0377` n `20`; unknown avg `-0.0697` n `763`
- 1h: commodity avg `0.0631` n `12`; crypto_alt avg `-0.1815` n `229`; crypto_major avg `-0.1122` n `8`; equity avg `0.0466` n `91`; fx avg `-0.0251` n `6`; index avg `0.0093` n `25`; metal avg `0.0618` n `20`; unknown avg `-0.1026` n `763`
- 4h: commodity avg `0.2352` n `12`; crypto_alt avg `-0.0999` n `229`; crypto_major avg `-0.072` n `8`; equity avg `0.1147` n `91`; fx avg `0.0148` n `6`; index avg `0.0169` n `25`; metal avg `-0.0276` n `20`; unknown avg `13.0813` n `745`
- 24h: commodity avg `0.418` n `12`; crypto_alt avg `0.2404` n `229`; crypto_major avg `-0.5234` n `8`; equity avg `-1.2958` n `90`; fx avg `-0.0373` n `6`; index avg `-0.3259` n `25`; metal avg `-0.3948` n `20`; unknown avg `-0.3826` n `743`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0551`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.053`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0511`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0505`, n `668`, weak_sample_signal
