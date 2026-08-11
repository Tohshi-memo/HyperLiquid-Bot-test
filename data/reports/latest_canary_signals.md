# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T05:41:02.798964+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0585` n `12`; crypto_alt avg `0.097` n `230`; crypto_major avg `0.1399` n `8`; equity avg `-0.0313` n `113`; fx avg `0.0033` n `6`; index avg `0.0023` n `25`; metal avg `-0.1656` n `20`; unknown avg `-0.1796` n `785`
- 1h: commodity avg `0.0242` n `12`; crypto_alt avg `-0.0559` n `230`; crypto_major avg `-0.1075` n `8`; equity avg `-0.1852` n `113`; fx avg `0.0113` n `6`; index avg `-0.037` n `25`; metal avg `-0.2667` n `20`; unknown avg `0.1034` n `785`
- 4h: commodity avg `-0.016` n `12`; crypto_alt avg `-0.2136` n `230`; crypto_major avg `0.0195` n `8`; equity avg `0.0934` n `113`; fx avg `0.0064` n `6`; index avg `0.0495` n `25`; metal avg `-0.3684` n `20`; unknown avg `-0.3561` n `785`
- 24h: commodity avg `0.8697` n `12`; crypto_alt avg `-0.7185` n `230`; crypto_major avg `-0.6664` n `8`; equity avg `-0.9346` n `113`; fx avg `0.0898` n `6`; index avg `0.0377` n `25`; metal avg `0.0937` n `20`; unknown avg `103.9184` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1613`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1604`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.159`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1576`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1516`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1365`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
