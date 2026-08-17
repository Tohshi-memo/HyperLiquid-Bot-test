# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T04:37:31.718705+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0064` n `12`; crypto_alt avg `0.0054` n `230`; crypto_major avg `-0.0935` n `8`; equity avg `-0.0054` n `114`; fx avg `-0.0145` n `6`; index avg `-0.0034` n `25`; metal avg `-0.0128` n `20`; unknown avg `-0.0129` n `792`
- 1h: commodity avg `-0.0479` n `12`; crypto_alt avg `0.1356` n `230`; crypto_major avg `0.0503` n `8`; equity avg `0.0908` n `114`; fx avg `-0.0111` n `6`; index avg `0.0181` n `25`; metal avg `-0.0306` n `20`; unknown avg `-0.0696` n `792`
- 4h: commodity avg `0.0035` n `12`; crypto_alt avg `1.0233` n `230`; crypto_major avg `1.2169` n `8`; equity avg `0.6888` n `114`; fx avg `-0.0109` n `6`; index avg `0.0608` n `25`; metal avg `0.0828` n `20`; unknown avg `1.8337` n `792`
- 24h: commodity avg `-0.1751` n `12`; crypto_alt avg `0.5234` n `230`; crypto_major avg `0.6726` n `8`; equity avg `0.8052` n `114`; fx avg `-0.0392` n `6`; index avg `0.0948` n `25`; metal avg `0.1779` n `20`; unknown avg `0.0743` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1756`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1751`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1484`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1482`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
