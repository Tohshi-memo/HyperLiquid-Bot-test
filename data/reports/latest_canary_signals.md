# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T01:52:25.165433+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0226` n `12`; crypto_alt avg `-0.2668` n `230`; crypto_major avg `-0.1997` n `8`; equity avg `-0.6983` n `114`; fx avg `-0.0227` n `6`; index avg `-0.0983` n `25`; metal avg `-0.1741` n `20`; unknown avg `0.2987` n `793`
- 1h: commodity avg `0.0506` n `12`; crypto_alt avg `-0.4023` n `230`; crypto_major avg `-0.3498` n `8`; equity avg `-0.9819` n `114`; fx avg `-0.0247` n `6`; index avg `-0.1498` n `25`; metal avg `-0.2102` n `20`; unknown avg `0.4618` n `793`
- 4h: commodity avg `0.0244` n `12`; crypto_alt avg `-0.6608` n `230`; crypto_major avg `-0.2139` n `8`; equity avg `-0.8183` n `114`; fx avg `-0.0576` n `6`; index avg `-0.1379` n `25`; metal avg `-0.1215` n `20`; unknown avg `-0.1791` n `792`
- 24h: commodity avg `0.572` n `12`; crypto_alt avg `-0.3468` n `230`; crypto_major avg `0.5365` n `8`; equity avg `0.175` n `114`; fx avg `0.0058` n `6`; index avg `-0.0795` n `25`; metal avg `-0.1095` n `20`; unknown avg `0.2391` n `776`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.2366`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1711`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1623`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1461`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1445`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
