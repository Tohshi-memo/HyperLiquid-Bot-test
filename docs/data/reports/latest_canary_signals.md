# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T13:52:29.264621+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0183` n `12`; crypto_alt avg `-0.0907` n `233`; crypto_major avg `-0.0449` n `8`; equity avg `0.0` n `136`; fx avg `-0.0018` n `6`; index avg `0.0002` n `26`; metal avg `0.0072` n `20`; unknown avg `0.1686` n `838`
- 1h: commodity avg `-0.0105` n `12`; crypto_alt avg `-0.1632` n `233`; crypto_major avg `-0.0236` n `8`; equity avg `-0.0402` n `136`; fx avg `-0.0001` n `6`; index avg `0.0005` n `26`; metal avg `0.0041` n `20`; unknown avg `0.0579` n `836`
- 4h: commodity avg `-0.0377` n `12`; crypto_alt avg `0.0189` n `233`; crypto_major avg `0.1925` n `8`; equity avg `0.0352` n `136`; fx avg `-0.0039` n `6`; index avg `0.002` n `26`; metal avg `0.0403` n `20`; unknown avg `1.0197` n `824`
- 24h: commodity avg `-0.1003` n `12`; crypto_alt avg `-0.3284` n `233`; crypto_major avg `-1.523` n `8`; equity avg `-0.1969` n `136`; fx avg `0.0142` n `6`; index avg `0.0476` n `26`; metal avg `-0.2567` n `20`; unknown avg `9.4982` n `692`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0603`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0587`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0539`, n `668`, weak_sample_signal
