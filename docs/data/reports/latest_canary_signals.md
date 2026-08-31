# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T11:52:32.539200+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0248` n `12`; crypto_alt avg `-0.1276` n `232`; crypto_major avg `-0.1676` n `8`; equity avg `-0.0532` n `128`; fx avg `-0.0077` n `6`; index avg `-0.0095` n `26`; metal avg `-0.0207` n `20`; unknown avg `0.0178` n `794`
- 1h: commodity avg `0.1293` n `12`; crypto_alt avg `-0.3557` n `232`; crypto_major avg `-0.4154` n `8`; equity avg `-0.1367` n `128`; fx avg `-0.0149` n `6`; index avg `-0.0221` n `26`; metal avg `0.0255` n `20`; unknown avg `0.2327` n `792`
- 4h: commodity avg `0.4383` n `12`; crypto_alt avg `-0.2145` n `232`; crypto_major avg `0.1832` n `8`; equity avg `-0.3178` n `128`; fx avg `-0.0413` n `6`; index avg `-0.0585` n `26`; metal avg `0.0692` n `20`; unknown avg `0.1841` n `791`
- 24h: commodity avg `0.7576` n `12`; crypto_alt avg `-0.5451` n `231`; crypto_major avg `-1.0768` n `8`; equity avg `-0.5496` n `128`; fx avg `-0.1468` n `6`; index avg `-0.0982` n `26`; metal avg `-0.1489` n `20`; unknown avg `0.0367` n `761`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0657`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0557`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0474`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0469`, n `668`, weak_sample_signal
