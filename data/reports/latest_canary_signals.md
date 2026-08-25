# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T12:52:24.093457+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.047` n `12`; crypto_alt avg `0.3783` n `231`; crypto_major avg `0.3819` n `8`; equity avg `0.1028` n `122`; fx avg `0.0095` n `6`; index avg `0.0034` n `25`; metal avg `0.0759` n `20`; unknown avg `0.0687` n `795`
- 1h: commodity avg `-0.1251` n `12`; crypto_alt avg `-0.0644` n `231`; crypto_major avg `-0.0946` n `8`; equity avg `-0.145` n `122`; fx avg `0.0132` n `6`; index avg `-0.0253` n `25`; metal avg `-0.0237` n `20`; unknown avg `-0.015` n `795`
- 4h: commodity avg `-0.3191` n `12`; crypto_alt avg `-0.5368` n `231`; crypto_major avg `-0.7945` n `8`; equity avg `0.1906` n `122`; fx avg `-0.0332` n `6`; index avg `0.054` n `25`; metal avg `0.0973` n `20`; unknown avg `-0.0029` n `794`
- 24h: commodity avg `-0.9986` n `12`; crypto_alt avg `-1.3826` n `231`; crypto_major avg `-0.8158` n `8`; equity avg `0.4677` n `122`; fx avg `0.0344` n `6`; index avg `0.1178` n `25`; metal avg `-0.3217` n `20`; unknown avg `-0.3662` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
