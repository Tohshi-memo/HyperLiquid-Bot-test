# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T06:37:30.221720+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0135` n `12`; crypto_alt avg `-0.0207` n `230`; crypto_major avg `-0.0339` n `8`; equity avg `-0.1623` n `120`; fx avg `-0.0131` n `6`; index avg `-0.0024` n `25`; metal avg `0.0011` n `20`; unknown avg `0.0013` n `789`
- 1h: commodity avg `0.0054` n `12`; crypto_alt avg `-0.0573` n `230`; crypto_major avg `-0.0769` n `8`; equity avg `-0.3226` n `120`; fx avg `0.0352` n `6`; index avg `-0.0054` n `25`; metal avg `0.07` n `20`; unknown avg `-0.0287` n `757`
- 4h: commodity avg `0.01` n `12`; crypto_alt avg `0.1217` n `230`; crypto_major avg `-0.0011` n `8`; equity avg `-0.7295` n `120`; fx avg `-0.0488` n `6`; index avg `-0.0586` n `25`; metal avg `-0.0252` n `20`; unknown avg `-0.1329` n `757`
- 24h: commodity avg `0.2225` n `12`; crypto_alt avg `0.1119` n `230`; crypto_major avg `-0.2122` n `8`; equity avg `-3.6537` n `120`; fx avg `-0.1731` n `6`; index avg `-0.4874` n `25`; metal avg `-0.6237` n `20`; unknown avg `-0.2939` n `755`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1477`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
