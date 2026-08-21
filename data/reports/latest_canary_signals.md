# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T18:37:27.598648+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0205` n `12`; crypto_alt avg `-0.3422` n `230`; crypto_major avg `-0.2692` n `8`; equity avg `-0.1109` n `121`; fx avg `-0.0005` n `6`; index avg `-0.0032` n `25`; metal avg `-0.0157` n `20`; unknown avg `0.1313` n `793`
- 1h: commodity avg `-0.0388` n `12`; crypto_alt avg `0.0521` n `230`; crypto_major avg `-0.0253` n `8`; equity avg `-0.2041` n `121`; fx avg `0.0063` n `6`; index avg `-0.0178` n `25`; metal avg `-0.0421` n `20`; unknown avg `-0.069` n `793`
- 4h: commodity avg `0.0392` n `12`; crypto_alt avg `0.2259` n `230`; crypto_major avg `-0.0887` n `8`; equity avg `0.1244` n `121`; fx avg `0.0356` n `6`; index avg `0.0445` n `25`; metal avg `0.0987` n `20`; unknown avg `0.0623` n `793`
- 24h: commodity avg `0.1516` n `12`; crypto_alt avg `7.9002` n `230`; crypto_major avg `5.2618` n `8`; equity avg `1.4333` n `121`; fx avg `-0.1031` n `6`; index avg `0.1568` n `25`; metal avg `0.6208` n `20`; unknown avg `1.2412` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.232`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1991`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1921`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1844`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
