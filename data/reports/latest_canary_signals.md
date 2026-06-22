# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T06:07:31.436092+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.018` n `12`; crypto_alt avg `-0.0813` n `228`; crypto_major avg `-0.0009` n `8`; equity avg `0.0315` n `79`; fx avg `-0.0321` n `6`; index avg `0.0096` n `23`; metal avg `0.0304` n `18`; unknown avg `0.2709` n `669`
- 1h: commodity avg `-0.0313` n `12`; crypto_alt avg `-0.1711` n `228`; crypto_major avg `-0.0504` n `8`; equity avg `-0.0008` n `79`; fx avg `-0.0347` n `6`; index avg `0.0203` n `23`; metal avg `0.3208` n `18`; unknown avg `1.2162` n `669`
- 4h: commodity avg `-0.0999` n `12`; crypto_alt avg `-0.6026` n `228`; crypto_major avg `-0.7074` n `8`; equity avg `-0.1828` n `79`; fx avg `-0.049` n `6`; index avg `-0.0547` n `23`; metal avg `0.1814` n `18`; unknown avg `0.451` n `669`
- 24h: commodity avg `-0.3923` n `12`; crypto_alt avg `0.0401` n `228`; crypto_major avg `-0.5136` n `8`; equity avg `-0.5789` n `79`; fx avg `-0.0341` n `6`; index avg `-0.0181` n `23`; metal avg `0.4511` n `18`; unknown avg `-0.2903` n `643`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0638`, n `668`, weak_sample_signal
