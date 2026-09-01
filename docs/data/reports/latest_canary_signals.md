# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T10:52:26.514769+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0421` n `12`; crypto_alt avg `-0.1112` n `232`; crypto_major avg `-0.1372` n `8`; equity avg `-0.1495` n `130`; fx avg `0.0054` n `6`; index avg `-0.0404` n `26`; metal avg `-0.0795` n `20`; unknown avg `-0.1363` n `792`
- 1h: commodity avg `-0.0125` n `12`; crypto_alt avg `0.4781` n `232`; crypto_major avg `0.3111` n `8`; equity avg `-0.0546` n `130`; fx avg `-0.003` n `6`; index avg `-0.0011` n `26`; metal avg `0.06` n `20`; unknown avg `0.0878` n `790`
- 4h: commodity avg `0.202` n `12`; crypto_alt avg `-0.6692` n `232`; crypto_major avg `-0.7162` n `8`; equity avg `-1.3456` n `130`; fx avg `0.0233` n `6`; index avg `-0.2861` n `26`; metal avg `-0.5399` n `20`; unknown avg `-0.1919` n `790`
- 24h: commodity avg `0.3277` n `12`; crypto_alt avg `0.5046` n `232`; crypto_major avg `-0.1768` n `8`; equity avg `-0.679` n `130`; fx avg `0.0997` n `6`; index avg `-0.2661` n `26`; metal avg `-0.7801` n `20`; unknown avg `0.0817` n `750`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0505`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.046`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0344`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0311`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0308`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.03`, n `668`, weak_sample_signal
