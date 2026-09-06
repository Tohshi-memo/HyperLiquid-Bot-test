# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T23:52:29.012475+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0115` n `12`; crypto_alt avg `0.0383` n `232`; crypto_major avg `-0.0368` n `8`; equity avg `0.013` n `134`; fx avg `0.0088` n `6`; index avg `0.0128` n `26`; metal avg `-0.0098` n `20`; unknown avg `1.11` n `790`
- 1h: commodity avg `0.0174` n `12`; crypto_alt avg `0.44` n `232`; crypto_major avg `0.389` n `8`; equity avg `-0.0418` n `134`; fx avg `0.0209` n `6`; index avg `-0.0144` n `26`; metal avg `-0.0385` n `20`; unknown avg `-0.1839` n `788`
- 4h: commodity avg `-0.0097` n `12`; crypto_alt avg `0.8964` n `232`; crypto_major avg `0.7968` n `8`; equity avg `-0.0769` n `134`; fx avg `0.0465` n `6`; index avg `-0.0139` n `26`; metal avg `-0.0733` n `20`; unknown avg `0.0656` n `767`
- 24h: commodity avg `0.0013` n `12`; crypto_alt avg `1.6376` n `232`; crypto_major avg `1.0438` n `8`; equity avg `0.2057` n `134`; fx avg `0.0574` n `6`; index avg `-0.0009` n `26`; metal avg `-0.0914` n `20`; unknown avg `150.8477` n `676`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.181`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
