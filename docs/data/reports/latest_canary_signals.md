# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T14:37:28.888763+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0077` n `12`; crypto_alt avg `0.3077` n `230`; crypto_major avg `0.0245` n `8`; equity avg `0.0086` n `121`; fx avg `0.0069` n `6`; index avg `-0.0049` n `25`; metal avg `-0.0009` n `20`; unknown avg `0.0248` n `794`
- 1h: commodity avg `-0.0185` n `12`; crypto_alt avg `-0.0271` n `230`; crypto_major avg `-0.059` n `8`; equity avg `0.016` n `121`; fx avg `-0.0165` n `6`; index avg `-0.0062` n `25`; metal avg `-0.01` n `20`; unknown avg `0.0276` n `794`
- 4h: commodity avg `-0.0796` n `12`; crypto_alt avg `0.1425` n `230`; crypto_major avg `0.0897` n `8`; equity avg `0.0279` n `121`; fx avg `-0.0222` n `6`; index avg `0.001` n `25`; metal avg `0.0158` n `20`; unknown avg `0.1202` n `794`
- 24h: commodity avg `-0.0866` n `12`; crypto_alt avg `0.6369` n `230`; crypto_major avg `2.6533` n `8`; equity avg `-0.1728` n `121`; fx avg `0.0531` n `6`; index avg `-0.0023` n `25`; metal avg `-0.0393` n `20`; unknown avg `1.3028` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.156`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1464`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
