# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T10:37:31.673500+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.069` n `12`; crypto_alt avg `0.0481` n `230`; crypto_major avg `0.0592` n `8`; equity avg `0.1524` n `114`; fx avg `0.0168` n `6`; index avg `0.0184` n `25`; metal avg `0.0441` n `20`; unknown avg `0.0096` n `795`
- 1h: commodity avg `-0.0305` n `12`; crypto_alt avg `0.0194` n `230`; crypto_major avg `0.0785` n `8`; equity avg `0.0158` n `114`; fx avg `-0.0114` n `6`; index avg `0.0082` n `25`; metal avg `0.0651` n `20`; unknown avg `0.0235` n `795`
- 4h: commodity avg `-0.179` n `12`; crypto_alt avg `0.0441` n `230`; crypto_major avg `-0.2818` n `8`; equity avg `-1.0664` n `114`; fx avg `-0.0249` n `6`; index avg `-0.1141` n `25`; metal avg `-0.069` n `20`; unknown avg `-0.0043` n `793`
- 24h: commodity avg `0.4806` n `12`; crypto_alt avg `-0.775` n `230`; crypto_major avg `-0.0744` n `8`; equity avg `-2.7594` n `114`; fx avg `-0.0451` n `6`; index avg `-0.5432` n `25`; metal avg `-0.2199` n `20`; unknown avg `-0.0046` n `760`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1433`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1329`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
