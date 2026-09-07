# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T04:22:24.191509+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0091` n `12`; crypto_alt avg `0.3004` n `232`; crypto_major avg `0.1557` n `8`; equity avg `0.0097` n `134`; fx avg `0.0186` n `6`; index avg `0.0063` n `26`; metal avg `-0.0041` n `20`; unknown avg `-0.1687` n `794`
- 1h: commodity avg `0.0788` n `12`; crypto_alt avg `-0.0986` n `232`; crypto_major avg `-0.1801` n `8`; equity avg `0.1107` n `134`; fx avg `0.0073` n `6`; index avg `0.0269` n `26`; metal avg `-0.0534` n `20`; unknown avg `-0.252` n `792`
- 4h: commodity avg `0.1094` n `12`; crypto_alt avg `-1.0033` n `232`; crypto_major avg `-0.8428` n `8`; equity avg `0.1756` n `134`; fx avg `0.0562` n `6`; index avg `0.0011` n `26`; metal avg `-0.1109` n `20`; unknown avg `3.0208` n `758`
- 24h: commodity avg `0.0537` n `12`; crypto_alt avg `0.3878` n `232`; crypto_major avg `-0.5358` n `8`; equity avg `0.4808` n `134`; fx avg `0.0484` n `6`; index avg `0.0018` n `26`; metal avg `-0.1851` n `20`; unknown avg `73.1453` n `658`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1942`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
