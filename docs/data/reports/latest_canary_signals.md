# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T07:52:24.689213+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0011` n `12`; crypto_alt avg `0.2491` n `230`; crypto_major avg `0.2142` n `8`; equity avg `0.0329` n `121`; fx avg `-0.0373` n `6`; index avg `-0.0012` n `25`; metal avg `0.0074` n `20`; unknown avg `0.0115` n `794`
- 1h: commodity avg `0.0012` n `12`; crypto_alt avg `0.8388` n `230`; crypto_major avg `0.5271` n `8`; equity avg `0.089` n `121`; fx avg `0.0706` n `6`; index avg `0.0027` n `25`; metal avg `0.0197` n `20`; unknown avg `0.1618` n `794`
- 4h: commodity avg `0.0107` n `12`; crypto_alt avg `0.5622` n `230`; crypto_major avg `-0.4589` n `8`; equity avg `-0.1169` n `121`; fx avg `0.0167` n `6`; index avg `-0.0297` n `25`; metal avg `-0.007` n `20`; unknown avg `0.4219` n `778`
- 24h: commodity avg `-0.0167` n `12`; crypto_alt avg `-3.5147` n `230`; crypto_major avg `-2.1927` n `8`; equity avg `-0.0444` n `121`; fx avg `0.1253` n `6`; index avg `-0.0167` n `25`; metal avg `0.0621` n `20`; unknown avg `2.4063` n `778`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1521`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1297`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1275`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
