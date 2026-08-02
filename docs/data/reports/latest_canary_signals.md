# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T19:37:31.574885+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0282` n `12`; crypto_alt avg `0.0252` n `230`; crypto_major avg `-0.0024` n `8`; equity avg `0.0419` n `102`; fx avg `0.0314` n `6`; index avg `0.0043` n `25`; metal avg `0.0121` n `20`; unknown avg `-0.0308` n `783`
- 1h: commodity avg `-0.0492` n `12`; crypto_alt avg `-0.0607` n `230`; crypto_major avg `-0.1271` n `8`; equity avg `0.0819` n `102`; fx avg `0.0514` n `6`; index avg `0.0085` n `25`; metal avg `0.0174` n `20`; unknown avg `0.0078` n `782`
- 4h: commodity avg `-0.1403` n `12`; crypto_alt avg `0.1188` n `230`; crypto_major avg `0.6033` n `8`; equity avg `0.4456` n `102`; fx avg `0.0667` n `6`; index avg `0.0605` n `25`; metal avg `0.0875` n `20`; unknown avg `0.3119` n `782`
- 24h: commodity avg `-1.409` n `12`; crypto_alt avg `1.5534` n `230`; crypto_major avg `2.0644` n `8`; equity avg `1.7214` n `102`; fx avg `-0.0696` n `6`; index avg `0.3128` n `25`; metal avg `0.332` n `20`; unknown avg `1.6672` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1365`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0644`, n `668`, weak_sample_signal
