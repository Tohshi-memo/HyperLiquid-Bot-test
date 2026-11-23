# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T03:07:37.029479+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0175` n `13`; crypto_alt avg `0.39` n `239`; crypto_major avg `0.4516` n `8`; equity avg `0.4908` n `166`; fx avg `-0.0066` n `6`; index avg `0.0321` n `27`; metal avg `0.0891` n `20`; unknown avg `-0.3126` n `1255`
- 1h: commodity avg `-0.0495` n `13`; crypto_alt avg `-0.0646` n `239`; crypto_major avg `0.1907` n `8`; equity avg `-0.4321` n `166`; fx avg `-0.0078` n `6`; index avg `-0.1149` n `27`; metal avg `0.0152` n `20`; unknown avg `158.7164` n `1259`
- 4h: commodity avg `-0.1538` n `13`; crypto_alt avg `-0.3577` n `239`; crypto_major avg `-0.3588` n `8`; equity avg `0.3218` n `166`; fx avg `0.0964` n `6`; index avg `0.0278` n `27`; metal avg `-0.0466` n `20`; unknown avg `160.6268` n `1242`
- 24h: commodity avg `-0.4413` n `13`; crypto_alt avg `1.1504` n `239`; crypto_major avg `1.6449` n `8`; equity avg `1.1811` n `166`; fx avg `0.1869` n `6`; index avg `0.1053` n `27`; metal avg `0.2229` n `20`; unknown avg `194.8265` n `1025`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1698`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1677`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.157`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1447`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.14`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1377`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1341`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1288`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
