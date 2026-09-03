# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T09:37:26.580164+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0331` n `12`; crypto_alt avg `-0.0628` n `232`; crypto_major avg `-0.1677` n `8`; equity avg `-0.0335` n `133`; fx avg `-0.0132` n `6`; index avg `-1.8112` n `26`; metal avg `-0.0414` n `20`; unknown avg `0.068` n `792`
- 1h: commodity avg `0.147` n `12`; crypto_alt avg `-0.1241` n `232`; crypto_major avg `-0.3451` n `8`; equity avg `-0.2715` n `133`; fx avg `-0.0335` n `6`; index avg `-1.8382` n `26`; metal avg `-0.0525` n `20`; unknown avg `0.23` n `790`
- 4h: commodity avg `0.2566` n `12`; crypto_alt avg `0.5365` n `232`; crypto_major avg `0.2534` n `8`; equity avg `0.1504` n `133`; fx avg `-0.1317` n `6`; index avg `-1.7631` n `26`; metal avg `0.0896` n `20`; unknown avg `16.2152` n `754`
- 24h: commodity avg `0.3205` n `12`; crypto_alt avg `1.6731` n `232`; crypto_major avg `1.708` n `8`; equity avg `1.7563` n `133`; fx avg `-0.4138` n `6`; index avg `-1.6134` n `26`; metal avg `0.899` n `20`; unknown avg `0.0808` n `735`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0628`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0489`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0477`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0449`, n `668`, weak_sample_signal
