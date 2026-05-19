# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T14:14:44.433680+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0062` n `12`; crypto_alt avg `-0.498` n `228`; crypto_major avg `-0.4382` n `8`; equity avg `-0.8817` n `66`; fx avg `-0.0177` n `6`; index avg `-0.4494` n `23`; metal avg `-0.1505` n `18`; unknown avg `-0.129` n `383`
- 1h: commodity avg `0.2116` n `12`; crypto_alt avg `0.0043` n `228`; crypto_major avg `0.0311` n `8`; equity avg `-0.4775` n `66`; fx avg `-0.0375` n `6`; index avg `-0.5771` n `23`; metal avg `-0.54` n `18`; unknown avg `-0.1752` n `383`
- 4h: commodity avg `0.3435` n `12`; crypto_alt avg `-0.4185` n `228`; crypto_major avg `-0.1723` n `8`; equity avg `-0.8624` n `66`; fx avg `-0.0654` n `6`; index avg `-0.7162` n `23`; metal avg `-1.213` n `18`; unknown avg `-0.639` n `383`
- 24h: commodity avg `1.5562` n `12`; crypto_alt avg `0.3588` n `228`; crypto_major avg `0.1953` n `8`; equity avg `-2.3776` n `66`; fx avg `0.2043` n `6`; index avg `-1.575` n `23`; metal avg `-1.9922` n `18`; unknown avg `-0.7406` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.2311`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1818`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1302`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
