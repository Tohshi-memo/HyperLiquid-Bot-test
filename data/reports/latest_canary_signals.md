# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T09:22:36.087806+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.6003` n `12`; crypto_alt avg `0.1265` n `228`; crypto_major avg `0.0237` n `8`; equity avg `0.0838` n `74`; fx avg `0.1014` n `6`; index avg `0.0211` n `23`; metal avg `0.1933` n `18`; unknown avg `0.135` n `643`
- 1h: commodity avg `0.8612` n `12`; crypto_alt avg `0.2389` n `228`; crypto_major avg `0.0823` n `8`; equity avg `0.1421` n `74`; fx avg `-0.0284` n `6`; index avg `0.0938` n `23`; metal avg `0.2409` n `18`; unknown avg `0.2378` n `643`
- 4h: commodity avg `0.7371` n `12`; crypto_alt avg `1.3799` n `228`; crypto_major avg `0.9639` n `8`; equity avg `0.3521` n `74`; fx avg `-0.0466` n `6`; index avg `0.0558` n `23`; metal avg `0.3507` n `18`; unknown avg `0.1737` n `627`
- 24h: commodity avg `1.169` n `12`; crypto_alt avg `0.7478` n `228`; crypto_major avg `0.0633` n `8`; equity avg `-0.5233` n `74`; fx avg `0.0275` n `6`; index avg `0.7007` n `23`; metal avg `0.397` n `18`; unknown avg `28.1924` n `619`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
