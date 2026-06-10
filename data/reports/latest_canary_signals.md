# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T11:37:30.089307+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.1503` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.4483` n `12`; crypto_alt avg `-0.4469` n `228`; crypto_major avg `-0.3692` n `8`; equity avg `-0.4368` n `74`; fx avg `0.0021` n `6`; index avg `-0.1872` n `23`; metal avg `-0.1437` n `18`; unknown avg `-0.0424` n `547`
- 1h: commodity avg `0.9836` n `12`; crypto_alt avg `-0.9565` n `228`; crypto_major avg `-0.5345` n `8`; equity avg `-0.5567` n `74`; fx avg `-0.0093` n `6`; index avg `-0.3385` n `23`; metal avg `-0.0713` n `18`; unknown avg `0.1867` n `547`
- 4h: commodity avg `0.9774` n `12`; crypto_alt avg `-1.6214` n `228`; crypto_major avg `-1.1729` n `8`; equity avg `-1.2658` n `74`; fx avg `-0.0762` n `6`; index avg `-0.7095` n `23`; metal avg `-0.3645` n `18`; unknown avg `0.3195` n `547`
- 24h: commodity avg `0.5712` n `12`; crypto_alt avg `-2.2869` n `228`; crypto_major avg `-3.7934` n `8`; equity avg `-4.9362` n `74`; fx avg `-0.0656` n `6`; index avg `-2.6925` n `23`; metal avg `-3.6317` n `18`; unknown avg `0.3692` n `535`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0575`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0508`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0467`, n `668`, weak_sample_signal
