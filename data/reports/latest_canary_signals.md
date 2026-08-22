# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T16:22:24.964083+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0007` n `12`; crypto_alt avg `0.5058` n `230`; crypto_major avg `0.4393` n `8`; equity avg `0.0331` n `121`; fx avg `0.0098` n `6`; index avg `0.0047` n `25`; metal avg `0.0029` n `20`; unknown avg `0.0757` n `794`
- 1h: commodity avg `0.0145` n `12`; crypto_alt avg `1.1139` n `230`; crypto_major avg `0.8699` n `8`; equity avg `0.0537` n `121`; fx avg `0.0213` n `6`; index avg `0.0041` n `25`; metal avg `0.0167` n `20`; unknown avg `0.2885` n `794`
- 4h: commodity avg `-0.0472` n `12`; crypto_alt avg `-0.6431` n `230`; crypto_major avg `-0.7905` n `8`; equity avg `-0.0768` n `121`; fx avg `0.0018` n `6`; index avg `-0.0027` n `25`; metal avg `0.023` n `20`; unknown avg `0.0497` n `794`
- 24h: commodity avg `-0.0144` n `12`; crypto_alt avg `0.6107` n `230`; crypto_major avg `2.7254` n `8`; equity avg `-0.5647` n `121`; fx avg `0.0582` n `6`; index avg `-0.0676` n `25`; metal avg `-0.1108` n `20`; unknown avg `0.5987` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1533`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1469`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
