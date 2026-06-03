# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T19:22:23.850794+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0137` n `12`; crypto_alt avg `-0.6569` n `228`; crypto_major avg `-0.6192` n `8`; equity avg `-0.0537` n `73`; fx avg `0.0064` n `6`; index avg `-0.0708` n `23`; metal avg `-0.0346` n `18`; unknown avg `0.0008` n `419`
- 1h: commodity avg `0.0489` n `12`; crypto_alt avg `0.1522` n `228`; crypto_major avg `-0.1851` n `8`; equity avg `-0.2578` n `73`; fx avg `0.0351` n `6`; index avg `-0.0417` n `23`; metal avg `0.0013` n `18`; unknown avg `-0.0311` n `419`
- 4h: commodity avg `0.2769` n `12`; crypto_alt avg `-1.136` n `228`; crypto_major avg `-0.9251` n `8`; equity avg `-0.5305` n `73`; fx avg `0.0219` n `6`; index avg `-0.1477` n `23`; metal avg `-0.3821` n `18`; unknown avg `-0.4763` n `419`
- 24h: commodity avg `0.8533` n `12`; crypto_alt avg `1.2303` n `228`; crypto_major avg `-2.0502` n `8`; equity avg `-1.9808` n `72`; fx avg `0.044` n `6`; index avg `-0.3033` n `23`; metal avg `-1.9371` n `18`; unknown avg `0.1516` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1337`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0598`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0531`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0484`, n `668`, weak_sample_signal
