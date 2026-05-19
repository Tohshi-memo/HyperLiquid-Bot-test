# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T12:37:38.327034+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.061` n `12`; crypto_alt avg `0.0457` n `228`; crypto_major avg `0.0602` n `8`; equity avg `0.1676` n `66`; fx avg `0.0046` n `6`; index avg `0.128` n `23`; metal avg `0.032` n `18`; unknown avg `-0.0904` n `383`
- 1h: commodity avg `-0.235` n `12`; crypto_alt avg `-0.0025` n `228`; crypto_major avg `-0.0605` n `8`; equity avg `-0.0532` n `66`; fx avg `-0.0023` n `6`; index avg `0.002` n `23`; metal avg `0.0412` n `18`; unknown avg `-0.1724` n `383`
- 4h: commodity avg `0.1133` n `12`; crypto_alt avg `-0.8847` n `228`; crypto_major avg `-0.52` n `8`; equity avg `-0.566` n `66`; fx avg `-0.0563` n `6`; index avg `-0.2634` n `23`; metal avg `-0.1473` n `18`; unknown avg `-0.8451` n `383`
- 24h: commodity avg `1.1797` n `12`; crypto_alt avg `-0.1719` n `228`; crypto_major avg `-0.4383` n `8`; equity avg `-2.0957` n `66`; fx avg `0.2231` n `6`; index avg `-0.9594` n `23`; metal avg `-0.7289` n `18`; unknown avg `0.1858` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1913`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1527`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1198`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
