# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T11:37:25.184604+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2618` n `12`; crypto_alt avg `-0.2458` n `228`; crypto_major avg `-0.1316` n `8`; equity avg `-0.0011` n `74`; fx avg `-0.0115` n `6`; index avg `-0.0237` n `23`; metal avg `-0.1507` n `18`; unknown avg `-0.0278` n `643`
- 1h: commodity avg `-0.0658` n `12`; crypto_alt avg `-0.2419` n `228`; crypto_major avg `0.1157` n `8`; equity avg `0.1644` n `74`; fx avg `-0.0223` n `6`; index avg `0.1175` n `23`; metal avg `-0.2178` n `18`; unknown avg `0.2855` n `643`
- 4h: commodity avg `-0.6817` n `12`; crypto_alt avg `1.1601` n `228`; crypto_major avg `1.1723` n `8`; equity avg `1.0495` n `74`; fx avg `-0.0048` n `6`; index avg `0.5655` n `23`; metal avg `0.6239` n `18`; unknown avg `0.6971` n `531`
- 24h: commodity avg `-2.1118` n `12`; crypto_alt avg `1.6475` n `228`; crypto_major avg `1.5777` n `8`; equity avg `2.7398` n `74`; fx avg `0.0042` n `6`; index avg `1.6149` n `23`; metal avg `3.0368` n `18`; unknown avg `1.121` n `514`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
