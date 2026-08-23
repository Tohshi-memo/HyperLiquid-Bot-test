# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T02:52:25.234232+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- news_risk_spike: score `70.5` - News risk is high; compare crypto drawdown vs metal/index behavior.

## Class Returns

- 15m: commodity avg `0.01` n `12`; crypto_alt avg `0.1242` n `230`; crypto_major avg `0.0216` n `8`; equity avg `0.0114` n `121`; fx avg `0.0112` n `6`; index avg `-0.0009` n `25`; metal avg `0.0025` n `20`; unknown avg `-0.0199` n `794`
- 1h: commodity avg `0.023` n `12`; crypto_alt avg `-0.3385` n `230`; crypto_major avg `-0.3546` n `8`; equity avg `0.0123` n `121`; fx avg `0.0215` n `6`; index avg `0.0055` n `25`; metal avg `0.0002` n `20`; unknown avg `0.0774` n `794`
- 4h: commodity avg `-0.0213` n `12`; crypto_alt avg `-0.5818` n `230`; crypto_major avg `0.5519` n `8`; equity avg `0.218` n `121`; fx avg `0.0381` n `6`; index avg `0.0322` n `25`; metal avg `0.0305` n `20`; unknown avg `2.7005` n `794`
- 24h: commodity avg `0.0765` n `12`; crypto_alt avg `-5.1778` n `230`; crypto_major avg `-1.939` n `8`; equity avg `-0.269` n `121`; fx avg `0.1092` n `6`; index avg `-0.0365` n `25`; metal avg `-0.0167` n `20`; unknown avg `3.4387` n `777`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1358`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
