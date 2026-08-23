# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T03:12:33.339362+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- news_risk_spike: score `70.5` - News risk is high; compare crypto drawdown vs metal/index behavior.

## Class Returns

- 15m: commodity avg `-0.0313` n `12`; crypto_alt avg `-0.7243` n `230`; crypto_major avg `-0.3994` n `8`; equity avg `-0.0273` n `121`; fx avg `-0.0016` n `6`; index avg `-0.0008` n `25`; metal avg `0.0029` n `20`; unknown avg `-0.0703` n `794`
- 1h: commodity avg `-0.0306` n `12`; crypto_alt avg `-0.7903` n `230`; crypto_major avg `-0.6172` n `8`; equity avg `-0.0192` n `121`; fx avg `0.0085` n `6`; index avg `0.0032` n `25`; metal avg `-0.0031` n `20`; unknown avg `0.1552` n `794`
- 4h: commodity avg `-0.0546` n `12`; crypto_alt avg `-1.3455` n `230`; crypto_major avg `0.0231` n `8`; equity avg `0.1879` n `121`; fx avg `0.0302` n `6`; index avg `0.0315` n `25`; metal avg `0.0388` n `20`; unknown avg `2.2912` n `794`
- 24h: commodity avg `0.0518` n `12`; crypto_alt avg `-6.1846` n `230`; crypto_major avg `-2.5864` n `8`; equity avg `-0.2976` n `121`; fx avg `0.1047` n `6`; index avg `-0.0407` n `25`; metal avg `-0.0212` n `20`; unknown avg `3.2259` n `777`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1396`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
