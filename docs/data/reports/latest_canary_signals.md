# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T09:37:31.293316+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0058` n `12`; crypto_alt avg `0.3282` n `228`; crypto_major avg `0.2219` n `8`; equity avg `0.0892` n `74`; fx avg `-0.0098` n `6`; index avg `-0.0067` n `23`; metal avg `0.0092` n `18`; unknown avg `-0.0839` n `629`
- 1h: commodity avg `0.1329` n `12`; crypto_alt avg `-0.0555` n `228`; crypto_major avg `-0.0831` n `8`; equity avg `-0.0276` n `74`; fx avg `-0.0142` n `6`; index avg `-0.0088` n `23`; metal avg `0.001` n `18`; unknown avg `-0.0311` n `629`
- 4h: commodity avg `-0.1089` n `12`; crypto_alt avg `0.4312` n `228`; crypto_major avg `0.0445` n `8`; equity avg `0.2422` n `74`; fx avg `-0.0187` n `6`; index avg `0.0362` n `23`; metal avg `0.2208` n `18`; unknown avg `1.9583` n `609`
- 24h: commodity avg `-0.8406` n `12`; crypto_alt avg `0.3054` n `228`; crypto_major avg `0.8189` n `8`; equity avg `0.8502` n `74`; fx avg `-0.0151` n `6`; index avg `0.2488` n `23`; metal avg `0.2934` n `18`; unknown avg `-1.253` n `591`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0628`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
