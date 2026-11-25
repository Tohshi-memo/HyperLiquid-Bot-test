# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T09:22:31.118222+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.032` n `13`; crypto_alt avg `-0.2053` n `239`; crypto_major avg `-0.3416` n `8`; equity avg `-0.3475` n `168`; fx avg `-0.0143` n `6`; index avg `-0.0482` n `27`; metal avg `-0.0855` n `20`; unknown avg `0.196` n `1261`
- 1h: commodity avg `0.276` n `13`; crypto_alt avg `0.051` n `239`; crypto_major avg `-0.0759` n `8`; equity avg `-0.4601` n `168`; fx avg `0.0095` n `6`; index avg `-0.0451` n `27`; metal avg `0.0027` n `20`; unknown avg `265.4516` n `1257`
- 4h: commodity avg `0.0278` n `13`; crypto_alt avg `-0.0587` n `239`; crypto_major avg `-0.61` n `8`; equity avg `-1.2267` n `168`; fx avg `-0.0122` n `6`; index avg `-0.1208` n `27`; metal avg `-0.1545` n `20`; unknown avg `167.6511` n `1205`
- 24h: commodity avg `0.2839` n `13`; crypto_alt avg `-1.9078` n `239`; crypto_major avg `-2.6945` n `8`; equity avg `-4.9556` n `167`; fx avg `0.0678` n `6`; index avg `-0.4406` n `27`; metal avg `-0.8252` n `20`; unknown avg `649.7176` n `1035`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
