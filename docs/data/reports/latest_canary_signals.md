# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T23:47:40.116014+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0081` n `12`; crypto_alt avg `0.0309` n `230`; crypto_major avg `-0.0185` n `8`; equity avg `0.0236` n `113`; fx avg `-0.0113` n `6`; index avg `0.0052` n `25`; metal avg `0.0012` n `20`; unknown avg `-0.0085` n `785`
- 1h: commodity avg `0.0034` n `12`; crypto_alt avg `0.007` n `230`; crypto_major avg `-0.087` n `8`; equity avg `-0.1357` n `113`; fx avg `-0.0045` n `6`; index avg `-0.0197` n `25`; metal avg `-0.0179` n `20`; unknown avg `-0.116` n `785`
- 4h: commodity avg `-0.0071` n `12`; crypto_alt avg `-0.4044` n `230`; crypto_major avg `-0.3771` n `8`; equity avg `-0.4586` n `113`; fx avg `-0.0048` n `6`; index avg `-0.0308` n `25`; metal avg `0.002` n `20`; unknown avg `1.4868` n `785`
- 24h: commodity avg `0.797` n `12`; crypto_alt avg `-0.2858` n `230`; crypto_major avg `-0.4051` n `8`; equity avg `-1.7778` n `113`; fx avg `0.2662` n `6`; index avg `-0.0891` n `25`; metal avg `0.3645` n `20`; unknown avg `103.6601` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1909`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1811`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1808`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1731`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1531`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1416`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
