# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T20:37:26.664299+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0101` n `12`; crypto_alt avg `0.0469` n `230`; crypto_major avg `0.1543` n `8`; equity avg `0.0142` n `121`; fx avg `-0.0062` n `6`; index avg `-0.0034` n `25`; metal avg `-0.0149` n `20`; unknown avg `-0.0271` n `793`
- 1h: commodity avg `0.0299` n `12`; crypto_alt avg `0.8267` n `230`; crypto_major avg `0.7247` n `8`; equity avg `0.0399` n `121`; fx avg `-0.0115` n `6`; index avg `-0.0095` n `25`; metal avg `-0.0194` n `20`; unknown avg `-0.2683` n `793`
- 4h: commodity avg `-0.0298` n `12`; crypto_alt avg `-0.2921` n `230`; crypto_major avg `0.097` n `8`; equity avg `-0.0219` n `121`; fx avg `0.0037` n `6`; index avg `-0.0373` n `25`; metal avg `-0.0684` n `20`; unknown avg `-0.2104` n `793`
- 24h: commodity avg `0.1274` n `12`; crypto_alt avg `7.0866` n `230`; crypto_major avg `5.054` n `8`; equity avg `0.9939` n `121`; fx avg `-0.0954` n `6`; index avg `0.101` n `25`; metal avg `0.5243` n `20`; unknown avg `1.0523` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2123`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1886`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1885`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1768`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
