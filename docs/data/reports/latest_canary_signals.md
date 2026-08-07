# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T17:07:38.212926+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0533` n `12`; crypto_alt avg `-0.1305` n `230`; crypto_major avg `-0.2661` n `8`; equity avg `0.0297` n `112`; fx avg `-0.0075` n `6`; index avg `-0.004` n `25`; metal avg `0.041` n `20`; unknown avg `0.0907` n `782`
- 1h: commodity avg `-0.0308` n `12`; crypto_alt avg `-0.3204` n `230`; crypto_major avg `-0.6041` n `8`; equity avg `-0.3821` n `112`; fx avg `-0.0143` n `6`; index avg `-0.0344` n `25`; metal avg `-0.0707` n `20`; unknown avg `0.2291` n `782`
- 4h: commodity avg `0.3099` n `12`; crypto_alt avg `-0.4549` n `230`; crypto_major avg `-1.056` n `8`; equity avg `-0.6097` n `112`; fx avg `-0.005` n `6`; index avg `-0.1271` n `25`; metal avg `-0.1586` n `20`; unknown avg `0.2077` n `782`
- 24h: commodity avg `0.3398` n `12`; crypto_alt avg `-0.4802` n `230`; crypto_major avg `-0.5663` n `8`; equity avg `0.7137` n `112`; fx avg `-0.149` n `6`; index avg `-0.0332` n `25`; metal avg `0.27` n `20`; unknown avg `-0.0789` n `765`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1713`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1445`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1288`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0643`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0603`, n `668`, weak_sample_signal
