# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T07:07:29.418386+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0164` n `12`; crypto_alt avg `0.2336` n `232`; crypto_major avg `0.2692` n `8`; equity avg `0.1674` n `134`; fx avg `0.014` n `6`; index avg `0.0372` n `26`; metal avg `0.0529` n `20`; unknown avg `0.6063` n `795`
- 1h: commodity avg `0.0657` n `12`; crypto_alt avg `-0.2728` n `232`; crypto_major avg `-0.0841` n `8`; equity avg `0.0278` n `134`; fx avg `0.0653` n `6`; index avg `-0.0003` n `26`; metal avg `0.0251` n `20`; unknown avg `0.4749` n `793`
- 4h: commodity avg `0.2484` n `12`; crypto_alt avg `-0.1041` n `232`; crypto_major avg `-0.1246` n `8`; equity avg `-0.5444` n `134`; fx avg `0.1377` n `6`; index avg `-0.1691` n `26`; metal avg `-0.0509` n `20`; unknown avg `2.2697` n `747`
- 24h: commodity avg `0.349` n `12`; crypto_alt avg `0.2314` n `232`; crypto_major avg `-1.2557` n `8`; equity avg `-0.1813` n `134`; fx avg `-0.157` n `6`; index avg `-0.0764` n `26`; metal avg `0.2067` n `20`; unknown avg `7508.6639` n `666`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
