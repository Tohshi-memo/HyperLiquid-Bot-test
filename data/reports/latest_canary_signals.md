# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T00:52:27.417965+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0448` n `12`; crypto_alt avg `-0.0121` n `230`; crypto_major avg `-0.0625` n `8`; equity avg `-0.1319` n `108`; fx avg `-0.045` n `6`; index avg `-0.0385` n `25`; metal avg `0.028` n `20`; unknown avg `-0.0308` n `782`
- 1h: commodity avg `-0.0356` n `12`; crypto_alt avg `0.177` n `230`; crypto_major avg `0.0516` n `8`; equity avg `-0.3753` n `108`; fx avg `-0.0589` n `6`; index avg `-0.0987` n `25`; metal avg `0.0749` n `20`; unknown avg `-0.2466` n `782`
- 4h: commodity avg `-0.059` n `12`; crypto_alt avg `-0.0597` n `230`; crypto_major avg `-0.4514` n `8`; equity avg `-0.4809` n `108`; fx avg `-0.0524` n `6`; index avg `-0.129` n `25`; metal avg `0.2522` n `20`; unknown avg `0.0784` n `782`
- 24h: commodity avg `-0.1467` n `12`; crypto_alt avg `0.9079` n `230`; crypto_major avg `0.9504` n `8`; equity avg `-1.6089` n `108`; fx avg `-0.0256` n `6`; index avg `-0.3191` n `25`; metal avg `1.0101` n `20`; unknown avg `1.1073` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1337`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
