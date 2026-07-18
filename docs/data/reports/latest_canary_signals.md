# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T17:22:28.677358+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0572` n `12`; crypto_alt avg `-0.0264` n `230`; crypto_major avg `0.0247` n `8`; equity avg `0.021` n `96`; fx avg `0.0` n `6`; index avg `0.0067` n `25`; metal avg `-0.0009` n `20`; unknown avg `-0.0372` n `770`
- 1h: commodity avg `0.0427` n `12`; crypto_alt avg `0.1091` n `230`; crypto_major avg `0.1624` n `8`; equity avg `0.0389` n `96`; fx avg `-0.0111` n `6`; index avg `-0.0001` n `25`; metal avg `-0.0069` n `20`; unknown avg `0.0338` n `770`
- 4h: commodity avg `0.07` n `12`; crypto_alt avg `0.339` n `230`; crypto_major avg `0.5496` n `8`; equity avg `-0.0001` n `96`; fx avg `-0.0582` n `6`; index avg `-0.0178` n `25`; metal avg `-0.0411` n `20`; unknown avg `0.046` n `770`
- 24h: commodity avg `0.2922` n `12`; crypto_alt avg `-1.0719` n `230`; crypto_major avg `-0.1515` n `8`; equity avg `-1.5907` n `96`; fx avg `-0.1126` n `6`; index avg `-0.1399` n `25`; metal avg `-0.0423` n `20`; unknown avg `-0.1234` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
