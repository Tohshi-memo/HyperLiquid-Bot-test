# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T19:07:28.503681+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0251` n `13`; crypto_alt avg `-0.0278` n `235`; crypto_major avg `-0.0445` n `8`; equity avg `0.0013` n `150`; fx avg `0.0` n `6`; index avg `-0.0028` n `26`; metal avg `0.0109` n `20`; unknown avg `-0.0112` n `1083`
- 1h: commodity avg `0.0214` n `13`; crypto_alt avg `0.1268` n `235`; crypto_major avg `-0.0207` n `8`; equity avg `-0.0001` n `150`; fx avg `0.0011` n `6`; index avg `-0.0084` n `26`; metal avg `0.0092` n `20`; unknown avg `3.3441` n `1043`
- 4h: commodity avg `0.0022` n `13`; crypto_alt avg `0.1994` n `235`; crypto_major avg `-0.3301` n `8`; equity avg `-0.0379` n `150`; fx avg `-0.005` n `6`; index avg `-0.0212` n `26`; metal avg `-0.0144` n `20`; unknown avg `1.3818` n `1023`
- 24h: commodity avg `-0.1492` n `13`; crypto_alt avg `2.7848` n `235`; crypto_major avg `0.9277` n `8`; equity avg `0.1745` n `150`; fx avg `-0.0166` n `6`; index avg `-0.0046` n `26`; metal avg `-0.0619` n `20`; unknown avg `1.0` n `944`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1544`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1445`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
