# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T04:54:23.897116+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0155` n `12`; crypto_alt avg `0.0279` n `230`; crypto_major avg `0.0095` n `8`; equity avg `-0.0044` n `114`; fx avg `0.0042` n `6`; index avg `-0.0021` n `25`; metal avg `0.0145` n `20`; unknown avg `16.4862` n `792`
- 1h: commodity avg `-0.0114` n `12`; crypto_alt avg `0.1406` n `230`; crypto_major avg `-0.0539` n `8`; equity avg `0.0456` n `114`; fx avg `-0.0092` n `6`; index avg `0.0077` n `25`; metal avg `-0.0033` n `20`; unknown avg `0.0165` n `792`
- 4h: commodity avg `0.0158` n `12`; crypto_alt avg `1.013` n `230`; crypto_major avg `1.1398` n `8`; equity avg `0.6202` n `114`; fx avg `0.02` n `6`; index avg `0.0691` n `25`; metal avg `0.0395` n `20`; unknown avg `1.3663` n `792`
- 24h: commodity avg `-0.1471` n `12`; crypto_alt avg `0.4753` n `230`; crypto_major avg `0.6337` n `8`; equity avg `0.7828` n `114`; fx avg `-0.0309` n `6`; index avg `0.089` n `25`; metal avg `0.1935` n `20`; unknown avg `0.0125` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1758`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1755`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.149`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1481`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
