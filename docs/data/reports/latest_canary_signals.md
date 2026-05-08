# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T22:52:15.591229+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0443` n `12`; crypto_alt avg `0.0446` n `228`; crypto_major avg `0.0009` n `8`; equity avg `0.0377` n `65`; fx avg `0.0` n `5`; index avg `-0.002` n `23`; metal avg `-0.1053` n `18`; unknown avg `-0.0985` n `375`
- 1h: commodity avg `-0.0824` n `12`; crypto_alt avg `0.2156` n `228`; crypto_major avg `0.103` n `8`; equity avg `0.1015` n `65`; fx avg `-0.0015` n `5`; index avg `0.0434` n `23`; metal avg `-0.1524` n `18`; unknown avg `0.0032` n `375`
- 4h: commodity avg `-0.2922` n `12`; crypto_alt avg `0.531` n `228`; crypto_major avg `0.0194` n `8`; equity avg `0.7865` n `65`; fx avg `-0.0087` n `5`; index avg `0.1158` n `23`; metal avg `-0.2907` n `18`; unknown avg `-0.3219` n `375`
- 24h: commodity avg `-0.7738` n `12`; crypto_alt avg `4.0569` n `228`; crypto_major avg `1.9371` n `8`; equity avg `4.5372` n `65`; fx avg `0.2145` n `5`; index avg `1.7384` n `23`; metal avg `1.1374` n `18`; unknown avg `0.9692` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0655`, n `668`, weak_sample_signal
