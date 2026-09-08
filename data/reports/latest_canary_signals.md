# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T19:07:36.693399+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0542` n `12`; crypto_alt avg `0.2512` n `233`; crypto_major avg `0.3053` n `8`; equity avg `0.1558` n `134`; fx avg `-0.0155` n `6`; index avg `0.0209` n `26`; metal avg `0.0947` n `20`; unknown avg `3.3699` n `795`
- 1h: commodity avg `0.3119` n `12`; crypto_alt avg `-0.7113` n `233`; crypto_major avg `-0.2802` n `8`; equity avg `-0.217` n `134`; fx avg `-0.027` n `6`; index avg `-0.0449` n `26`; metal avg `-0.1221` n `20`; unknown avg `1.0718` n `795`
- 4h: commodity avg `0.2068` n `12`; crypto_alt avg `-0.5615` n `232`; crypto_major avg `0.266` n `8`; equity avg `0.1681` n `134`; fx avg `-0.073` n `6`; index avg `-0.0095` n `26`; metal avg `-0.1843` n `20`; unknown avg `-0.0554` n `765`
- 24h: commodity avg `0.0347` n `12`; crypto_alt avg `0.1324` n `232`; crypto_major avg `0.2756` n `8`; equity avg `0.7729` n `134`; fx avg `-0.1109` n `6`; index avg `-0.0995` n `26`; metal avg `-0.1807` n `20`; unknown avg `9.5035` n `706`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1458`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
