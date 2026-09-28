# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T16:07:33.528921+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1651` n `12`; crypto_alt avg `0.342` n `234`; crypto_major avg `0.2656` n `8`; equity avg `0.2265` n `141`; fx avg `-0.0102` n `6`; index avg `0.0305` n `26`; metal avg `0.0208` n `20`; unknown avg `1.3198` n `954`
- 1h: commodity avg `-0.1823` n `12`; crypto_alt avg `0.7303` n `234`; crypto_major avg `0.7245` n `8`; equity avg `0.2576` n `141`; fx avg `-0.0192` n `6`; index avg `0.0293` n `26`; metal avg `0.0045` n `20`; unknown avg `2.5162` n `954`
- 4h: commodity avg `-0.1487` n `12`; crypto_alt avg `-1.3167` n `234`; crypto_major avg `-0.6289` n `8`; equity avg `-1.0625` n `141`; fx avg `0.0527` n `6`; index avg `-0.1737` n `26`; metal avg `-0.3223` n `20`; unknown avg `46.7281` n `904`
- 24h: commodity avg `-0.1508` n `12`; crypto_alt avg `-3.2761` n `234`; crypto_major avg `-1.8503` n `8`; equity avg `-3.3629` n `141`; fx avg `0.0298` n `6`; index avg `-0.3576` n `26`; metal avg `-1.0887` n `20`; unknown avg `5.2948` n `786`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1994`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1844`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1647`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.152`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1445`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1292`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1285`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
