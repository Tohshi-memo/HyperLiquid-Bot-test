# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T07:22:13.681998+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0244` n `12`; crypto_alt avg `0.346` n `230`; crypto_major avg `0.3879` n `8`; equity avg `0.1191` n `121`; fx avg `-0.0168` n `6`; index avg `0.0138` n `25`; metal avg `0.0211` n `20`; unknown avg `0.0367` n `793`
- 1h: commodity avg `0.0339` n `12`; crypto_alt avg `0.5406` n `230`; crypto_major avg `0.3758` n `8`; equity avg `0.4634` n `121`; fx avg `-0.0113` n `6`; index avg `0.0447` n `25`; metal avg `0.0718` n `20`; unknown avg `0.0218` n `793`
- 4h: commodity avg `0.0044` n `12`; crypto_alt avg `1.724` n `230`; crypto_major avg `1.5949` n `8`; equity avg `0.452` n `121`; fx avg `0.0295` n `6`; index avg `0.0473` n `25`; metal avg `0.1475` n `20`; unknown avg `0.0573` n `777`
- 24h: commodity avg `0.1706` n `12`; crypto_alt avg `6.8072` n `230`; crypto_major avg `7.4436` n `8`; equity avg `-0.0689` n `121`; fx avg `-0.0193` n `6`; index avg `-0.0406` n `25`; metal avg `0.7553` n `20`; unknown avg `2.326` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2028`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1931`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1852`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
