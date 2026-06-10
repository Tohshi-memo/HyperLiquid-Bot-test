# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T07:22:23.966239+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.3016` n `12`; crypto_alt avg `0.2796` n `228`; crypto_major avg `0.221` n `8`; equity avg `0.0263` n `74`; fx avg `0.0107` n `6`; index avg `0.0148` n `23`; metal avg `-0.0926` n `18`; unknown avg `0.0574` n `547`
- 1h: commodity avg `0.59` n `12`; crypto_alt avg `0.6444` n `228`; crypto_major avg `0.3689` n `8`; equity avg `0.0369` n `74`; fx avg `0.0269` n `6`; index avg `0.0866` n `23`; metal avg `-0.1964` n `18`; unknown avg `0.1796` n `547`
- 4h: commodity avg `-0.2511` n `12`; crypto_alt avg `0.2441` n `228`; crypto_major avg `-0.1344` n `8`; equity avg `-0.1592` n `74`; fx avg `0.0707` n `6`; index avg `-0.1938` n `23`; metal avg `0.5782` n `18`; unknown avg `-0.7039` n `537`
- 24h: commodity avg `-0.6895` n `12`; crypto_alt avg `-1.4244` n `228`; crypto_major avg `-3.8674` n `8`; equity avg `-3.5841` n `74`; fx avg `0.1836` n `6`; index avg `-1.7532` n `23`; metal avg `-2.6481` n `18`; unknown avg `-0.0208` n `535`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0603`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0523`, n `668`, weak_sample_signal
