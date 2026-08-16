# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T17:07:27.559676+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0101` n `12`; crypto_alt avg `0.0143` n `230`; crypto_major avg `0.0645` n `8`; equity avg `0.0058` n `114`; fx avg `0.0012` n `6`; index avg `-0.0053` n `25`; metal avg `0.0061` n `20`; unknown avg `-0.0277` n `791`
- 1h: commodity avg `0.0134` n `12`; crypto_alt avg `-0.0811` n `230`; crypto_major avg `0.1561` n `8`; equity avg `0.0432` n `114`; fx avg `-0.0011` n `6`; index avg `0.0042` n `25`; metal avg `0.0186` n `20`; unknown avg `-0.0612` n `791`
- 4h: commodity avg `0.0089` n `12`; crypto_alt avg `0.0472` n `230`; crypto_major avg `0.3381` n `8`; equity avg `0.1465` n `114`; fx avg `0.003` n `6`; index avg `-0.0007` n `25`; metal avg `0.0174` n `20`; unknown avg `-0.0149` n `791`
- 24h: commodity avg `0.0696` n `12`; crypto_alt avg `-0.2619` n `230`; crypto_major avg `0.1423` n `8`; equity avg `0.3641` n `114`; fx avg `-0.0023` n `6`; index avg `0.0299` n `25`; metal avg `0.0584` n `20`; unknown avg `0.1879` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2145`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1849`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1672`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1595`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1587`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1558`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1526`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.139`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1326`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
