# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T17:07:25.176778+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3729` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0101` n `12`; crypto_alt avg `-0.2096` n `231`; crypto_major avg `-0.2537` n `8`; equity avg `-0.3249` n `127`; fx avg `-0.0173` n `6`; index avg `-0.0855` n `26`; metal avg `-0.0757` n `20`; unknown avg `-0.0095` n `793`
- 1h: commodity avg `0.1083` n `12`; crypto_alt avg `-0.5581` n `231`; crypto_major avg `-0.5978` n `8`; equity avg `-0.4648` n `127`; fx avg `-0.0146` n `6`; index avg `-0.1188` n `26`; metal avg `-0.2493` n `20`; unknown avg `0.4488` n `793`
- 4h: commodity avg `0.212` n `12`; crypto_alt avg `-1.8986` n `231`; crypto_major avg `-1.5934` n `8`; equity avg `-1.7093` n `127`; fx avg `-0.016` n `6`; index avg `-0.2205` n `26`; metal avg `-0.792` n `20`; unknown avg `3.692` n `793`
- 24h: commodity avg `-0.0475` n `12`; crypto_alt avg `-3.6935` n `231`; crypto_major avg `-3.3819` n `8`; equity avg `-2.2679` n `127`; fx avg `-0.0937` n `6`; index avg `-0.2139` n `26`; metal avg `-0.1968` n `20`; unknown avg `-0.3742` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1232`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
