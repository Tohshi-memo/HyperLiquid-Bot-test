# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T23:37:26.904913+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0009` n `12`; crypto_alt avg `0.0676` n `230`; crypto_major avg `0.1528` n `8`; equity avg `0.0683` n `114`; fx avg `0.004` n `6`; index avg `0.0041` n `25`; metal avg `0.0307` n `20`; unknown avg `-0.0951` n `793`
- 1h: commodity avg `-0.0213` n `12`; crypto_alt avg `0.0732` n `230`; crypto_major avg `0.2781` n `8`; equity avg `-0.0439` n `114`; fx avg `-0.0218` n `6`; index avg `-0.0133` n `25`; metal avg `0.0473` n `20`; unknown avg `-0.163` n `793`
- 4h: commodity avg `0.0988` n `12`; crypto_alt avg `-0.2155` n `230`; crypto_major avg `0.2632` n `8`; equity avg `0.0025` n `114`; fx avg `-0.0134` n `6`; index avg `-0.005` n `25`; metal avg `0.0232` n `20`; unknown avg `-0.2847` n `792`
- 24h: commodity avg `0.5576` n `12`; crypto_alt avg `0.5326` n `230`; crypto_major avg `1.7213` n `8`; equity avg `1.1898` n `114`; fx avg `0.0078` n `6`; index avg `0.0467` n `25`; metal avg `0.2658` n `20`; unknown avg `0.3129` n `776`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.192`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1598`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1284`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1258`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
