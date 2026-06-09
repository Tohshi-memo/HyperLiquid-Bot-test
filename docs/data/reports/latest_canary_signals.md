# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T18:37:32.466636+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.9988` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.2365` n `12`; crypto_alt avg `-0.0142` n `228`; crypto_major avg `-0.1158` n `8`; equity avg `0.2909` n `74`; fx avg `-0.0146` n `6`; index avg `0.2481` n `23`; metal avg `0.0413` n `18`; unknown avg `-0.0264` n `547`
- 1h: commodity avg `0.2476` n `12`; crypto_alt avg `0.0028` n `228`; crypto_major avg `0.0553` n `8`; equity avg `0.6516` n `74`; fx avg `-0.0171` n `6`; index avg `0.5266` n `23`; metal avg `0.3475` n `18`; unknown avg `-0.13` n `547`
- 4h: commodity avg `0.1321` n `12`; crypto_alt avg `0.898` n `228`; crypto_major avg `0.3581` n `8`; equity avg `-1.6407` n `74`; fx avg `-0.0561` n `6`; index avg `-1.1556` n `23`; metal avg `-0.7856` n `18`; unknown avg `1.7803` n `547`
- 24h: commodity avg `-0.6843` n `12`; crypto_alt avg `-2.2162` n `228`; crypto_major avg `-2.8` n `8`; equity avg `-2.2981` n `74`; fx avg `0.0784` n `6`; index avg `-1.5379` n `23`; metal avg `-1.2807` n `18`; unknown avg `-1.3761` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.054`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0471`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0432`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0425`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0418`, n `668`, weak_sample_signal
