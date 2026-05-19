# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T05:52:16.684401+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0197` n `12`; crypto_alt avg `-0.0633` n `228`; crypto_major avg `0.0085` n `8`; equity avg `0.023` n `66`; fx avg `0.0013` n `6`; index avg `-0.0111` n `23`; metal avg `-0.0971` n `18`; unknown avg `-0.0438` n `383`
- 1h: commodity avg `0.1762` n `12`; crypto_alt avg `-0.1647` n `228`; crypto_major avg `-0.1211` n `8`; equity avg `0.0176` n `66`; fx avg `0.014` n `6`; index avg `0.0851` n `23`; metal avg `-0.1983` n `18`; unknown avg `-0.1154` n `383`
- 4h: commodity avg `0.2295` n `12`; crypto_alt avg `0.1608` n `228`; crypto_major avg `0.155` n `8`; equity avg `-0.1299` n `66`; fx avg `0.0596` n `6`; index avg `-0.1302` n `23`; metal avg `-0.9411` n `18`; unknown avg `-0.2919` n `383`
- 24h: commodity avg `0.4568` n `12`; crypto_alt avg `1.1548` n `228`; crypto_major avg `0.4755` n `8`; equity avg `-0.9744` n `66`; fx avg `0.286` n `6`; index avg `-0.4533` n `23`; metal avg `0.2725` n `18`; unknown avg `0.6826` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.2017`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1741`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1365`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1327`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
