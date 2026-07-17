# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T18:16:00.808569+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.008` n `12`; crypto_alt avg `-0.0072` n `230`; crypto_major avg `-0.0128` n `8`; equity avg `-0.2009` n `96`; fx avg `-0.0027` n `6`; index avg `-0.0144` n `25`; metal avg `-0.0228` n `20`; unknown avg `-0.078` n `769`
- 1h: commodity avg `0.0886` n `12`; crypto_alt avg `-0.1656` n `230`; crypto_major avg `-0.1086` n `8`; equity avg `-0.6374` n `96`; fx avg `-0.0004` n `6`; index avg `-0.1011` n `25`; metal avg `-0.0617` n `20`; unknown avg `-0.0691` n `769`
- 4h: commodity avg `0.2679` n `12`; crypto_alt avg `0.4853` n `230`; crypto_major avg `0.6291` n `8`; equity avg `0.5815` n `96`; fx avg `0.0706` n `6`; index avg `0.0753` n `25`; metal avg `0.0984` n `20`; unknown avg `0.3689` n `769`
- 24h: commodity avg `0.9151` n `12`; crypto_alt avg `-1.182` n `230`; crypto_major avg `-1.3385` n `8`; equity avg `-1.2084` n `94`; fx avg `0.0932` n `6`; index avg `-0.2646` n `25`; metal avg `-0.1366` n `20`; unknown avg `-0.0352` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
