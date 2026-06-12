# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T12:37:28.235377+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2244` n `12`; crypto_alt avg `-0.2047` n `228`; crypto_major avg `-0.0834` n `8`; equity avg `-0.1585` n `74`; fx avg `-0.008` n `6`; index avg `-0.1026` n `23`; metal avg `-0.2504` n `18`; unknown avg `-0.0679` n `643`
- 1h: commodity avg `0.5801` n `12`; crypto_alt avg `0.1693` n `228`; crypto_major avg `0.1733` n `8`; equity avg `-0.3963` n `74`; fx avg `-0.0139` n `6`; index avg `-0.1479` n `23`; metal avg `-0.3429` n `18`; unknown avg `0.3976` n `643`
- 4h: commodity avg `0.918` n `12`; crypto_alt avg `0.5305` n `228`; crypto_major avg `0.5735` n `8`; equity avg `0.0415` n `74`; fx avg `-0.0008` n `6`; index avg `0.1208` n `23`; metal avg `-0.6023` n `18`; unknown avg `1.6112` n `643`
- 24h: commodity avg `-2.3777` n `12`; crypto_alt avg `2.4098` n `228`; crypto_major avg `2.4563` n `8`; equity avg `3.193` n `74`; fx avg `0.0149` n `6`; index avg `1.7863` n `23`; metal avg `3.1566` n `18`; unknown avg `1.6522` n `514`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
