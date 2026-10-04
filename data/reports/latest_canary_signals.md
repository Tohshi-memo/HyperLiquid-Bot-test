# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T17:52:26.827170+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0188` n `13`; crypto_alt avg `0.0371` n `235`; crypto_major avg `0.1278` n `8`; equity avg `0.0011` n `144`; fx avg `-0.0165` n `6`; index avg `0.003` n `26`; metal avg `-0.0004` n `20`; unknown avg `0.1392` n `1078`
- 1h: commodity avg `0.0824` n `13`; crypto_alt avg `-0.0753` n `235`; crypto_major avg `0.1294` n `8`; equity avg `-0.0034` n `144`; fx avg `-0.0037` n `6`; index avg `-0.0007` n `26`; metal avg `0.0018` n `20`; unknown avg `0.0202` n `1076`
- 4h: commodity avg `-0.0404` n `13`; crypto_alt avg `-0.0213` n `235`; crypto_major avg `0.2985` n `8`; equity avg `0.0129` n `144`; fx avg `-0.002` n `6`; index avg `-0.0203` n `26`; metal avg `-0.0025` n `20`; unknown avg `-0.0253` n `1070`
- 24h: commodity avg `0.042` n `13`; crypto_alt avg `0.6686` n `235`; crypto_major avg `0.9062` n `8`; equity avg `0.2079` n `144`; fx avg `0.0207` n `6`; index avg `-0.0187` n `26`; metal avg `-0.0003` n `20`; unknown avg `0.1144` n `1019`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.204`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1768`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1698`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1529`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.148`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
