# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T21:19:29.271476+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0183` n `12`; crypto_alt avg `-0.1257` n `230`; crypto_major avg `-0.0551` n `8`; equity avg `-0.0142` n `114`; fx avg `-0.0111` n `6`; index avg `0.0021` n `25`; metal avg `0.013` n `20`; unknown avg `-0.0147` n `791`
- 1h: commodity avg `0.0096` n `12`; crypto_alt avg `-0.0419` n `230`; crypto_major avg `-0.0478` n `8`; equity avg `0.0032` n `114`; fx avg `-0.0157` n `6`; index avg `-0.0066` n `25`; metal avg `0.0349` n `20`; unknown avg `0.0046` n `791`
- 4h: commodity avg `-0.0715` n `12`; crypto_alt avg `-0.2883` n `230`; crypto_major avg `-0.4079` n `8`; equity avg `0.0179` n `114`; fx avg `0.0159` n `6`; index avg `0.0263` n `25`; metal avg `-0.0252` n `20`; unknown avg `-0.3151` n `791`
- 24h: commodity avg `0.1704` n `12`; crypto_alt avg `0.0892` n `230`; crypto_major avg `-1.0527` n `8`; equity avg `-0.5001` n `114`; fx avg `0.0783` n `6`; index avg `-0.0884` n `25`; metal avg `0.2109` n `20`; unknown avg `-0.0323` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2165`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1883`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1816`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1571`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1551`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1524`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1477`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1473`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1408`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1351`, n `668`, weak_sample_signal
