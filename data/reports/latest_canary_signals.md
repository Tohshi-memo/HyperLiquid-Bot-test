# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T09:07:35.242536+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1146` n `12`; crypto_alt avg `0.2393` n `228`; crypto_major avg `0.0819` n `8`; equity avg `0.0672` n `74`; fx avg `-0.0035` n `6`; index avg `0.0427` n `23`; metal avg `0.0598` n `18`; unknown avg `0.2393` n `643`
- 1h: commodity avg `-0.5658` n `12`; crypto_alt avg `0.5563` n `228`; crypto_major avg `0.5108` n `8`; equity avg `0.2475` n `74`; fx avg `-0.0122` n `6`; index avg `0.04` n `23`; metal avg `0.4063` n `18`; unknown avg `3.3884` n `643`
- 4h: commodity avg `-1.2702` n `12`; crypto_alt avg `0.1692` n `228`; crypto_major avg `-0.0822` n `8`; equity avg `-0.2856` n `74`; fx avg `-0.0461` n `6`; index avg `-0.18` n `23`; metal avg `0.3152` n `18`; unknown avg `0.0171` n `515`
- 24h: commodity avg `-2.7454` n `12`; crypto_alt avg `1.7294` n `228`; crypto_major avg `1.7386` n `8`; equity avg `2.4997` n `74`; fx avg `-0.0274` n `6`; index avg `1.3637` n `23`; metal avg `3.2118` n `18`; unknown avg `-0.4419` n `514`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1304`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
