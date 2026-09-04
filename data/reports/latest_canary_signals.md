# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T07:07:31.021139+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0679` n `12`; crypto_alt avg `0.2844` n `232`; crypto_major avg `0.3088` n `8`; equity avg `0.0305` n `133`; fx avg `0.0245` n `6`; index avg `-0.0047` n `26`; metal avg `0.0924` n `20`; unknown avg `0.012` n `791`
- 1h: commodity avg `0.0655` n `12`; crypto_alt avg `0.2345` n `232`; crypto_major avg `0.0116` n `8`; equity avg `-0.223` n `133`; fx avg `0.0098` n `6`; index avg `-0.0382` n `26`; metal avg `0.0076` n `20`; unknown avg `-0.104` n `789`
- 4h: commodity avg `0.0205` n `12`; crypto_alt avg `-0.6273` n `232`; crypto_major avg `-0.2512` n `8`; equity avg `-0.0251` n `133`; fx avg `-0.0269` n `6`; index avg `0.0179` n `26`; metal avg `-0.0076` n `20`; unknown avg `0.4777` n `755`
- 24h: commodity avg `0.0447` n `12`; crypto_alt avg `1.7058` n `232`; crypto_major avg `3.5944` n `8`; equity avg `1.6379` n `133`; fx avg `0.002` n `6`; index avg `0.32` n `26`; metal avg `0.4959` n `20`; unknown avg `1.5242` n `730`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
