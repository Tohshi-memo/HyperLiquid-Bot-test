# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T20:52:23.704930+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0001` n `12`; crypto_alt avg `-0.1066` n `230`; crypto_major avg `-0.0258` n `8`; equity avg `0.0272` n `96`; fx avg `0.0003` n `6`; index avg `-0.0032` n `25`; metal avg `0.0242` n `20`; unknown avg `0.0282` n `769`
- 1h: commodity avg `0.0933` n `12`; crypto_alt avg `-0.2656` n `230`; crypto_major avg `-0.2671` n `8`; equity avg `-0.385` n `96`; fx avg `-0.0375` n `6`; index avg `-0.0933` n `25`; metal avg `-0.0251` n `20`; unknown avg `0.0924` n `769`
- 4h: commodity avg `0.1269` n `12`; crypto_alt avg `-0.4026` n `230`; crypto_major avg `0.0562` n `8`; equity avg `-1.0668` n `96`; fx avg `-0.0421` n `6`; index avg `-0.1905` n `25`; metal avg `-0.0512` n `20`; unknown avg `-0.0241` n `769`
- 24h: commodity avg `0.6294` n `12`; crypto_alt avg `-1.3417` n `230`; crypto_major avg `-1.2933` n `8`; equity avg `-1.4952` n `94`; fx avg `0.0679` n `6`; index avg `-0.297` n `25`; metal avg `0.0141` n `20`; unknown avg `-0.0697` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1318`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
