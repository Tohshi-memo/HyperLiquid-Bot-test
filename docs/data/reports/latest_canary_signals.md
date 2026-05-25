# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T04:52:22.146420+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0723` n `12`; crypto_alt avg `0.4949` n `228`; crypto_major avg `0.468` n `8`; equity avg `0.0975` n `67`; fx avg `-0.0014` n `6`; index avg `-0.0456` n `23`; metal avg `0.0585` n `18`; unknown avg `-0.3365` n `397`
- 1h: commodity avg `0.0076` n `12`; crypto_alt avg `0.7562` n `228`; crypto_major avg `0.711` n `8`; equity avg `0.1258` n `67`; fx avg `-0.0053` n `6`; index avg `0.1018` n `23`; metal avg `0.2373` n `18`; unknown avg `-0.1828` n `397`
- 4h: commodity avg `-0.3757` n `12`; crypto_alt avg `0.7145` n `228`; crypto_major avg `0.3014` n `8`; equity avg `0.394` n `67`; fx avg `-0.0394` n `6`; index avg `0.1602` n `23`; metal avg `-0.1416` n `18`; unknown avg `-0.2601` n `396`
- 24h: commodity avg `-0.0085` n `12`; crypto_alt avg `-0.2837` n `228`; crypto_major avg `0.5263` n `8`; equity avg `0.4928` n `67`; fx avg `-0.0897` n `6`; index avg `-0.1045` n `23`; metal avg `0.624` n `18`; unknown avg `-0.1838` n `386`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1491`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1327`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
