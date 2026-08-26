# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T19:17:01.440712+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0234` n `12`; crypto_alt avg `-0.0762` n `231`; crypto_major avg `0.0445` n `8`; equity avg `0.0012` n `122`; fx avg `-0.0032` n `6`; index avg `-0.0059` n `25`; metal avg `-0.0031` n `20`; unknown avg `-0.0362` n `797`
- 1h: commodity avg `0.0241` n `12`; crypto_alt avg `-0.1137` n `231`; crypto_major avg `-0.0936` n `8`; equity avg `0.1743` n `122`; fx avg `-0.0087` n `6`; index avg `0.049` n `25`; metal avg `-0.0228` n `20`; unknown avg `-0.1263` n `797`
- 4h: commodity avg `0.0077` n `12`; crypto_alt avg `0.2538` n `231`; crypto_major avg `0.4218` n `8`; equity avg `0.3518` n `122`; fx avg `-0.0019` n `6`; index avg `0.0425` n `25`; metal avg `-0.1291` n `20`; unknown avg `0.0693` n `797`
- 24h: commodity avg `0.086` n `12`; crypto_alt avg `-1.8237` n `231`; crypto_major avg `-1.9619` n `8`; equity avg `0.0508` n `122`; fx avg `-0.057` n `6`; index avg `0.0796` n `25`; metal avg `-0.4325` n `20`; unknown avg `0.3852` n `779`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1483`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
