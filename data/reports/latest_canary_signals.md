# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T00:07:28.460509+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0139` n `12`; crypto_alt avg `-0.0663` n `230`; crypto_major avg `0.0447` n `8`; equity avg `0.0106` n `121`; fx avg `0.0153` n `6`; index avg `-0.0025` n `25`; metal avg `-0.0029` n `20`; unknown avg `-0.004` n `794`
- 1h: commodity avg `-0.0343` n `12`; crypto_alt avg `0.032` n `230`; crypto_major avg `0.2406` n `8`; equity avg `0.0783` n `121`; fx avg `0.022` n `6`; index avg `0.0104` n `25`; metal avg `0.0083` n `20`; unknown avg `0.0747` n `794`
- 4h: commodity avg `0.0727` n `12`; crypto_alt avg `-1.123` n `230`; crypto_major avg `-0.7713` n `8`; equity avg `0.0882` n `121`; fx avg `0.058` n `6`; index avg `0.0109` n `25`; metal avg `-0.0017` n `20`; unknown avg `0.2467` n `794`
- 24h: commodity avg `0.059` n `12`; crypto_alt avg `-1.6622` n `230`; crypto_major avg `1.2712` n `8`; equity avg `-0.3237` n `121`; fx avg `0.122` n `6`; index avg `-0.0619` n `25`; metal avg `-0.0761` n `20`; unknown avg `3.076` n `777`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
