# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T05:53:00.523145+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0337` n `12`; crypto_alt avg `-0.0003` n `230`; crypto_major avg `0.012` n `8`; equity avg `0.1219` n `114`; fx avg `-0.0067` n `6`; index avg `0.0217` n `25`; metal avg `0.013` n `20`; unknown avg `-0.1403` n `792`
- 1h: commodity avg `-0.0747` n `12`; crypto_alt avg `-0.1155` n `230`; crypto_major avg `-0.034` n `8`; equity avg `0.2382` n `114`; fx avg `0.0081` n `6`; index avg `0.04` n `25`; metal avg `0.058` n `20`; unknown avg `-0.3691` n `792`
- 4h: commodity avg `-0.1258` n `12`; crypto_alt avg `0.4068` n `230`; crypto_major avg `0.3716` n `8`; equity avg `0.8019` n `114`; fx avg `0.0391` n `6`; index avg `0.0979` n `25`; metal avg `0.0396` n `20`; unknown avg `0.3642` n `792`
- 24h: commodity avg `-0.2182` n `12`; crypto_alt avg `0.3791` n `230`; crypto_major avg `0.732` n `8`; equity avg `0.9714` n `114`; fx avg `-0.0215` n `6`; index avg `0.124` n `25`; metal avg `0.2319` n `20`; unknown avg `0.0126` n `759`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1735`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1716`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1479`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1424`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
