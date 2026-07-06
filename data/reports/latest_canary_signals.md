# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T02:52:28.606154+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.44` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0687` n `12`; crypto_alt avg `-0.1576` n `229`; crypto_major avg `-0.1767` n `8`; equity avg `-0.2352` n `88`; fx avg `-0.0017` n `6`; index avg `-0.0492` n `25`; metal avg `0.0148` n `20`; unknown avg `0.2532` n `765`
- 1h: commodity avg `-0.0486` n `12`; crypto_alt avg `-0.1491` n `229`; crypto_major avg `-0.2656` n `8`; equity avg `-0.5174` n `88`; fx avg `0.0156` n `6`; index avg `-0.1097` n `25`; metal avg `-0.2399` n `20`; unknown avg `-0.0156` n `765`
- 4h: commodity avg `-0.051` n `12`; crypto_alt avg `-0.436` n `229`; crypto_major avg `-0.3874` n `8`; equity avg `-1.6183` n `88`; fx avg `0.0592` n `6`; index avg `-0.2285` n `25`; metal avg `-0.3049` n `20`; unknown avg `-0.4955` n `765`
- 24h: commodity avg `-0.2447` n `12`; crypto_alt avg `0.8208` n `229`; crypto_major avg `1.8817` n `8`; equity avg `-1.181` n `88`; fx avg `0.0783` n `6`; index avg `-0.1808` n `25`; metal avg `-0.1073` n `20`; unknown avg `1.2326` n `663`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0633`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0562`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
