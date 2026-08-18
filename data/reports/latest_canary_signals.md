# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T01:22:24.838341+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0115` n `12`; crypto_alt avg `-0.0569` n `230`; crypto_major avg `0.0049` n `8`; equity avg `-0.0098` n `114`; fx avg `0.0007` n `6`; index avg `-0.0114` n `25`; metal avg `-0.0737` n `20`; unknown avg `-0.0511` n `793`
- 1h: commodity avg `-0.0043` n `12`; crypto_alt avg `-0.0135` n `230`; crypto_major avg `-0.1387` n `8`; equity avg `-0.1122` n `114`; fx avg `-0.0204` n `6`; index avg `-0.0079` n `25`; metal avg `-0.0367` n `20`; unknown avg `0.0414` n `793`
- 4h: commodity avg `-0.008` n `12`; crypto_alt avg `-0.2892` n `230`; crypto_major avg `0.0668` n `8`; equity avg `0.1194` n `114`; fx avg `-0.0572` n `6`; index avg `-0.0131` n `25`; metal avg `0.0646` n `20`; unknown avg `-0.1629` n `792`
- 24h: commodity avg `0.6312` n `12`; crypto_alt avg `-0.0399` n `230`; crypto_major avg `0.8651` n `8`; equity avg `0.9416` n `114`; fx avg `0.0127` n `6`; index avg `0.0229` n `25`; metal avg `-0.0331` n `20`; unknown avg `0.2023` n `776`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.22`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1666`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1565`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1511`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.139`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
