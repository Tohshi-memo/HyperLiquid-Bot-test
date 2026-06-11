# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T22:22:29.556143+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0526` n `12`; crypto_alt avg `-0.1241` n `228`; crypto_major avg `-0.0449` n `8`; equity avg `0.091` n `74`; fx avg `0.0001` n `6`; index avg `0.1895` n `23`; metal avg `-0.5092` n `18`; unknown avg `1.1083` n `556`
- 1h: commodity avg `-0.3453` n `12`; crypto_alt avg `-0.2733` n `228`; crypto_major avg `0.0239` n `8`; equity avg `0.215` n `74`; fx avg `-0.0495` n `6`; index avg `0.2667` n `23`; metal avg `0.0194` n `18`; unknown avg `0.6179` n `556`
- 4h: commodity avg `-0.6085` n `12`; crypto_alt avg `0.4599` n `228`; crypto_major avg `0.4424` n `8`; equity avg `1.5073` n `74`; fx avg `0.0167` n `6`; index avg `0.9879` n `23`; metal avg `1.0672` n `18`; unknown avg `0.9605` n `556`
- 24h: commodity avg `-2.8051` n `12`; crypto_alt avg `5.6742` n `228`; crypto_major avg `5.1415` n `8`; equity avg `4.8823` n `74`; fx avg `0.1276` n `6`; index avg `2.8482` n `23`; metal avg `4.263` n `18`; unknown avg `2.366` n `530`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1574`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
