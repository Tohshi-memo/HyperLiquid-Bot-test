# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T07:07:24.575843+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.5238` n `12`; crypto_alt avg `0.1675` n `228`; crypto_major avg `0.113` n `8`; equity avg `-0.1125` n `74`; fx avg `0.0268` n `6`; index avg `-0.0116` n `23`; metal avg `-0.088` n `18`; unknown avg `0.0132` n `547`
- 1h: commodity avg `0.6679` n `12`; crypto_alt avg `0.5618` n `228`; crypto_major avg `0.2135` n `8`; equity avg `0.1503` n `74`; fx avg `0.0208` n `6`; index avg `0.0751` n `23`; metal avg `-0.1209` n `18`; unknown avg `-0.2533` n `547`
- 4h: commodity avg `0.1251` n `12`; crypto_alt avg `-0.0193` n `228`; crypto_major avg `-0.2151` n `8`; equity avg `-0.1142` n `74`; fx avg `0.0681` n `6`; index avg `-0.2114` n `23`; metal avg `0.6859` n `18`; unknown avg `-0.7131` n `537`
- 24h: commodity avg `-0.344` n `12`; crypto_alt avg `-1.5613` n `228`; crypto_major avg `-4.0714` n `8`; equity avg `-3.7207` n `74`; fx avg `0.1932` n `6`; index avg `-1.7756` n `23`; metal avg `-2.6384` n `18`; unknown avg `-0.0111` n `535`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0561`, n `668`, weak_sample_signal
