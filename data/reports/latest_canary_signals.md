# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T20:37:32.721418+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.035` n `12`; crypto_alt avg `0.052` n `232`; crypto_major avg `0.0816` n `8`; equity avg `0.1125` n `133`; fx avg `0.0043` n `6`; index avg `-0.0007` n `26`; metal avg `0.0118` n `20`; unknown avg `15.6944` n `792`
- 1h: commodity avg `-0.0281` n `12`; crypto_alt avg `0.4935` n `232`; crypto_major avg `0.5115` n `8`; equity avg `-0.0577` n `133`; fx avg `-0.0283` n `6`; index avg `-0.0319` n `26`; metal avg `0.0253` n `20`; unknown avg `0.1876` n `778`
- 4h: commodity avg `0.012` n `12`; crypto_alt avg `0.0304` n `232`; crypto_major avg `0.1796` n `8`; equity avg `0.5547` n `133`; fx avg `-0.0286` n `6`; index avg `0.0102` n `26`; metal avg `0.1173` n `20`; unknown avg `-0.5176` n `778`
- 24h: commodity avg `0.1202` n `12`; crypto_alt avg `-0.2015` n `232`; crypto_major avg `-0.2974` n `8`; equity avg `0.6667` n `133`; fx avg `-0.3873` n `6`; index avg `0.0866` n `26`; metal avg `0.5183` n `20`; unknown avg `-0.3052` n `751`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0556`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0496`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0457`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0447`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0422`, n `668`, weak_sample_signal
