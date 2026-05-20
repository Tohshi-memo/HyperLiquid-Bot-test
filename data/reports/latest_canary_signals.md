# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T14:22:29.132544+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.9662` n `12`; crypto_alt avg `0.7176` n `228`; crypto_major avg `0.3878` n `8`; equity avg `0.513` n `66`; fx avg `0.006` n `6`; index avg `0.3702` n `23`; metal avg `0.6925` n `18`; unknown avg `0.1395` n `384`
- 1h: commodity avg `-0.6294` n `12`; crypto_alt avg `0.5236` n `228`; crypto_major avg `0.2464` n `8`; equity avg `0.1296` n `66`; fx avg `0.0043` n `6`; index avg `0.5607` n `23`; metal avg `0.4818` n `18`; unknown avg `0.4012` n `384`
- 4h: commodity avg `-1.0725` n `12`; crypto_alt avg `0.619` n `228`; crypto_major avg `0.516` n `8`; equity avg `0.2358` n `66`; fx avg `0.0319` n `6`; index avg `0.6115` n `23`; metal avg `0.2751` n `18`; unknown avg `1.4804` n `384`
- 24h: commodity avg `-1.4189` n `12`; crypto_alt avg `1.8612` n `228`; crypto_major avg `1.6254` n `8`; equity avg `2.9094` n `66`; fx avg `-0.0521` n `6`; index avg `1.7165` n `23`; metal avg `0.961` n `18`; unknown avg `1.8071` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0541`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0537`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0491`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0477`, n `668`, weak_sample_signal
