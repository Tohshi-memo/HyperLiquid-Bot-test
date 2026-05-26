# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T21:22:18.171835+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0183` n `12`; crypto_alt avg `0.0112` n `228`; crypto_major avg `-0.0136` n `8`; equity avg `0.0666` n `67`; fx avg `0.0117` n `6`; index avg `0.009` n `23`; metal avg `-0.0272` n `18`; unknown avg `0.2381` n `418`
- 1h: commodity avg `0.2741` n `12`; crypto_alt avg `-0.0979` n `228`; crypto_major avg `-0.1773` n `8`; equity avg `0.1351` n `67`; fx avg `-0.0036` n `6`; index avg `-0.0212` n `23`; metal avg `-0.0039` n `18`; unknown avg `0.3267` n `418`
- 4h: commodity avg `0.0047` n `12`; crypto_alt avg `-0.4877` n `228`; crypto_major avg `-0.6547` n `8`; equity avg `0.0257` n `67`; fx avg `0.0194` n `6`; index avg `0.1035` n `23`; metal avg `0.3796` n `18`; unknown avg `-0.3633` n `418`
- 24h: commodity avg `1.0618` n `12`; crypto_alt avg `-1.7579` n `228`; crypto_major avg `-1.6323` n `8`; equity avg `-0.2989` n `67`; fx avg `-0.1402` n `6`; index avg `0.3917` n `23`; metal avg `-0.8899` n `18`; unknown avg `0.2317` n `395`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1751`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1742`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1738`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1583`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1449`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1433`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1379`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1357`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
