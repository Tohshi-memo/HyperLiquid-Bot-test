# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T18:37:28.311441+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0326` n `12`; crypto_alt avg `0.0858` n `234`; crypto_major avg `0.1365` n `8`; equity avg `0.0108` n `140`; fx avg `0.0007` n `6`; index avg `-0.0025` n `26`; metal avg `0.0035` n `20`; unknown avg `0.0825` n `943`
- 1h: commodity avg `0.0256` n `12`; crypto_alt avg `0.0574` n `234`; crypto_major avg `0.0963` n `8`; equity avg `0.0588` n `140`; fx avg `-0.0182` n `6`; index avg `0.0125` n `26`; metal avg `0.0135` n `20`; unknown avg `0.1895` n `941`
- 4h: commodity avg `-0.0985` n `12`; crypto_alt avg `-0.1049` n `234`; crypto_major avg `-0.2218` n `8`; equity avg `0.0474` n `140`; fx avg `-0.0096` n `6`; index avg `0.025` n `26`; metal avg `0.0012` n `20`; unknown avg `5.6838` n `882`
- 24h: commodity avg `-0.0289` n `12`; crypto_alt avg `2.2726` n `234`; crypto_major avg `0.7659` n `8`; equity avg `0.5366` n `140`; fx avg `0.0156` n `6`; index avg `0.1191` n `26`; metal avg `-0.0954` n `20`; unknown avg `3.8563` n `792`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1747`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1727`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1685`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1589`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1546`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1429`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1334`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1292`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.128`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
