# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T03:22:28.604526+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0834` n `13`; crypto_alt avg `-0.6398` n `235`; crypto_major avg `-0.2313` n `8`; equity avg `-0.05` n `150`; fx avg `0.0094` n `6`; index avg `-0.0064` n `26`; metal avg `-0.0024` n `20`; unknown avg `1.4064` n `1117`
- 1h: commodity avg `0.1178` n `13`; crypto_alt avg `-0.9598` n `235`; crypto_major avg `-0.3276` n `8`; equity avg `-0.0587` n `150`; fx avg `0.0021` n `6`; index avg `-0.009` n `26`; metal avg `-0.0029` n `20`; unknown avg `1.2392` n `1115`
- 4h: commodity avg `0.1641` n `13`; crypto_alt avg `-0.5529` n `235`; crypto_major avg `-0.2699` n `8`; equity avg `-0.0795` n `150`; fx avg `0.0139` n `6`; index avg `-0.0071` n `26`; metal avg `0.0056` n `20`; unknown avg `0.5182` n `1109`
- 24h: commodity avg `0.2079` n `13`; crypto_alt avg `0.4472` n `235`; crypto_major avg `0.1351` n `8`; equity avg `0.0131` n `150`; fx avg `-0.0025` n `6`; index avg `-0.0183` n `26`; metal avg `-0.0136` n `20`; unknown avg `0.3143` n `942`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1534`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
