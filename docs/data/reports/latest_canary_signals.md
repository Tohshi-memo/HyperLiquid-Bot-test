# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T23:22:30.889829+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0106` n `12`; crypto_alt avg `0.0797` n `230`; crypto_major avg `0.1087` n `8`; equity avg `0.0313` n `120`; fx avg `-0.0031` n `6`; index avg `0.0168` n `25`; metal avg `-0.0168` n `20`; unknown avg `-0.1177` n `789`
- 1h: commodity avg `0.0207` n `12`; crypto_alt avg `0.0288` n `230`; crypto_major avg `0.0918` n `8`; equity avg `-0.2579` n `120`; fx avg `-0.0049` n `6`; index avg `-0.0125` n `25`; metal avg `-0.0045` n `20`; unknown avg `-0.1809` n `789`
- 4h: commodity avg `0.115` n `12`; crypto_alt avg `-0.228` n `230`; crypto_major avg `-0.0724` n `8`; equity avg `-0.3494` n `120`; fx avg `-0.007` n `6`; index avg `-0.0319` n `25`; metal avg `-0.18` n `20`; unknown avg `-0.183` n `789`
- 24h: commodity avg `0.3172` n `12`; crypto_alt avg `-0.4795` n `230`; crypto_major avg `0.1241` n `8`; equity avg `-4.6527` n `120`; fx avg `-0.0282` n `6`; index avg `-0.697` n `25`; metal avg `-0.833` n `20`; unknown avg `-0.2248` n `755`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
