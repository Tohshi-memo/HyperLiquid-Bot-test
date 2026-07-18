# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T07:22:22.614276+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0367` n `12`; crypto_alt avg `0.0215` n `230`; crypto_major avg `0.1077` n `8`; equity avg `0.0612` n `96`; fx avg `0.0073` n `6`; index avg `0.0073` n `25`; metal avg `0.0058` n `20`; unknown avg `-0.0274` n `769`
- 1h: commodity avg `0.0209` n `12`; crypto_alt avg `-0.1572` n `230`; crypto_major avg `0.0015` n `8`; equity avg `-0.0047` n `96`; fx avg `0.0097` n `6`; index avg `-0.0325` n `25`; metal avg `0.0171` n `20`; unknown avg `0.0351` n `769`
- 4h: commodity avg `-0.032` n `12`; crypto_alt avg `-0.4586` n `230`; crypto_major avg `-0.2292` n `8`; equity avg `-0.1651` n `96`; fx avg `0.0051` n `6`; index avg `-0.0027` n `25`; metal avg `0.0054` n `20`; unknown avg `-0.1248` n `737`
- 24h: commodity avg `0.7712` n `12`; crypto_alt avg `-0.0806` n `230`; crypto_major avg `0.6331` n `8`; equity avg `1.2865` n `96`; fx avg `0.0528` n `6`; index avg `0.1611` n `25`; metal avg `0.2917` n `20`; unknown avg `0.2581` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
