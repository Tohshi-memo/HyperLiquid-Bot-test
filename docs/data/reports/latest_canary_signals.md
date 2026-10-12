# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T03:37:25.970337+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.068` n `13`; crypto_alt avg `0.1248` n `235`; crypto_major avg `0.029` n `8`; equity avg `0.0242` n `151`; fx avg `-0.006` n `6`; index avg `0.0018` n `26`; metal avg `-0.0015` n `20`; unknown avg `0.003` n `1133`
- 1h: commodity avg `0.0236` n `13`; crypto_alt avg `0.0244` n `235`; crypto_major avg `-0.1632` n `8`; equity avg `-0.0738` n `151`; fx avg `-0.0197` n `6`; index avg `-0.019` n `26`; metal avg `-0.0555` n `20`; unknown avg `0.2193` n `1131`
- 4h: commodity avg `-0.2293` n `13`; crypto_alt avg `0.0632` n `235`; crypto_major avg `0.1472` n `8`; equity avg `-0.7143` n `151`; fx avg `-0.0911` n `6`; index avg `-0.0812` n `26`; metal avg `0.0464` n `20`; unknown avg `0.3632` n `1097`
- 24h: commodity avg `-0.4844` n `13`; crypto_alt avg `2.8495` n `235`; crypto_major avg `1.1982` n `8`; equity avg `-0.1872` n `151`; fx avg `-0.08` n `6`; index avg `0.0223` n `26`; metal avg `0.1499` n `20`; unknown avg `0.9079` n `928`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0509`, n `668`, weak_sample_signal
