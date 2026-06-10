# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T07:52:24.730093+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0133` n `12`; crypto_alt avg `-0.1452` n `228`; crypto_major avg `-0.0231` n `8`; equity avg `-0.1058` n `74`; fx avg `-0.0202` n `6`; index avg `-0.0949` n `23`; metal avg `-0.0926` n `18`; unknown avg `-0.0393` n `547`
- 1h: commodity avg `0.4993` n `12`; crypto_alt avg `0.3759` n `228`; crypto_major avg `0.5555` n `8`; equity avg `-0.1952` n `74`; fx avg `0.0352` n `6`; index avg `-0.095` n `23`; metal avg `-0.3946` n `18`; unknown avg `0.0659` n `547`
- 4h: commodity avg `0.1827` n `12`; crypto_alt avg `0.2089` n `228`; crypto_major avg `0.0119` n `8`; equity avg `-0.032` n `74`; fx avg `0.0624` n `6`; index avg `-0.2817` n `23`; metal avg `0.1361` n `18`; unknown avg `-0.6625` n `537`
- 24h: commodity avg `-0.5026` n `12`; crypto_alt avg `-1.2433` n `228`; crypto_major avg `-3.3352` n `8`; equity avg `-3.5189` n `74`; fx avg `0.1646` n `6`; index avg `-1.7139` n `23`; metal avg `-2.9833` n `18`; unknown avg `0.0368` n `535`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0595`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0567`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0551`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0484`, n `668`, weak_sample_signal
