# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T23:07:28.546511+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1102` n `12`; crypto_alt avg `-0.0249` n `228`; crypto_major avg `-0.0577` n `8`; equity avg `0.0053` n `74`; fx avg `0.0161` n `6`; index avg `0.0001` n `23`; metal avg `0.0011` n `18`; unknown avg `-0.002` n `643`
- 1h: commodity avg `-0.2388` n `12`; crypto_alt avg `-0.1474` n `228`; crypto_major avg `-0.1511` n `8`; equity avg `0.0849` n `74`; fx avg `0.0459` n `6`; index avg `-0.0355` n `23`; metal avg `-0.0035` n `18`; unknown avg `-0.0941` n `643`
- 4h: commodity avg `-0.3149` n `12`; crypto_alt avg `-0.423` n `228`; crypto_major avg `-0.6715` n `8`; equity avg `-0.0621` n `74`; fx avg `-0.012` n `6`; index avg `0.057` n `23`; metal avg `0.0047` n `18`; unknown avg `0.4002` n `643`
- 24h: commodity avg `-0.4893` n `12`; crypto_alt avg `-0.3418` n `228`; crypto_major avg `0.1012` n `8`; equity avg `-0.4608` n `74`; fx avg `-0.0222` n `6`; index avg `0.3581` n `23`; metal avg `0.1354` n `18`; unknown avg `41.326` n `514`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
