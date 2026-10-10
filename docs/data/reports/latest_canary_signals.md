# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T23:52:27.108714+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0339` n `13`; crypto_alt avg `0.0366` n `235`; crypto_major avg `0.0077` n `8`; equity avg `-0.0013` n `150`; fx avg `-0.0104` n `6`; index avg `0.0027` n `26`; metal avg `0.0012` n `20`; unknown avg `2.554` n `1117`
- 1h: commodity avg `0.0335` n `13`; crypto_alt avg `0.0406` n `235`; crypto_major avg `-0.022` n `8`; equity avg `-0.0178` n `150`; fx avg `0.0038` n `6`; index avg `-0.0014` n `26`; metal avg `0.0028` n `20`; unknown avg `1.0546` n `1115`
- 4h: commodity avg `0.2037` n `13`; crypto_alt avg `0.1127` n `235`; crypto_major avg `-0.0904` n `8`; equity avg `0.0093` n `150`; fx avg `0.0007` n `6`; index avg `0.0094` n `26`; metal avg `0.0152` n `20`; unknown avg `3.8264` n `1071`
- 24h: commodity avg `0.0563` n `13`; crypto_alt avg `1.7879` n `235`; crypto_major avg `0.6879` n `8`; equity avg `0.1727` n `150`; fx avg `-0.003` n `6`; index avg `0.0228` n `26`; metal avg `0.008` n `20`; unknown avg `0.2675` n `942`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1528`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
