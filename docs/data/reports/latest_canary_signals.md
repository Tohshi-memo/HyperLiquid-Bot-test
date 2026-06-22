# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T05:22:31.593379+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0101` n `12`; crypto_alt avg `0.0966` n `228`; crypto_major avg `0.1104` n `8`; equity avg `0.0347` n `79`; fx avg `-0.0044` n `6`; index avg `0.0252` n `23`; metal avg `0.0524` n `18`; unknown avg `0.0926` n `701`
- 1h: commodity avg `-0.0636` n `12`; crypto_alt avg `0.321` n `228`; crypto_major avg `0.4226` n `8`; equity avg `0.1161` n `79`; fx avg `-0.0056` n `6`; index avg `0.0215` n `23`; metal avg `0.1137` n `18`; unknown avg `-0.4577` n `701`
- 4h: commodity avg `-0.1561` n `12`; crypto_alt avg `-0.0439` n `228`; crypto_major avg `-0.2294` n `8`; equity avg `0.1005` n `79`; fx avg `0.0096` n `6`; index avg `-0.0522` n `23`; metal avg `-0.3495` n `18`; unknown avg `-0.6733` n `693`
- 24h: commodity avg `-0.376` n `12`; crypto_alt avg `0.3286` n `228`; crypto_major avg `-0.3771` n `8`; equity avg `-0.5006` n `79`; fx avg `-0.0021` n `6`; index avg `-0.0165` n `23`; metal avg `0.2076` n `18`; unknown avg `-0.4273` n `637`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
