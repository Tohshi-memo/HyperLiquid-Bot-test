# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T02:37:31.290452+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0018` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0114` n `12`; crypto_alt avg `0.1074` n `228`; crypto_major avg `0.0585` n `8`; equity avg `0.0853` n `88`; fx avg `-0.0016` n `6`; index avg `0.015` n `23`; metal avg `-0.0178` n `20`; unknown avg `0.1335` n `765`
- 1h: commodity avg `0.0044` n `12`; crypto_alt avg `-0.0569` n `228`; crypto_major avg `-0.197` n `8`; equity avg `0.2973` n `88`; fx avg `-0.0256` n `6`; index avg `0.0477` n `23`; metal avg `-0.1834` n `20`; unknown avg `-0.2223` n `763`
- 4h: commodity avg `0.0042` n `12`; crypto_alt avg `-0.7058` n `228`; crypto_major avg `-1.0156` n `8`; equity avg `0.0018` n `88`; fx avg `0.0313` n `6`; index avg `-0.0138` n `23`; metal avg `-0.546` n `20`; unknown avg `0.1085` n `763`
- 24h: commodity avg `-0.2021` n `12`; crypto_alt avg `0.3846` n `228`; crypto_major avg `1.4816` n `8`; equity avg `2.2777` n `88`; fx avg `0.1492` n `6`; index avg `0.301` n `23`; metal avg `-0.8235` n `20`; unknown avg `1.6224` n `728`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1285`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
