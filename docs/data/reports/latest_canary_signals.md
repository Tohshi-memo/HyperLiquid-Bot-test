# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T14:22:33.669503+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0676` n `12`; crypto_alt avg `0.5163` n `232`; crypto_major avg `0.5992` n `8`; equity avg `0.4095` n `133`; fx avg `-0.0005` n `6`; index avg `0.0611` n `26`; metal avg `0.0388` n `20`; unknown avg `0.2803` n `792`
- 1h: commodity avg `0.1118` n `12`; crypto_alt avg `0.2626` n `232`; crypto_major avg `0.6846` n `8`; equity avg `-0.0765` n `133`; fx avg `-0.0079` n `6`; index avg `0.0176` n `26`; metal avg `-0.0047` n `20`; unknown avg `2.2336` n `790`
- 4h: commodity avg `-0.0722` n `12`; crypto_alt avg `0.6228` n `232`; crypto_major avg `1.6688` n `8`; equity avg `0.4881` n `133`; fx avg `-0.0626` n `6`; index avg `0.1488` n `26`; metal avg `0.369` n `20`; unknown avg `12.8245` n `790`
- 24h: commodity avg `0.5387` n `12`; crypto_alt avg `2.0704` n `232`; crypto_major avg `2.4873` n `8`; equity avg `0.7859` n `133`; fx avg `-0.3245` n `6`; index avg `0.0248` n `26`; metal avg `0.4677` n `20`; unknown avg `15.9238` n `735`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0546`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0392`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0382`, n `668`, weak_sample_signal
