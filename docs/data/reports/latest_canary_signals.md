# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T05:07:19.625388+00:00`
- Correlation status: `ready`
- Asset price records: `520`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.36` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0498` n `12`; crypto_alt avg `0.2953` n `228`; crypto_major avg `0.0818` n `8`; equity avg `0.0685` n `65`; fx avg `0.0031` n `4`; index avg `0.0137` n `23`; metal avg `0.1134` n `18`; unknown avg `1.0123` n `358`
- 1h: commodity avg `0.0259` n `12`; crypto_alt avg `1.1661` n `228`; crypto_major avg `0.3806` n `8`; equity avg `0.1439` n `65`; fx avg `-0.0411` n `4`; index avg `0.0285` n `23`; metal avg `0.1016` n `18`; unknown avg `1.313` n `358`
- 4h: commodity avg `-0.2399` n `12`; crypto_alt avg `0.8943` n `228`; crypto_major avg `-0.0044` n `8`; equity avg `0.6191` n `65`; fx avg `0.0105` n `4`; index avg `0.1918` n `23`; metal avg `0.1654` n `18`; unknown avg `0.8593` n `357`
- 24h: commodity avg `-1.7018` n `7`; crypto_alt avg `1.2543` n `223`; crypto_major avg `-0.8443` n `7`; equity avg `1.3668` n `47`; fx avg `0.0067` n `4`; index avg `1.0783` n `6`; metal avg `1.5542` n `7`; unknown avg `2.9836` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1187`, n `516`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.108`, n `516`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0901`, n `516`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0754`, n `516`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.074`, n `512`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0714`, n `512`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0714`, n `512`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0674`, n `512`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0666`, n `516`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0665`, n `512`, weak_sample_signal
