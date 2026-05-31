# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T15:07:23.673753+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0053` n `12`; crypto_alt avg `-0.0758` n `228`; crypto_major avg `-0.0073` n `8`; equity avg `0.0215` n `69`; fx avg `0.0025` n `6`; index avg `-0.0443` n `23`; metal avg `-0.0092` n `18`; unknown avg `-0.0036` n `421`
- 1h: commodity avg `0.0459` n `12`; crypto_alt avg `-0.8222` n `228`; crypto_major avg `-0.4687` n `8`; equity avg `-0.0411` n `69`; fx avg `-0.0012` n `6`; index avg `-0.0424` n `23`; metal avg `-0.0115` n `18`; unknown avg `0.0718` n `421`
- 4h: commodity avg `0.1053` n `12`; crypto_alt avg `-1.1367` n `228`; crypto_major avg `-0.3697` n `8`; equity avg `0.0067` n `69`; fx avg `0.0082` n `6`; index avg `-0.0949` n `23`; metal avg `-0.0109` n `18`; unknown avg `-0.1944` n `421`
- 24h: commodity avg `0.1532` n `12`; crypto_alt avg `-1.1358` n `228`; crypto_major avg `0.1512` n `8`; equity avg `0.6672` n `69`; fx avg `-0.0225` n `6`; index avg `-0.3225` n `23`; metal avg `-0.0441` n `18`; unknown avg `0.2966` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.159`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
