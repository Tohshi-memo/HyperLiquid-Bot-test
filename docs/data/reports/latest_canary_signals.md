# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T12:37:30.535387+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1011` n `12`; crypto_alt avg `-0.0736` n `230`; crypto_major avg `-0.1351` n `8`; equity avg `-0.2379` n `114`; fx avg `0.004` n `6`; index avg `-0.0346` n `25`; metal avg `-0.0314` n `20`; unknown avg `0.0029` n `792`
- 1h: commodity avg `0.1406` n `12`; crypto_alt avg `-0.1829` n `230`; crypto_major avg `-0.2975` n `8`; equity avg `-0.3021` n `114`; fx avg `0.0121` n `6`; index avg `-0.0384` n `25`; metal avg `-0.1289` n `20`; unknown avg `0.0365` n `792`
- 4h: commodity avg `0.1205` n `12`; crypto_alt avg `0.0869` n `230`; crypto_major avg `0.0077` n `8`; equity avg `-0.5421` n `114`; fx avg `0.0085` n `6`; index avg `-0.052` n `25`; metal avg `-0.1218` n `20`; unknown avg `0.0411` n `792`
- 24h: commodity avg `-0.0303` n `12`; crypto_alt avg `-0.0952` n `230`; crypto_major avg `0.6643` n `8`; equity avg `0.879` n `114`; fx avg `-0.0089` n `6`; index avg `0.0999` n `25`; metal avg `0.0795` n `20`; unknown avg `0.0638` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1682`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1593`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1456`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1411`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
