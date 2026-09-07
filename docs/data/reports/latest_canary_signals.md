# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T02:07:26.924184+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0645` n `12`; crypto_alt avg `-0.1954` n `232`; crypto_major avg `-0.1475` n `8`; equity avg `0.0523` n `134`; fx avg `0.025` n `6`; index avg `0.0014` n `26`; metal avg `-0.0659` n `20`; unknown avg `-0.0477` n `792`
- 1h: commodity avg `0.0547` n `12`; crypto_alt avg `-0.7547` n `232`; crypto_major avg `-0.5652` n `8`; equity avg `0.036` n `134`; fx avg `0.1081` n `6`; index avg `0.0289` n `26`; metal avg `0.0142` n `20`; unknown avg `1.3598` n `792`
- 4h: commodity avg `-0.0012` n `12`; crypto_alt avg `-0.6545` n `232`; crypto_major avg `-0.3662` n `8`; equity avg `0.1181` n `134`; fx avg `-0.0261` n `6`; index avg `0.008` n `26`; metal avg `-0.0434` n `20`; unknown avg `1.6991` n `783`
- 24h: commodity avg `-0.0106` n `12`; crypto_alt avg `-0.5521` n `232`; crypto_major avg `-0.301` n `8`; equity avg `0.3535` n `134`; fx avg `0.0019` n `6`; index avg `0.0319` n `26`; metal avg `-0.1386` n `20`; unknown avg `151.1318` n `676`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1928`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
