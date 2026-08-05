# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T15:22:31.658127+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0229` n `12`; crypto_alt avg `-0.0772` n `230`; crypto_major avg `-0.0859` n `8`; equity avg `0.0872` n `108`; fx avg `0.0139` n `6`; index avg `-0.001` n `25`; metal avg `0.0477` n `20`; unknown avg `-0.0466` n `782`
- 1h: commodity avg `0.067` n `12`; crypto_alt avg `0.0209` n `230`; crypto_major avg `0.1033` n `8`; equity avg `-0.225` n `108`; fx avg `-0.0198` n `6`; index avg `-0.0563` n `25`; metal avg `0.0784` n `20`; unknown avg `-0.0731` n `782`
- 4h: commodity avg `-0.3226` n `12`; crypto_alt avg `-0.0153` n `230`; crypto_major avg `0.2486` n `8`; equity avg `-0.0272` n `108`; fx avg `-0.0325` n `6`; index avg `-0.0039` n `25`; metal avg `0.2308` n `20`; unknown avg `-0.0197` n `782`
- 24h: commodity avg `-0.2363` n `12`; crypto_alt avg `0.9124` n `230`; crypto_major avg `0.6451` n `8`; equity avg `0.5632` n `108`; fx avg `0.0237` n `6`; index avg `0.2014` n `25`; metal avg `0.8812` n `20`; unknown avg `0.7106` n `749`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0553`, n `668`, weak_sample_signal
