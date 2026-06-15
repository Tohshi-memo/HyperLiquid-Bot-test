# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T09:07:38.180295+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.53` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.131` n `12`; crypto_alt avg `-0.13` n `228`; crypto_major avg `0.0161` n `8`; equity avg `-0.0582` n `74`; fx avg `0.0125` n `6`; index avg `-0.0017` n `23`; metal avg `0.0809` n `18`; unknown avg `0.0265` n `689`
- 1h: commodity avg `-0.2132` n `12`; crypto_alt avg `-0.0972` n `228`; crypto_major avg `0.0735` n `8`; equity avg `0.1123` n `74`; fx avg `-0.0185` n `6`; index avg `0.0549` n `23`; metal avg `0.3745` n `18`; unknown avg `0.0429` n `689`
- 4h: commodity avg `-0.44` n `12`; crypto_alt avg `0.3376` n `228`; crypto_major avg `0.3345` n `8`; equity avg `0.1994` n `74`; fx avg `-0.0076` n `6`; index avg `0.1443` n `23`; metal avg `0.3432` n `18`; unknown avg `0.9109` n `529`
- 24h: commodity avg `-1.175` n `12`; crypto_alt avg `2.9348` n `228`; crypto_major avg `3.0933` n `8`; equity avg `1.8704` n `74`; fx avg `0.0484` n `6`; index avg `1.0199` n `23`; metal avg `2.3485` n `18`; unknown avg `1.6418` n `529`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0578`, n `668`, weak_sample_signal
