# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T14:52:25.531907+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0075` n `12`; crypto_alt avg `0.2285` n `232`; crypto_major avg `0.1791` n `8`; equity avg `-0.0184` n `134`; fx avg `0.0108` n `6`; index avg `-0.0184` n `26`; metal avg `0.023` n `20`; unknown avg `1.8314` n `792`
- 1h: commodity avg `0.0369` n `12`; crypto_alt avg `-0.7502` n `232`; crypto_major avg `-0.4382` n `8`; equity avg `-0.1641` n `134`; fx avg `0.0018` n `6`; index avg `-0.0437` n `26`; metal avg `-0.0027` n `20`; unknown avg `1.8474` n `790`
- 4h: commodity avg `0.0219` n `12`; crypto_alt avg `-0.7863` n `232`; crypto_major avg `-0.4447` n `8`; equity avg `-0.2724` n `134`; fx avg `0.0067` n `6`; index avg `-0.0517` n `26`; metal avg `-0.0021` n `20`; unknown avg `68.2203` n `720`
- 24h: commodity avg `0.1242` n `12`; crypto_alt avg `1.1595` n `232`; crypto_major avg `0.8529` n `8`; equity avg `0.2398` n `134`; fx avg `-0.0187` n `6`; index avg `0.0173` n `26`; metal avg `0.0066` n `20`; unknown avg `1.4726` n `664`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1322`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
