# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T23:22:24.774017+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0015` n `12`; crypto_alt avg `0.0064` n `232`; crypto_major avg `-0.0619` n `8`; equity avg `0.0145` n `133`; fx avg `-0.0106` n `6`; index avg `-0.0113` n `26`; metal avg `-0.0274` n `20`; unknown avg `-0.0244` n `792`
- 1h: commodity avg `0.0059` n `12`; crypto_alt avg `0.3721` n `232`; crypto_major avg `0.2029` n `8`; equity avg `0.0256` n `133`; fx avg `0.0083` n `6`; index avg `0.0041` n `26`; metal avg `-0.0184` n `20`; unknown avg `0.2835` n `790`
- 4h: commodity avg `0.0119` n `12`; crypto_alt avg `0.108` n `232`; crypto_major avg `-0.0857` n `8`; equity avg `0.1343` n `133`; fx avg `-0.0329` n `6`; index avg `0.0047` n `26`; metal avg `-0.0197` n `20`; unknown avg `-0.3476` n `772`
- 24h: commodity avg `0.1565` n `12`; crypto_alt avg `0.1162` n `232`; crypto_major avg `-0.2979` n `8`; equity avg `1.1716` n `133`; fx avg `-0.392` n `6`; index avg `0.1343` n `26`; metal avg `0.4538` n `20`; unknown avg `-0.5158` n `751`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0655`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0649`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0585`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0465`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0445`, n `668`, weak_sample_signal
