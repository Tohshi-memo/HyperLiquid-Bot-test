# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T08:52:28.203578+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0445` n `12`; crypto_alt avg `-0.0202` n `230`; crypto_major avg `0.0625` n `8`; equity avg `0.1132` n `120`; fx avg `0.011` n `6`; index avg `0.0004` n `25`; metal avg `-0.021` n `20`; unknown avg `-0.0157` n `789`
- 1h: commodity avg `0.0112` n `12`; crypto_alt avg `0.1741` n `230`; crypto_major avg `0.2539` n `8`; equity avg `0.2104` n `120`; fx avg `-0.0214` n `6`; index avg `0.0695` n `25`; metal avg `0.0329` n `20`; unknown avg `-0.0099` n `789`
- 4h: commodity avg `-0.0279` n `12`; crypto_alt avg `0.4241` n `230`; crypto_major avg `0.3405` n `8`; equity avg `1.4353` n `120`; fx avg `-0.0279` n `6`; index avg `0.2908` n `25`; metal avg `0.0969` n `20`; unknown avg `0.0937` n `757`
- 24h: commodity avg `0.3195` n `12`; crypto_alt avg `0.3652` n `230`; crypto_major avg `0.3582` n `8`; equity avg `-1.3176` n `120`; fx avg `-0.2047` n `6`; index avg `-0.1543` n `25`; metal avg `-0.4292` n `20`; unknown avg `-0.2272` n `757`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.146`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
