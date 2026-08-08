# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T08:07:31.086981+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0029` n `12`; crypto_alt avg `0.0532` n `230`; crypto_major avg `0.0281` n `8`; equity avg `0.0083` n `112`; fx avg `0.0047` n `6`; index avg `0.0178` n `25`; metal avg `-0.0162` n `20`; unknown avg `-0.0186` n `784`
- 1h: commodity avg `0.0195` n `12`; crypto_alt avg `0.0027` n `230`; crypto_major avg `-0.0077` n `8`; equity avg `0.0304` n `112`; fx avg `-0.0042` n `6`; index avg `0.0071` n `25`; metal avg `0.0019` n `20`; unknown avg `0.1493` n `784`
- 4h: commodity avg `0.011` n `12`; crypto_alt avg `0.1123` n `230`; crypto_major avg `0.0308` n `8`; equity avg `-0.1079` n `112`; fx avg `0.0019` n `6`; index avg `-0.0387` n `25`; metal avg `-0.0208` n `20`; unknown avg `0.0381` n `751`
- 24h: commodity avg `-0.156` n `12`; crypto_alt avg `-0.009` n `230`; crypto_major avg `0.6557` n `8`; equity avg `0.9085` n `112`; fx avg `-0.0519` n `6`; index avg `0.0458` n `25`; metal avg `-0.0348` n `20`; unknown avg `0.0577` n `750`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1588`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0605`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0582`, n `668`, weak_sample_signal
