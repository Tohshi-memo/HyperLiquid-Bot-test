# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T11:52:29.407549+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0236` n `12`; crypto_alt avg `0.013` n `230`; crypto_major avg `-0.0211` n `8`; equity avg `0.004` n `102`; fx avg `0.0466` n `6`; index avg `-0.0011` n `25`; metal avg `0.0026` n `20`; unknown avg `0.0` n `781`
- 1h: commodity avg `0.0153` n `12`; crypto_alt avg `0.0848` n `230`; crypto_major avg `-0.0286` n `8`; equity avg `0.0784` n `102`; fx avg `-0.0552` n `6`; index avg `-0.043` n `25`; metal avg `-0.0009` n `20`; unknown avg `-0.0162` n `781`
- 4h: commodity avg `0.0422` n `12`; crypto_alt avg `-0.1179` n `230`; crypto_major avg `-0.2265` n `8`; equity avg `0.0118` n `102`; fx avg `-0.1046` n `6`; index avg `-0.021` n `25`; metal avg `-0.0149` n `20`; unknown avg `-0.1636` n `781`
- 24h: commodity avg `0.3078` n `12`; crypto_alt avg `0.3957` n `230`; crypto_major avg `-1.2831` n `8`; equity avg `-2.677` n `102`; fx avg `-0.1528` n `6`; index avg `-0.2912` n `25`; metal avg `0.0089` n `20`; unknown avg `4.5901` n `764`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
