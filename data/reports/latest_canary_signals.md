# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T11:07:30.613222+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0101` n `12`; crypto_alt avg `0.0637` n `228`; crypto_major avg `-0.0665` n `8`; equity avg `0.0934` n `88`; fx avg `-0.0012` n `6`; index avg `0.0222` n `23`; metal avg `0.1636` n `20`; unknown avg `0.3217` n `765`
- 1h: commodity avg `-0.0259` n `12`; crypto_alt avg `-0.0603` n `228`; crypto_major avg `-0.5469` n `8`; equity avg `0.1786` n `88`; fx avg `0.0108` n `6`; index avg `0.0445` n `23`; metal avg `0.121` n `20`; unknown avg `-0.0267` n `765`
- 4h: commodity avg `-0.1362` n `12`; crypto_alt avg `0.6156` n `228`; crypto_major avg `-0.3205` n `8`; equity avg `0.4049` n `88`; fx avg `0.0442` n `6`; index avg `0.0718` n `23`; metal avg `0.4385` n `20`; unknown avg `0.2583` n `765`
- 24h: commodity avg `-0.3997` n `12`; crypto_alt avg `-0.1857` n `228`; crypto_major avg `-1.1385` n `8`; equity avg `0.563` n `88`; fx avg `0.1403` n `6`; index avg `0.0059` n `23`; metal avg `-0.6428` n `20`; unknown avg `0.0721` n `743`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
