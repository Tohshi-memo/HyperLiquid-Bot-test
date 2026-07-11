# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T15:37:29.724472+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0082` n `12`; crypto_alt avg `-0.3596` n `230`; crypto_major avg `-0.3181` n `8`; equity avg `-0.089` n `92`; fx avg `0.007` n `6`; index avg `-0.0094` n `25`; metal avg `-0.0098` n `20`; unknown avg `0.1765` n `765`
- 1h: commodity avg `0.0136` n `12`; crypto_alt avg `-0.3402` n `230`; crypto_major avg `-0.1997` n `8`; equity avg `-0.0586` n `92`; fx avg `-0.0043` n `6`; index avg `0.0127` n `25`; metal avg `-0.0254` n `20`; unknown avg `0.1871` n `765`
- 4h: commodity avg `0.0061` n `12`; crypto_alt avg `0.2336` n `230`; crypto_major avg `0.3804` n `8`; equity avg `-0.1109` n `92`; fx avg `-0.0093` n `6`; index avg `0.0158` n `25`; metal avg `-0.0301` n `20`; unknown avg `0.1924` n `765`
- 24h: commodity avg `0.2553` n `12`; crypto_alt avg `0.809` n `229`; crypto_major avg `0.5863` n `8`; equity avg `0.289` n `92`; fx avg `-0.033` n `6`; index avg `0.0622` n `25`; metal avg `0.027` n `20`; unknown avg `2.9465` n `727`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
