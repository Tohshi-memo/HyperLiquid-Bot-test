# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T05:52:26.961073+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0067` n `12`; crypto_alt avg `-0.1789` n `230`; crypto_major avg `-0.0884` n `8`; equity avg `-0.0231` n `92`; fx avg `0.0` n `6`; index avg `-0.0113` n `25`; metal avg `-0.0021` n `20`; unknown avg `-0.0093` n `765`
- 1h: commodity avg `-0.027` n `12`; crypto_alt avg `0.0079` n `230`; crypto_major avg `0.086` n `8`; equity avg `0.0044` n `92`; fx avg `0.0312` n `6`; index avg `-0.0127` n `25`; metal avg `-0.0067` n `20`; unknown avg `0.171` n `765`
- 4h: commodity avg `-0.0287` n `12`; crypto_alt avg `-0.0995` n `229`; crypto_major avg `0.0816` n `8`; equity avg `0.0922` n `92`; fx avg `0.0315` n `6`; index avg `0.0088` n `25`; metal avg `0.0212` n `20`; unknown avg `-0.1773` n `763`
- 24h: commodity avg `-0.3553` n `12`; crypto_alt avg `0.1863` n `229`; crypto_major avg `-0.4231` n `8`; equity avg `-0.4079` n `92`; fx avg `-0.1151` n `6`; index avg `0.0663` n `25`; metal avg `0.0226` n `20`; unknown avg `4.1413` n `730`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
