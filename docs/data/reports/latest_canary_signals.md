# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T01:22:26.822502+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0073` n `13`; crypto_alt avg `-0.0006` n `235`; crypto_major avg `-0.0457` n `8`; equity avg `-0.0251` n `143`; fx avg `-0.0001` n `6`; index avg `-0.0025` n `26`; metal avg `0.003` n `20`; unknown avg `0.0096` n `1079`
- 1h: commodity avg `0.0364` n `13`; crypto_alt avg `-0.2782` n `235`; crypto_major avg `-0.1295` n `8`; equity avg `-0.0508` n `143`; fx avg `-0.0037` n `6`; index avg `-0.0064` n `26`; metal avg `0.0013` n `20`; unknown avg `0.0646` n `1077`
- 4h: commodity avg `-0.0609` n `13`; crypto_alt avg `0.1544` n `235`; crypto_major avg `0.0291` n `8`; equity avg `0.0219` n `143`; fx avg `0.0042` n `6`; index avg `-0.0011` n `26`; metal avg `0.0017` n `20`; unknown avg `-0.1402` n `1055`
- 24h: commodity avg `0.0387` n `13`; crypto_alt avg `1.27` n `235`; crypto_major avg `0.3575` n `8`; equity avg `0.1522` n `143`; fx avg `-0.0237` n `6`; index avg `0.0231` n `26`; metal avg `0.0133` n `20`; unknown avg `-0.0347` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.199`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1861`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1566`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1549`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1345`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1309`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1194`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1132`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
