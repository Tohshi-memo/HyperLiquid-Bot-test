# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T19:52:25.598748+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.58` - Polymarket crypto volume is unusually high.
- 1h_index_leads_crypto: score `1.0892` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0093` n `12`; crypto_alt avg `-0.5622` n `230`; crypto_major avg `-0.5296` n `8`; equity avg `-0.8985` n `102`; fx avg `0.0044` n `6`; index avg `-0.2508` n `25`; metal avg `-0.0942` n `20`; unknown avg `-0.166` n `778`
- 1h: commodity avg `0.0435` n `12`; crypto_alt avg `-1.5128` n `230`; crypto_major avg `-1.6955` n `8`; equity avg `-2.7212` n `102`; fx avg `0.0404` n `6`; index avg `-0.6063` n `25`; metal avg `-0.3374` n `20`; unknown avg `-0.0324` n `778`
- 4h: commodity avg `0.0967` n `12`; crypto_alt avg `-0.4247` n `230`; crypto_major avg `-0.5701` n `8`; equity avg `-0.5364` n `102`; fx avg `0.1017` n `6`; index avg `-0.1669` n `25`; metal avg `0.4116` n `20`; unknown avg `-0.4887` n `778`
- 24h: commodity avg `1.3913` n `12`; crypto_alt avg `-2.6911` n `230`; crypto_major avg `-1.0294` n `8`; equity avg `-2.8234` n `102`; fx avg `-0.0049` n `6`; index avg `-0.5825` n `25`; metal avg `0.2026` n `20`; unknown avg `-0.8177` n `760`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1617`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
