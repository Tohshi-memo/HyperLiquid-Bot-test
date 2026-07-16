# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T21:07:30.507590+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0181` n `12`; crypto_alt avg `0.1429` n `230`; crypto_major avg `0.088` n `8`; equity avg `-0.046` n `94`; fx avg `-0.0016` n `6`; index avg `0.0189` n `25`; metal avg `0.0183` n `20`; unknown avg `0.0748` n `768`
- 1h: commodity avg `0.1539` n `12`; crypto_alt avg `0.1371` n `230`; crypto_major avg `0.1004` n `8`; equity avg `-0.0485` n `94`; fx avg `0.0033` n `6`; index avg `0.0313` n `25`; metal avg `-0.0118` n `20`; unknown avg `-0.0278` n `768`
- 4h: commodity avg `0.2623` n `12`; crypto_alt avg `-0.2762` n `230`; crypto_major avg `-0.3611` n `8`; equity avg `-0.4895` n `94`; fx avg `-0.0009` n `6`; index avg `-0.0773` n `25`; metal avg `-0.1747` n `20`; unknown avg `-0.2592` n `768`
- 24h: commodity avg `-0.1873` n `12`; crypto_alt avg `-0.9163` n `230`; crypto_major avg `-1.9548` n `8`; equity avg `-3.7435` n `94`; fx avg `-0.1735` n `6`; index avg `-0.5044` n `25`; metal avg `-0.8528` n `20`; unknown avg `-0.4387` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
