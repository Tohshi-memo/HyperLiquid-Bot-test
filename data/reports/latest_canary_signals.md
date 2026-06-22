# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T13:37:29.143420+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.0378` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.7022` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.049` n `12`; crypto_alt avg `0.264` n `228`; crypto_major avg `0.4477` n `8`; equity avg `0.1661` n `79`; fx avg `-0.0081` n `6`; index avg `0.0228` n `23`; metal avg `0.0001` n `20`; unknown avg `-0.1165` n `722`
- 1h: commodity avg `-0.1001` n `12`; crypto_alt avg `0.2639` n `228`; crypto_major avg `0.6275` n `8`; equity avg `0.2419` n `79`; fx avg `-0.03` n `6`; index avg `0.0431` n `23`; metal avg `0.0389` n `20`; unknown avg `-0.1496` n `722`
- 4h: commodity avg `-0.3882` n `12`; crypto_alt avg `1.4565` n `228`; crypto_major avg `1.6496` n `8`; equity avg `0.6547` n `79`; fx avg `0.0046` n `6`; index avg `0.1587` n `23`; metal avg `-0.0526` n `18`; unknown avg `0.8511` n `701`
- 24h: commodity avg `-0.6336` n `12`; crypto_alt avg `1.0885` n `228`; crypto_major avg `1.8903` n `8`; equity avg `0.5527` n `79`; fx avg `0.0237` n `6`; index avg `0.1884` n `23`; metal avg `0.4856` n `18`; unknown avg `0.5812` n `637`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
