# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T00:52:27.001245+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.11` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0001` n `12`; crypto_alt avg `0.0224` n `228`; crypto_major avg `0.0771` n `8`; equity avg `-0.0104` n `88`; fx avg `0.038` n `6`; index avg `-0.0021` n `23`; metal avg `-0.0576` n `20`; unknown avg `-0.0397` n `765`
- 1h: commodity avg `-0.023` n `12`; crypto_alt avg `0.0931` n `228`; crypto_major avg `-0.0386` n `8`; equity avg `-0.2433` n `88`; fx avg `0.0747` n `6`; index avg `-0.021` n `23`; metal avg `-0.098` n `20`; unknown avg `-0.1409` n `765`
- 4h: commodity avg `-0.007` n `12`; crypto_alt avg `0.0329` n `228`; crypto_major avg `-0.1097` n `8`; equity avg `-0.0387` n `88`; fx avg `0.0771` n `6`; index avg `-0.0064` n `23`; metal avg `-0.1734` n `20`; unknown avg `-0.831` n `765`
- 24h: commodity avg `0.1469` n `12`; crypto_alt avg `-1.5301` n `228`; crypto_major avg `-1.3628` n `8`; equity avg `1.4977` n `88`; fx avg `0.1331` n `6`; index avg `0.3635` n `23`; metal avg `0.0356` n `20`; unknown avg `6.7739` n `735`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0556`, n `668`, weak_sample_signal
