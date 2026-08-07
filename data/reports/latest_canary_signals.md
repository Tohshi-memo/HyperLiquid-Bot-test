# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T04:22:32.039807+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0826` n `12`; crypto_alt avg `0.0484` n `230`; crypto_major avg `-0.0295` n `8`; equity avg `0.0557` n `112`; fx avg `-0.0013` n `6`; index avg `0.0452` n `25`; metal avg `-0.0062` n `20`; unknown avg `-0.0527` n `782`
- 1h: commodity avg `0.0863` n `12`; crypto_alt avg `-0.0855` n `230`; crypto_major avg `-0.1628` n `8`; equity avg `0.0231` n `112`; fx avg `-0.0167` n `6`; index avg `0.0492` n `25`; metal avg `0.0697` n `20`; unknown avg `-0.2671` n `782`
- 4h: commodity avg `0.0828` n `12`; crypto_alt avg `-0.1203` n `230`; crypto_major avg `-0.1855` n `8`; equity avg `0.3831` n `112`; fx avg `-0.0457` n `6`; index avg `-0.0274` n `25`; metal avg `0.1886` n `20`; unknown avg `-0.2033` n `782`
- 24h: commodity avg `0.813` n `12`; crypto_alt avg `0.124` n `230`; crypto_major avg `-1.0328` n `8`; equity avg `0.6737` n `109`; fx avg `0.0277` n `6`; index avg `-0.1194` n `25`; metal avg `0.0113` n `20`; unknown avg `113.1151` n `749`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1646`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1296`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
