# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T05:07:24.807013+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0063` n `12`; crypto_alt avg `0.0131` n `230`; crypto_major avg `0.002` n `8`; equity avg `0.0334` n `96`; fx avg `0.002` n `6`; index avg `0.0048` n `25`; metal avg `0.0031` n `20`; unknown avg `0.2025` n `769`
- 1h: commodity avg `0.0066` n `12`; crypto_alt avg `-0.1978` n `230`; crypto_major avg `-0.159` n `8`; equity avg `-0.0376` n `96`; fx avg `-0.0013` n `6`; index avg `0.0066` n `25`; metal avg `0.0024` n `20`; unknown avg `0.2295` n `769`
- 4h: commodity avg `-0.0217` n `12`; crypto_alt avg `-0.2451` n `230`; crypto_major avg `-0.045` n `8`; equity avg `0.0179` n `96`; fx avg `-0.0207` n `6`; index avg `0.0661` n `25`; metal avg `-0.01` n `20`; unknown avg `0.0794` n `769`
- 24h: commodity avg `0.6731` n `12`; crypto_alt avg `-0.6212` n `230`; crypto_major avg `-0.0863` n `8`; equity avg `1.1119` n `96`; fx avg `0.0633` n `6`; index avg `0.1986` n `25`; metal avg `0.2845` n `20`; unknown avg `0.2272` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
