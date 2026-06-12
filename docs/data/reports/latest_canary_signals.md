# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T16:37:32.034689+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1191` n `12`; crypto_alt avg `0.2139` n `228`; crypto_major avg `0.3662` n `8`; equity avg `0.1939` n `74`; fx avg `0.0038` n `6`; index avg `0.067` n `23`; metal avg `-0.14` n `18`; unknown avg `0.0241` n `643`
- 1h: commodity avg `0.1798` n `12`; crypto_alt avg `-0.299` n `228`; crypto_major avg `-0.0781` n `8`; equity avg `-0.1271` n `74`; fx avg `-0.0114` n `6`; index avg `-0.0934` n `23`; metal avg `-0.0124` n `18`; unknown avg `0.1132` n `643`
- 4h: commodity avg `0.0226` n `12`; crypto_alt avg `-0.2473` n `228`; crypto_major avg `0.6054` n `8`; equity avg `-0.2941` n `74`; fx avg `0.0008` n `6`; index avg `0.3501` n `23`; metal avg `0.5241` n `18`; unknown avg `25.8843` n `643`
- 24h: commodity avg `-2.1455` n `12`; crypto_alt avg `1.385` n `228`; crypto_major avg `2.709` n `8`; equity avg `1.909` n `74`; fx avg `0.0893` n `6`; index avg `1.6739` n `23`; metal avg `2.9315` n `18`; unknown avg `41.2285` n `514`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0591`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0591`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0577`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0562`, n `668`, weak_sample_signal
