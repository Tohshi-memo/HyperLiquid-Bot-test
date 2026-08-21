# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T06:52:28.920153+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.028` n `12`; crypto_alt avg `0.0177` n `230`; crypto_major avg `-0.1623` n `8`; equity avg `0.043` n `121`; fx avg `0.0044` n `6`; index avg `0.0027` n `25`; metal avg `-0.0148` n `20`; unknown avg `-0.1027` n `793`
- 1h: commodity avg `0.0472` n `12`; crypto_alt avg `0.3185` n `230`; crypto_major avg `0.0302` n `8`; equity avg `0.312` n `121`; fx avg `0.0412` n `6`; index avg `0.0496` n `25`; metal avg `0.0611` n `20`; unknown avg `-0.2077` n `777`
- 4h: commodity avg `-0.0168` n `12`; crypto_alt avg `1.1503` n `230`; crypto_major avg `0.527` n `8`; equity avg `0.0215` n `121`; fx avg `0.0522` n `6`; index avg `0.0117` n `25`; metal avg `0.0479` n `20`; unknown avg `-0.1728` n `777`
- 24h: commodity avg `0.3071` n `12`; crypto_alt avg `6.1355` n `230`; crypto_major avg `6.6409` n `8`; equity avg `-0.5023` n `121`; fx avg `0.0395` n `6`; index avg `-0.0957` n `25`; metal avg `0.669` n `20`; unknown avg `2.1977` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.199`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1924`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1849`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
