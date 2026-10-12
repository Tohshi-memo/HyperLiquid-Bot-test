# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T07:07:25.014288+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0635` n `13`; crypto_alt avg `0.0073` n `235`; crypto_major avg `0.1666` n `8`; equity avg `0.0031` n `151`; fx avg `-0.0155` n `6`; index avg `0.0062` n `26`; metal avg `0.0224` n `20`; unknown avg `-0.0908` n `1131`
- 1h: commodity avg `0.0128` n `13`; crypto_alt avg `-0.0334` n `235`; crypto_major avg `0.3042` n `8`; equity avg `-0.1153` n `151`; fx avg `-0.0233` n `6`; index avg `-0.0043` n `26`; metal avg `0.0384` n `20`; unknown avg `0.0905` n `1131`
- 4h: commodity avg `0.1949` n `13`; crypto_alt avg `0.3016` n `235`; crypto_major avg `0.6439` n `8`; equity avg `-0.4261` n `151`; fx avg `-0.0038` n `6`; index avg `-0.0777` n `26`; metal avg `-0.0577` n `20`; unknown avg `0.6435` n `1043`
- 24h: commodity avg `-0.3257` n `13`; crypto_alt avg `2.3282` n `235`; crypto_major avg `1.8669` n `8`; equity avg `-0.6306` n `151`; fx avg `-0.0702` n `6`; index avg `-0.0624` n `26`; metal avg `0.0937` n `20`; unknown avg `0.4381` n `866`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.2134`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.179`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
