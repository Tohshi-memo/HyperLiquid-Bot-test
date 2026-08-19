# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T09:22:28.049668+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0146` n `12`; crypto_alt avg `-0.0648` n `230`; crypto_major avg `-0.0144` n `8`; equity avg `-0.1971` n `120`; fx avg `0.0068` n `6`; index avg `-0.0316` n `25`; metal avg `-0.007` n `20`; unknown avg `0.0696` n `791`
- 1h: commodity avg `0.1297` n `12`; crypto_alt avg `-0.0062` n `230`; crypto_major avg `0.1825` n `8`; equity avg `-0.2318` n `120`; fx avg `0.0031` n `6`; index avg `-0.0193` n `25`; metal avg `-0.0219` n `20`; unknown avg `-0.006` n `789`
- 4h: commodity avg `0.0871` n `12`; crypto_alt avg `0.232` n `230`; crypto_major avg `0.2829` n `8`; equity avg `1.0579` n `120`; fx avg `-0.0067` n `6`; index avg `0.2208` n `25`; metal avg `0.1119` n `20`; unknown avg `0.0216` n `757`
- 24h: commodity avg `0.4387` n `12`; crypto_alt avg `0.3136` n `230`; crypto_major avg `0.4522` n `8`; equity avg `-1.403` n `120`; fx avg `-0.1708` n `6`; index avg `-0.1507` n `25`; metal avg `-0.4354` n `20`; unknown avg `-0.2541` n `757`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1361`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
