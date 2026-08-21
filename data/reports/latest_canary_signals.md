# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T21:11:03.924535+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0062` n `12`; crypto_alt avg `0.4124` n `230`; crypto_major avg `0.4833` n `8`; equity avg `-0.009` n `121`; fx avg `0.004` n `6`; index avg `-0.0002` n `25`; metal avg `0.0289` n `20`; unknown avg `-0.0509` n `793`
- 1h: commodity avg `0.0464` n `12`; crypto_alt avg `1.0944` n `230`; crypto_major avg `1.1525` n `8`; equity avg `0.0325` n `121`; fx avg `-0.0049` n `6`; index avg `-0.0068` n `25`; metal avg `-0.0441` n `20`; unknown avg `-0.1285` n `793`
- 4h: commodity avg `-0.0561` n `12`; crypto_alt avg `0.1467` n `230`; crypto_major avg `0.2318` n `8`; equity avg `-0.0607` n `121`; fx avg `0.0029` n `6`; index avg `-0.0537` n `25`; metal avg `-0.1145` n `20`; unknown avg `-0.4093` n `793`
- 24h: commodity avg `0.144` n `12`; crypto_alt avg `7.7581` n `230`; crypto_major avg `5.4941` n `8`; equity avg `0.9526` n `121`; fx avg `-0.1003` n `6`; index avg `0.0928` n `25`; metal avg `0.5346` n `20`; unknown avg `1.185` n `777`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2153`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1876`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1868`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1788`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
