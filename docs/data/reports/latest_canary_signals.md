# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T08:37:27.680635+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.057` n `12`; crypto_alt avg `0.1027` n `230`; crypto_major avg `0.1436` n `8`; equity avg `0.0771` n `98`; fx avg `0.0105` n `6`; index avg `0.0034` n `25`; metal avg `0.0037` n `20`; unknown avg `-0.0054` n `773`
- 1h: commodity avg `-0.0064` n `12`; crypto_alt avg `0.3147` n `230`; crypto_major avg `0.395` n `8`; equity avg `0.4564` n `98`; fx avg `-0.0122` n `6`; index avg `0.0651` n `25`; metal avg `0.0442` n `20`; unknown avg `0.035` n `773`
- 4h: commodity avg `0.291` n `12`; crypto_alt avg `0.1011` n `230`; crypto_major avg `-0.1145` n `8`; equity avg `0.0042` n `98`; fx avg `0.0337` n `6`; index avg `-0.0793` n `25`; metal avg `-0.4101` n `20`; unknown avg `-0.247` n `741`
- 24h: commodity avg `0.7248` n `12`; crypto_alt avg `0.0738` n `230`; crypto_major avg `0.0313` n `8`; equity avg `0.6231` n `98`; fx avg `-0.0615` n `6`; index avg `0.1493` n `25`; metal avg `-0.3181` n `20`; unknown avg `11.4916` n `741`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1515`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0816`, n `666`, weak_sample_signal
