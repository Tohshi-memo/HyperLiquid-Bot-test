# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T10:22:31.106319+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0105` n `12`; crypto_alt avg `0.191` n `234`; crypto_major avg `0.1762` n `8`; equity avg `0.0128` n `140`; fx avg `0.001` n `6`; index avg `0.0054` n `26`; metal avg `0.0055` n `20`; unknown avg `-0.0201` n `942`
- 1h: commodity avg `-0.0081` n `12`; crypto_alt avg `0.3464` n `234`; crypto_major avg `-0.141` n `8`; equity avg `0.0241` n `140`; fx avg `0.0056` n `6`; index avg `0.0048` n `26`; metal avg `0.0059` n `20`; unknown avg `0.0559` n `940`
- 4h: commodity avg `-0.012` n `12`; crypto_alt avg `1.5555` n `234`; crypto_major avg `0.2929` n `8`; equity avg `0.0647` n `140`; fx avg `0.0127` n `6`; index avg `0.0263` n `26`; metal avg `0.0028` n `20`; unknown avg `0.5268` n `934`
- 24h: commodity avg `0.1748` n `12`; crypto_alt avg `3.1942` n `234`; crypto_major avg `3.4132` n `8`; equity avg `0.2247` n `140`; fx avg `-0.0243` n `6`; index avg `-0.0119` n `26`; metal avg `-0.1553` n `20`; unknown avg `2.4572` n `803`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1672`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.166`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.157`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1444`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1359`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1354`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.131`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1301`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
