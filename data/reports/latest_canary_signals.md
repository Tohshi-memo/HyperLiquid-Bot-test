# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T14:42:59.587531+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0117` n `12`; crypto_alt avg `-0.0511` n `230`; crypto_major avg `-0.4215` n `8`; equity avg `-0.0071` n `121`; fx avg `0.0105` n `6`; index avg `-0.0026` n `25`; metal avg `-0.0024` n `20`; unknown avg `-0.0222` n `794`
- 1h: commodity avg `0.0009` n `12`; crypto_alt avg `-0.3843` n `230`; crypto_major avg `-0.5035` n `8`; equity avg `0.0003` n `121`; fx avg `-0.0129` n `6`; index avg `-0.0039` n `25`; metal avg `-0.0114` n `20`; unknown avg `-0.0173` n `794`
- 4h: commodity avg `-0.0603` n `12`; crypto_alt avg `-0.2143` n `230`; crypto_major avg `-0.3547` n `8`; equity avg `0.0122` n `121`; fx avg `-0.0186` n `6`; index avg `0.0032` n `25`; metal avg `0.0144` n `20`; unknown avg `0.0709` n `794`
- 24h: commodity avg `-0.0673` n `12`; crypto_alt avg `0.273` n `230`; crypto_major avg `2.1861` n `8`; equity avg `-0.1884` n `121`; fx avg `0.0567` n `6`; index avg `0.0` n `25`; metal avg `-0.0407` n `20`; unknown avg `1.28` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1562`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1465`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1317`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
