# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T08:52:33.642155+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.59` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0574` n `12`; crypto_alt avg `0.0626` n `230`; crypto_major avg `0.0933` n `8`; equity avg `0.1748` n `102`; fx avg `0.0126` n `6`; index avg `0.0854` n `25`; metal avg `0.0103` n `20`; unknown avg `0.044` n `777`
- 1h: commodity avg `-0.0718` n `12`; crypto_alt avg `-0.0217` n `230`; crypto_major avg `-0.1608` n `8`; equity avg `0.0512` n `102`; fx avg `0.0338` n `6`; index avg `0.0207` n `25`; metal avg `-0.0874` n `20`; unknown avg `-0.2939` n `777`
- 4h: commodity avg `-0.0626` n `12`; crypto_alt avg `0.4445` n `230`; crypto_major avg `0.6733` n `8`; equity avg `1.6684` n `102`; fx avg `0.1003` n `6`; index avg `0.4598` n `25`; metal avg `0.1073` n `20`; unknown avg `-0.1205` n `761`
- 24h: commodity avg `0.1483` n `12`; crypto_alt avg `-1.2852` n `230`; crypto_major avg `1.0346` n `8`; equity avg `-1.4308` n `102`; fx avg `-0.0951` n `6`; index avg `-0.1828` n `25`; metal avg `-0.0657` n `20`; unknown avg `-0.5668` n `758`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
