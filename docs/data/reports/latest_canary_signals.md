# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T17:22:28.076521+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0056` n `12`; crypto_alt avg `0.1263` n `230`; crypto_major avg `0.1268` n `8`; equity avg `0.0066` n `121`; fx avg `-0.0001` n `6`; index avg `-0.0005` n `25`; metal avg `0.0032` n `20`; unknown avg `-0.0084` n `794`
- 1h: commodity avg `0.0021` n `12`; crypto_alt avg `0.3814` n `230`; crypto_major avg `0.4758` n `8`; equity avg `0.0175` n `121`; fx avg `0.0002` n `6`; index avg `-0.0073` n `25`; metal avg `-0.001` n `20`; unknown avg `0.0988` n `794`
- 4h: commodity avg `-0.0005` n `12`; crypto_alt avg `0.4736` n `230`; crypto_major avg `0.2948` n `8`; equity avg `-0.0199` n `121`; fx avg `0.0055` n `6`; index avg `-0.0052` n `25`; metal avg `0.0124` n `20`; unknown avg `0.2577` n `794`
- 24h: commodity avg `-0.0981` n `12`; crypto_alt avg `1.2895` n `230`; crypto_major avg `3.3908` n `8`; equity avg `-0.3572` n `121`; fx avg `0.0525` n `6`; index avg `-0.0569` n `25`; metal avg `-0.1424` n `20`; unknown avg `1.6811` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1507`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
