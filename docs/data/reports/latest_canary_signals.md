# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T10:07:19.119575+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1128` n `12`; crypto_alt avg `-0.1438` n `228`; crypto_major avg `0.0029` n `8`; equity avg `-0.1823` n `67`; fx avg `-0.0023` n `6`; index avg `-0.047` n `23`; metal avg `0.0396` n `18`; unknown avg `-0.1129` n `386`
- 1h: commodity avg `-0.2486` n `12`; crypto_alt avg `-0.1844` n `228`; crypto_major avg `-0.1001` n `8`; equity avg `-0.047` n `67`; fx avg `-0.0205` n `6`; index avg `-0.0651` n `23`; metal avg `0.5598` n `18`; unknown avg `-0.0544` n `386`
- 4h: commodity avg `0.0632` n `12`; crypto_alt avg `-0.0054` n `228`; crypto_major avg `0.3151` n `8`; equity avg `-0.4874` n `67`; fx avg `-0.0187` n `6`; index avg `-0.1026` n `23`; metal avg `0.1662` n `18`; unknown avg `-0.5215` n `386`
- 24h: commodity avg `0.1587` n `12`; crypto_alt avg `1.6729` n `228`; crypto_major avg `0.2947` n `8`; equity avg `0.7207` n `67`; fx avg `0.0983` n `6`; index avg `0.5392` n `23`; metal avg `0.6361` n `18`; unknown avg `0.979` n `375`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0617`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0495`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0484`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0432`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0401`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0393`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0365`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0351`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0345`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0334`, n `668`, weak_sample_signal
