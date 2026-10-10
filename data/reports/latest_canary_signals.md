# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T19:37:26.418903+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0056` n `13`; crypto_alt avg `0.0513` n `235`; crypto_major avg `0.0935` n `8`; equity avg `0.0167` n `150`; fx avg `-0.0016` n `6`; index avg `0.0018` n `26`; metal avg `0.002` n `20`; unknown avg `1.8277` n `1101`
- 1h: commodity avg `0.027` n `13`; crypto_alt avg `0.2157` n `235`; crypto_major avg `0.1815` n `8`; equity avg `0.0401` n `150`; fx avg `-0.0018` n `6`; index avg `0.002` n `26`; metal avg `0.0018` n `20`; unknown avg `0.9934` n `1027`
- 4h: commodity avg `0.0123` n `13`; crypto_alt avg `0.4458` n `235`; crypto_major avg `-0.0705` n `8`; equity avg `-0.0127` n `150`; fx avg `-0.0044` n `6`; index avg `-0.0209` n `26`; metal avg `-0.0191` n `20`; unknown avg `1.7727` n `1007`
- 24h: commodity avg `-0.1385` n `13`; crypto_alt avg `3.4136` n `235`; crypto_major avg `1.3631` n `8`; equity avg `0.2793` n `150`; fx avg `-0.0018` n `6`; index avg `0.0208` n `26`; metal avg `-0.0213` n `20`; unknown avg `2.676` n `928`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1535`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1439`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
