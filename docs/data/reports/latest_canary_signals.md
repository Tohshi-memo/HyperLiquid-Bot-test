# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T07:37:23.665299+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0267` n `12`; crypto_alt avg `-0.0325` n `232`; crypto_major avg `-0.0029` n `8`; equity avg `-0.0227` n `132`; fx avg `-0.0003` n `6`; index avg `-0.0098` n `26`; metal avg `0.0194` n `20`; unknown avg `0.0968` n `792`
- 1h: commodity avg `-0.1497` n `12`; crypto_alt avg `0.1726` n `232`; crypto_major avg `0.1229` n `8`; equity avg `0.1721` n `132`; fx avg `-0.0068` n `6`; index avg `0.0524` n `26`; metal avg `0.0764` n `20`; unknown avg `0.0654` n `790`
- 4h: commodity avg `-0.1132` n `12`; crypto_alt avg `0.2157` n `232`; crypto_major avg `-0.002` n `8`; equity avg `0.1233` n `132`; fx avg `-0.1059` n `6`; index avg `0.0057` n `26`; metal avg `0.287` n `20`; unknown avg `0.2207` n `770`
- 24h: commodity avg `0.6282` n `12`; crypto_alt avg `-0.6534` n `232`; crypto_major avg `-1.3815` n `8`; equity avg `-2.4507` n `130`; fx avg `-0.169` n `6`; index avg `-0.4401` n `26`; metal avg `-0.8034` n `20`; unknown avg `-0.5533` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0543`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.054`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0453`, n `668`, weak_sample_signal
