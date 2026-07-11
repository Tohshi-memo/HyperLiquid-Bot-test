# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T07:07:27.356005+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0049` n `12`; crypto_alt avg `-0.0039` n `230`; crypto_major avg `-0.0391` n `8`; equity avg `-0.0253` n `92`; fx avg `0.0` n `6`; index avg `0.0136` n `25`; metal avg `-0.0046` n `20`; unknown avg `-0.0042` n `765`
- 1h: commodity avg `0.0477` n `12`; crypto_alt avg `0.0741` n `230`; crypto_major avg `0.0337` n `8`; equity avg `0.0861` n `92`; fx avg `-0.012` n `6`; index avg `0.0195` n `25`; metal avg `-0.004` n `20`; unknown avg `0.004` n `765`
- 4h: commodity avg `0.0248` n `12`; crypto_alt avg `-0.2575` n `229`; crypto_major avg `-0.0037` n `8`; equity avg `0.0501` n `92`; fx avg `0.0185` n `6`; index avg `0.0131` n `25`; metal avg `0.0103` n `20`; unknown avg `-0.0201` n `731`
- 24h: commodity avg `-0.2452` n `12`; crypto_alt avg `0.5068` n `229`; crypto_major avg `-0.0825` n `8`; equity avg `0.0372` n `92`; fx avg `-0.0845` n `6`; index avg `0.1638` n `25`; metal avg `0.0237` n `20`; unknown avg `2.8924` n `730`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
