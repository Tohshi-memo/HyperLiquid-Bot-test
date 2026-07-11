# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T06:37:38.771439+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0317` n `12`; crypto_alt avg `-0.0141` n `230`; crypto_major avg `0.0316` n `8`; equity avg `0.0125` n `92`; fx avg `-0.0031` n `6`; index avg `0.0027` n `25`; metal avg `-0.0008` n `20`; unknown avg `0.0042` n `765`
- 1h: commodity avg `0.0324` n `12`; crypto_alt avg `0.0004` n `230`; crypto_major avg `0.0546` n `8`; equity avg `0.0187` n `92`; fx avg `-0.0037` n `6`; index avg `-0.009` n `25`; metal avg `-0.0055` n `20`; unknown avg `-0.0293` n `733`
- 4h: commodity avg `0.0192` n `12`; crypto_alt avg `0.0135` n `229`; crypto_major avg `0.1802` n `8`; equity avg `0.029` n `92`; fx avg `0.0305` n `6`; index avg `0.0008` n `25`; metal avg `0.0149` n `20`; unknown avg `-0.0759` n `731`
- 24h: commodity avg `-0.2966` n `12`; crypto_alt avg `0.565` n `229`; crypto_major avg `0.0233` n `8`; equity avg `-0.1567` n `92`; fx avg `-0.067` n `6`; index avg `0.149` n `25`; metal avg `0.0231` n `20`; unknown avg `4.1868` n `730`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
