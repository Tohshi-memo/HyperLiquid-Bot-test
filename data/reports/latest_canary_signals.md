# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T00:37:26.698047+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0012` n `12`; crypto_alt avg `0.5098` n `230`; crypto_major avg `0.4932` n `8`; equity avg `0.0565` n `121`; fx avg `0.0052` n `6`; index avg `0.0038` n `25`; metal avg `0.0082` n `20`; unknown avg `0.1389` n `794`
- 1h: commodity avg `-0.0111` n `12`; crypto_alt avg `0.9588` n `230`; crypto_major avg `1.3063` n `8`; equity avg `0.1148` n `121`; fx avg `0.0078` n `6`; index avg `0.0022` n `25`; metal avg `0.0103` n `20`; unknown avg `0.5512` n `794`
- 4h: commodity avg `0.0317` n `12`; crypto_alt avg `-0.416` n `230`; crypto_major avg `-0.0862` n `8`; equity avg `0.1455` n `121`; fx avg `0.0441` n `6`; index avg `0.0175` n `25`; metal avg `0.0123` n `20`; unknown avg `0.4352` n `794`
- 24h: commodity avg `0.0895` n `12`; crypto_alt avg `-1.9849` n `230`; crypto_major avg `1.407` n `8`; equity avg `-0.2848` n `121`; fx avg `0.1189` n `6`; index avg `-0.0547` n `25`; metal avg `-0.0591` n `20`; unknown avg `3.1599` n `777`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
