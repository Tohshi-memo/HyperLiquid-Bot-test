# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T08:07:31.339426+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0106` n `13`; crypto_alt avg `0.2436` n `235`; crypto_major avg `0.1344` n `8`; equity avg `0.019` n `150`; fx avg `0.0146` n `6`; index avg `0.0022` n `26`; metal avg `0.0057` n `20`; unknown avg `0.1132` n `1099`
- 1h: commodity avg `-0.0125` n `13`; crypto_alt avg `-0.027` n `235`; crypto_major avg `0.1563` n `8`; equity avg `-0.0101` n `150`; fx avg `0.0214` n `6`; index avg `-0.0152` n `26`; metal avg `0.0078` n `20`; unknown avg `0.1466` n `1099`
- 4h: commodity avg `0.0293` n `13`; crypto_alt avg `-0.051` n `235`; crypto_major avg `0.1767` n `8`; equity avg `-0.0916` n `150`; fx avg `0.0152` n `6`; index avg `-0.0264` n `26`; metal avg `-0.006` n `20`; unknown avg `0.3235` n `1082`
- 24h: commodity avg `0.0604` n `13`; crypto_alt avg `1.3205` n `235`; crypto_major avg `0.0164` n `8`; equity avg `-0.2392` n `150`; fx avg `-0.0637` n `6`; index avg `-0.0451` n `26`; metal avg `-0.0188` n `20`; unknown avg `640.5202` n `942`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1516`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
