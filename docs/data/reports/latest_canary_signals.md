# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T15:52:30.139285+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0051` n `12`; crypto_alt avg `0.0956` n `230`; crypto_major avg `0.0189` n `8`; equity avg `0.0158` n `96`; fx avg `-0.0012` n `6`; index avg `0.0035` n `25`; metal avg `-0.0048` n `20`; unknown avg `-0.0259` n `770`
- 1h: commodity avg `0.0176` n `12`; crypto_alt avg `-0.0124` n `230`; crypto_major avg `-0.0935` n `8`; equity avg `-0.0422` n `96`; fx avg `0.0005` n `6`; index avg `0.0062` n `25`; metal avg `-0.0186` n `20`; unknown avg `-0.0409` n `770`
- 4h: commodity avg `-0.0219` n `12`; crypto_alt avg `-0.0408` n `230`; crypto_major avg `0.1295` n `8`; equity avg `-0.1184` n `96`; fx avg `-0.0069` n `6`; index avg `-0.021` n `25`; metal avg `-0.0562` n `20`; unknown avg `-0.0559` n `770`
- 24h: commodity avg `0.4668` n `12`; crypto_alt avg `-0.4789` n `230`; crypto_major avg `0.4165` n `8`; equity avg `-0.2802` n `96`; fx avg `-0.048` n `6`; index avg `-0.0229` n `25`; metal avg `-0.0257` n `20`; unknown avg `0.0729` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
