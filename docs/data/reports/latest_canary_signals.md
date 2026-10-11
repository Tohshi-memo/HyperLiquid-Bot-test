# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T12:22:29.319365+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0226` n `13`; crypto_alt avg `-0.0795` n `235`; crypto_major avg `-0.0163` n `8`; equity avg `0.0219` n `150`; fx avg `-0.0157` n `6`; index avg `-0.0035` n `26`; metal avg `0.0026` n `20`; unknown avg `0.8175` n `1117`
- 1h: commodity avg `-0.0292` n `13`; crypto_alt avg `0.1655` n `235`; crypto_major avg `0.1752` n `8`; equity avg `0.1096` n `150`; fx avg `0.002` n `6`; index avg `0.0036` n `26`; metal avg `0.0086` n `20`; unknown avg `0.1541` n `1109`
- 4h: commodity avg `-0.0195` n `13`; crypto_alt avg `-0.03` n `235`; crypto_major avg `0.2174` n `8`; equity avg `0.147` n `150`; fx avg `0.0164` n `6`; index avg `0.0072` n `26`; metal avg `-0.0002` n `20`; unknown avg `0.5702` n `1109`
- 24h: commodity avg `0.4098` n `13`; crypto_alt avg `1.1021` n `235`; crypto_major avg `0.1749` n `8`; equity avg `0.1735` n `150`; fx avg `0.0139` n `6`; index avg `0.0022` n `26`; metal avg `0.0051` n `20`; unknown avg `0.3336` n `943`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1132`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
