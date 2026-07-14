# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T04:07:29.466868+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0421` n `12`; crypto_alt avg `0.107` n `230`; crypto_major avg `0.1096` n `8`; equity avg `0.1008` n `92`; fx avg `0.0114` n `6`; index avg `0.026` n `25`; metal avg `0.0231` n `20`; unknown avg `-0.0395` n `766`
- 1h: commodity avg `0.022` n `12`; crypto_alt avg `0.1505` n `230`; crypto_major avg `0.1536` n `8`; equity avg `0.2841` n `92`; fx avg `-0.0105` n `6`; index avg `0.1158` n `25`; metal avg `0.0477` n `20`; unknown avg `-0.085` n `766`
- 4h: commodity avg `-0.0619` n `12`; crypto_alt avg `0.2874` n `230`; crypto_major avg `0.299` n `8`; equity avg `0.19` n `92`; fx avg `-0.085` n `6`; index avg `0.1055` n `25`; metal avg `0.2327` n `20`; unknown avg `0.0873` n `766`
- 24h: commodity avg `1.045` n `12`; crypto_alt avg `-0.1677` n `230`; crypto_major avg `-0.6331` n `8`; equity avg `-1.3005` n `92`; fx avg `-0.2244` n `6`; index avg `-0.2479` n `25`; metal avg `0.0482` n `20`; unknown avg `-0.2595` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1958`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1866`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1202`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
