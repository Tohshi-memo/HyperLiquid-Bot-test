# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T08:07:27.300231+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0589` n `12`; crypto_alt avg `0.0898` n `234`; crypto_major avg `0.1642` n `8`; equity avg `-0.1766` n `140`; fx avg `-0.0185` n `6`; index avg `-0.0254` n `26`; metal avg `-0.0078` n `20`; unknown avg `1.275` n `936`
- 1h: commodity avg `-0.0809` n `12`; crypto_alt avg `0.0304` n `234`; crypto_major avg `-0.1152` n `8`; equity avg `-0.201` n `140`; fx avg `0.0178` n `6`; index avg `-0.0457` n `26`; metal avg `-0.0694` n `20`; unknown avg `0.7771` n `936`
- 4h: commodity avg `-0.0251` n `12`; crypto_alt avg `-0.283` n `234`; crypto_major avg `-0.7299` n `8`; equity avg `-0.9395` n `140`; fx avg `0.0068` n `6`; index avg `-0.1406` n `26`; metal avg `-0.1999` n `20`; unknown avg `9.0113` n `908`
- 24h: commodity avg `-0.2133` n `12`; crypto_alt avg `2.6317` n `234`; crypto_major avg `3.4267` n `8`; equity avg `0.7842` n `140`; fx avg `-0.154` n `6`; index avg `0.2048` n `26`; metal avg `-0.2334` n `20`; unknown avg `1126.3885` n `792`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.138`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1375`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1305`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
