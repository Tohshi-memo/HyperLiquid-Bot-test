# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T23:32:21.354774+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0024` n `12`; crypto_alt avg `-0.0293` n `232`; crypto_major avg `0.0277` n `8`; equity avg `0.0572` n `133`; fx avg `0.0056` n `6`; index avg `0.0023` n `26`; metal avg `0.0065` n `20`; unknown avg `0.0` n `792`
- 1h: commodity avg `-0.0173` n `12`; crypto_alt avg `0.1329` n `232`; crypto_major avg `0.0513` n `8`; equity avg `0.0811` n `133`; fx avg `0.0122` n `6`; index avg `-0.0058` n `26`; metal avg `-0.0307` n `20`; unknown avg `-0.0546` n `790`
- 4h: commodity avg `0.0023` n `12`; crypto_alt avg `0.3718` n `232`; crypto_major avg `0.2596` n `8`; equity avg `0.2043` n `133`; fx avg `-0.0181` n `6`; index avg `0.0023` n `26`; metal avg `-0.0236` n `20`; unknown avg `-0.1963` n `772`
- 24h: commodity avg `0.1817` n `12`; crypto_alt avg `-0.2687` n `232`; crypto_major avg `-0.5974` n `8`; equity avg `1.1995` n `133`; fx avg `-0.3779` n `6`; index avg `0.1392` n `26`; metal avg `0.4181` n `20`; unknown avg `-0.2103` n `751`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0649`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0464`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0444`, n `668`, weak_sample_signal
