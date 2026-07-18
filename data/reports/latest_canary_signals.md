# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T06:52:27.517883+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0009` n `12`; crypto_alt avg `0.0433` n `230`; crypto_major avg `0.0722` n `8`; equity avg `0.0254` n `96`; fx avg `0.0015` n `6`; index avg `-0.0133` n `25`; metal avg `0.0086` n `20`; unknown avg `-0.023` n `769`
- 1h: commodity avg `0.0289` n `12`; crypto_alt avg `0.07` n `230`; crypto_major avg `0.083` n `8`; equity avg `-0.0916` n `96`; fx avg `-0.0029` n `6`; index avg `-0.0225` n `25`; metal avg `-0.0067` n `20`; unknown avg `-0.0241` n `737`
- 4h: commodity avg `-0.0476` n `12`; crypto_alt avg `-0.4019` n `230`; crypto_major avg `-0.1748` n `8`; equity avg `-0.2074` n `96`; fx avg `-0.0029` n `6`; index avg `0.0157` n `25`; metal avg `0.0073` n `20`; unknown avg `-0.0813` n `737`
- 24h: commodity avg `0.9261` n `12`; crypto_alt avg `-0.2469` n `230`; crypto_major avg `0.5042` n `8`; equity avg `1.1524` n `96`; fx avg `0.0113` n `6`; index avg `0.1674` n `25`; metal avg `0.2258` n `20`; unknown avg `0.2718` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1365`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
