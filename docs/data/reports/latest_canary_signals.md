# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T05:07:23.970558+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0402` n `12`; crypto_alt avg `0.1745` n `230`; crypto_major avg `0.3425` n `8`; equity avg `0.1981` n `108`; fx avg `0.0054` n `6`; index avg `0.0456` n `25`; metal avg `0.0002` n `20`; unknown avg `0.758` n `782`
- 1h: commodity avg `-0.005` n `12`; crypto_alt avg `0.4486` n `230`; crypto_major avg `0.5303` n `8`; equity avg `0.2642` n `108`; fx avg `-0.0098` n `6`; index avg `0.0598` n `25`; metal avg `-0.0319` n `20`; unknown avg `0.7578` n `782`
- 4h: commodity avg `-0.047` n `12`; crypto_alt avg `-0.0503` n `230`; crypto_major avg `-0.0483` n `8`; equity avg `0.5933` n `108`; fx avg `0.0173` n `6`; index avg `0.0664` n `25`; metal avg `-0.274` n `20`; unknown avg `0.1707` n `782`
- 24h: commodity avg `-0.0757` n `12`; crypto_alt avg `0.145` n `230`; crypto_major avg `0.0883` n `8`; equity avg `-1.9014` n `108`; fx avg `-0.0608` n `6`; index avg `-0.3217` n `25`; metal avg `0.5085` n `20`; unknown avg `0.9041` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.182`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1633`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1289`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
