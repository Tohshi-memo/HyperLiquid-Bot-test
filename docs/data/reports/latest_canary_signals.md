# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T04:29:19.866221+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0358` n `12`; crypto_alt avg `-0.0549` n `230`; crypto_major avg `0.009` n `8`; equity avg `-0.0354` n `113`; fx avg `-0.003` n `6`; index avg `-0.0073` n `25`; metal avg `-0.0032` n `20`; unknown avg `0.3147` n `786`
- 1h: commodity avg `0.0137` n `12`; crypto_alt avg `-0.1229` n `230`; crypto_major avg `0.0052` n `8`; equity avg `0.0179` n `113`; fx avg `-0.0299` n `6`; index avg `-0.0207` n `25`; metal avg `-0.0299` n `20`; unknown avg `0.1615` n `786`
- 4h: commodity avg `0.1032` n `12`; crypto_alt avg `0.1959` n `230`; crypto_major avg `0.1434` n `8`; equity avg `0.6615` n `113`; fx avg `0.0155` n `6`; index avg `0.1344` n `25`; metal avg `0.145` n `20`; unknown avg `-0.1175` n `786`
- 24h: commodity avg `0.3368` n `12`; crypto_alt avg `-1.1011` n `230`; crypto_major avg `0.55` n `8`; equity avg `1.6349` n `113`; fx avg `0.0313` n `6`; index avg `0.1216` n `25`; metal avg `-0.1277` n `20`; unknown avg `-0.112` n `753`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.224`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2234`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.215`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2074`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.2041`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
