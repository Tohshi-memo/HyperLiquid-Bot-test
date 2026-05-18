# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T23:22:16.945275+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0001` n `12`; crypto_alt avg `-0.0205` n `228`; crypto_major avg `-0.0555` n `8`; equity avg `-0.0399` n `66`; fx avg `-0.0083` n `6`; index avg `-0.015` n `23`; metal avg `0.0296` n `18`; unknown avg `-0.0198` n `383`
- 1h: commodity avg `0.0188` n `12`; crypto_alt avg `-0.1514` n `228`; crypto_major avg `-0.2312` n `8`; equity avg `0.1906` n `66`; fx avg `-0.0208` n `6`; index avg `0.0112` n `23`; metal avg `0.4042` n `18`; unknown avg `-0.3976` n `383`
- 4h: commodity avg `0.0495` n `12`; crypto_alt avg `1.5119` n `228`; crypto_major avg `1.1797` n `8`; equity avg `1.1575` n `66`; fx avg `-0.028` n `6`; index avg `0.5748` n `23`; metal avg `0.8888` n `18`; unknown avg `0.0336` n `383`
- 24h: commodity avg `0.6845` n `12`; crypto_alt avg `-0.1326` n `228`; crypto_major avg `-0.8225` n `8`; equity avg `-0.3853` n `66`; fx avg `0.1604` n `6`; index avg `-0.0766` n `23`; metal avg `1.1208` n `18`; unknown avg `-0.0561` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1641`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1526`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1416`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
