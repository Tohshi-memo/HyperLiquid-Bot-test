# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T09:52:23.327897+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0013` n `13`; crypto_alt avg `-0.0906` n `235`; crypto_major avg `-0.0307` n `8`; equity avg `-0.0064` n `150`; fx avg `0.0003` n `6`; index avg `0.0005` n `26`; metal avg `0.0006` n `20`; unknown avg `0.0563` n `1117`
- 1h: commodity avg `-0.0012` n `13`; crypto_alt avg `-0.187` n `235`; crypto_major avg `-0.0532` n `8`; equity avg `0.0086` n `150`; fx avg `0.0005` n `6`; index avg `0.0015` n `26`; metal avg `-0.0027` n `20`; unknown avg `0.0292` n `1115`
- 4h: commodity avg `0.0571` n `13`; crypto_alt avg `0.2354` n `235`; crypto_major avg `-0.0383` n `8`; equity avg `0.0553` n `150`; fx avg `0.0021` n `6`; index avg `0.0087` n `26`; metal avg `0.0121` n `20`; unknown avg `0.2066` n `1083`
- 24h: commodity avg `0.4188` n `13`; crypto_alt avg `1.0306` n `235`; crypto_major avg `-0.1852` n `8`; equity avg `0.0836` n `150`; fx avg `0.0012` n `6`; index avg `-0.0072` n `26`; metal avg `0.0069` n `20`; unknown avg `0.6925` n `943`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1519`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1202`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
