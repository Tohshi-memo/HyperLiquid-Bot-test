# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T09:52:37.281757+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0134` n `12`; crypto_alt avg `-0.0319` n `230`; crypto_major avg `-0.0175` n `8`; equity avg `-0.0869` n `114`; fx avg `-0.0206` n `6`; index avg `-0.0136` n `25`; metal avg `0.0094` n `20`; unknown avg `-0.0203` n `795`
- 1h: commodity avg `-0.0152` n `12`; crypto_alt avg `-0.0516` n `230`; crypto_major avg `-0.191` n `8`; equity avg `-0.3411` n `114`; fx avg `-0.0442` n `6`; index avg `-0.0506` n `25`; metal avg `0.0251` n `20`; unknown avg `-0.0233` n `795`
- 4h: commodity avg `-0.0004` n `12`; crypto_alt avg `0.4866` n `230`; crypto_major avg `0.0525` n `8`; equity avg `-1.0937` n `114`; fx avg `-0.0196` n `6`; index avg `-0.1403` n `25`; metal avg `-0.0869` n `20`; unknown avg `-0.0205` n `761`
- 24h: commodity avg `0.4806` n `12`; crypto_alt avg `-0.5756` n `230`; crypto_major avg `0.1592` n `8`; equity avg `-2.7512` n `114`; fx avg `-0.0591` n `6`; index avg `-0.5465` n `25`; metal avg `-0.2176` n `20`; unknown avg `0.0109` n `760`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1461`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
