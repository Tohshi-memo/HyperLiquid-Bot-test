# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T16:50:18.322831+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0166` n `12`; crypto_alt avg `0.0033` n `230`; crypto_major avg `-0.0287` n `8`; equity avg `0.0002` n `114`; fx avg `-0.0085` n `6`; index avg `-0.0131` n `25`; metal avg `-0.006` n `20`; unknown avg `0.1004` n `792`
- 1h: commodity avg `0.0181` n `12`; crypto_alt avg `-0.138` n `230`; crypto_major avg `-0.1115` n `8`; equity avg `-0.0202` n `114`; fx avg `0.0018` n `6`; index avg `-0.0262` n `25`; metal avg `-0.0117` n `20`; unknown avg `0.2241` n `792`
- 4h: commodity avg `0.0164` n `12`; crypto_alt avg `0.154` n `230`; crypto_major avg `0.5564` n `8`; equity avg `0.8899` n `114`; fx avg `0.031` n `6`; index avg `0.0866` n `25`; metal avg `0.2091` n `20`; unknown avg `0.174` n `792`
- 24h: commodity avg `0.0356` n `12`; crypto_alt avg `-0.1134` n `230`; crypto_major avg `0.8151` n `8`; equity avg `1.6829` n `114`; fx avg `0.0169` n `6`; index avg `0.1759` n `25`; metal avg `0.2906` n `20`; unknown avg `0.1107` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1641`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1567`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1462`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1331`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
