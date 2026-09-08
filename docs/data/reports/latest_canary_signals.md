# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T10:07:28.420522+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0111` n `12`; crypto_alt avg `-0.0318` n `232`; crypto_major avg `0.0115` n `8`; equity avg `0.0068` n `134`; fx avg `0.0054` n `6`; index avg `0.0015` n `26`; metal avg `0.0012` n `20`; unknown avg `0.271` n `795`
- 1h: commodity avg `-0.0914` n `12`; crypto_alt avg `0.7971` n `232`; crypto_major avg `0.5525` n `8`; equity avg `0.4312` n `134`; fx avg `-0.0298` n `6`; index avg `0.0739` n `26`; metal avg `0.0958` n `20`; unknown avg `0.3999` n `795`
- 4h: commodity avg `0.0812` n `12`; crypto_alt avg `0.7529` n `232`; crypto_major avg `0.576` n `8`; equity avg `0.0005` n `134`; fx avg `0.0198` n `6`; index avg `-0.0181` n `26`; metal avg `-0.0123` n `20`; unknown avg `0.6009` n `785`
- 24h: commodity avg `0.4574` n `12`; crypto_alt avg `1.2467` n `232`; crypto_major avg `-0.3692` n `8`; equity avg `-0.1292` n `134`; fx avg `-0.1049` n `6`; index avg `-0.0666` n `26`; metal avg `0.1313` n `20`; unknown avg `7462.2246` n `670`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
