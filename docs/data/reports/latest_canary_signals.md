# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T05:22:10.663299+00:00`
- Correlation status: `ready`
- Asset price records: `521`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.38` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0384` n `12`; crypto_alt avg `0.1788` n `228`; crypto_major avg `0.0833` n `8`; equity avg `0.0858` n `65`; fx avg `0.0024` n `4`; index avg `0.028` n `23`; metal avg `-0.1192` n `18`; unknown avg `-0.155` n `358`
- 1h: commodity avg `-0.0317` n `12`; crypto_alt avg `0.8205` n `228`; crypto_major avg `0.2249` n `8`; equity avg `0.1313` n `65`; fx avg `0.0025` n `4`; index avg `0.0557` n `23`; metal avg `0.014` n `18`; unknown avg `0.3008` n `358`
- 4h: commodity avg `-0.092` n `12`; crypto_alt avg `1.2288` n `228`; crypto_major avg `0.0541` n `8`; equity avg `0.604` n `65`; fx avg `0.034` n `4`; index avg `0.1806` n `23`; metal avg `-0.3578` n `18`; unknown avg `-0.0524` n `357`
- 24h: commodity avg `-1.9726` n `7`; crypto_alt avg `1.5686` n `223`; crypto_major avg `-0.7046` n `7`; equity avg `1.4716` n `47`; fx avg `-0.0318` n `4`; index avg `1.1008` n `6`; metal avg `1.4174` n `7`; unknown avg `2.0153` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1185`, n `517`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1078`, n `517`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0871`, n `517`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0747`, n `513`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0727`, n `513`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0719`, n `517`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0716`, n `513`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0678`, n `513`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0667`, n `517`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0667`, n `513`, weak_sample_signal
