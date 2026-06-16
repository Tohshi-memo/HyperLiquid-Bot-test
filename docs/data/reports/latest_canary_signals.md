# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T17:37:38.788872+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0073` n `12`; crypto_alt avg `0.217` n `228`; crypto_major avg `0.2096` n `8`; equity avg `-0.0314` n `77`; fx avg `-0.0033` n `6`; index avg `-0.0076` n `23`; metal avg `0.187` n `18`; unknown avg `0.0197` n `687`
- 1h: commodity avg `0.1578` n `12`; crypto_alt avg `0.384` n `228`; crypto_major avg `0.1645` n `8`; equity avg `-0.0811` n `77`; fx avg `0.001` n `6`; index avg `0.001` n `23`; metal avg `-0.0837` n `18`; unknown avg `0.0644` n `687`
- 4h: commodity avg `-0.5728` n `12`; crypto_alt avg `-0.4763` n `228`; crypto_major avg `-0.9924` n `8`; equity avg `-1.233` n `77`; fx avg `0.0605` n `6`; index avg `-0.8746` n `23`; metal avg `-0.2205` n `18`; unknown avg `0.3689` n `687`
- 24h: commodity avg `-0.9717` n `12`; crypto_alt avg `-1.7528` n `228`; crypto_major avg `-1.2316` n `8`; equity avg `-1.2194` n `77`; fx avg `-0.009` n `6`; index avg `-0.8206` n `23`; metal avg `0.5008` n `18`; unknown avg `0.4849` n `623`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0608`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0591`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0589`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0554`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0468`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0458`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0439`, n `668`, weak_sample_signal
