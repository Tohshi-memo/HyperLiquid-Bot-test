# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T07:07:27.020817+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0438` n `12`; crypto_alt avg `-0.043` n `230`; crypto_major avg `-0.0923` n `8`; equity avg `0.0434` n `92`; fx avg `0.0027` n `6`; index avg `-0.0121` n `25`; metal avg `-0.006` n `20`; unknown avg `-0.0214` n `766`
- 1h: commodity avg `0.0925` n `12`; crypto_alt avg `0.0346` n `230`; crypto_major avg `-0.0798` n `8`; equity avg `-0.0089` n `92`; fx avg `0.0366` n `6`; index avg `-0.0412` n `25`; metal avg `-0.0019` n `20`; unknown avg `0.1602` n `766`
- 4h: commodity avg `0.0404` n `12`; crypto_alt avg `0.5359` n `230`; crypto_major avg `0.2724` n `8`; equity avg `1.2698` n `92`; fx avg `0.0573` n `6`; index avg `0.303` n `25`; metal avg `0.2145` n `20`; unknown avg `-0.0013` n `750`
- 24h: commodity avg `1.1231` n `12`; crypto_alt avg `-0.5036` n `230`; crypto_major avg `-0.5727` n `8`; equity avg `-0.2558` n `92`; fx avg `-0.135` n `6`; index avg `-0.0487` n `25`; metal avg `0.1169` n `20`; unknown avg `-0.265` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1807`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.164`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
