# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T16:37:29.828779+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0329` n `12`; crypto_alt avg `-0.1347` n `232`; crypto_major avg `-0.196` n `8`; equity avg `0.0311` n `133`; fx avg `0.0072` n `6`; index avg `-0.0065` n `26`; metal avg `-0.0229` n `20`; unknown avg `-0.0649` n `792`
- 1h: commodity avg `0.0314` n `12`; crypto_alt avg `0.3123` n `232`; crypto_major avg `0.1638` n `8`; equity avg `0.1145` n `133`; fx avg `0.0064` n `6`; index avg `-0.0043` n `26`; metal avg `-0.0173` n `20`; unknown avg `16.4192` n `790`
- 4h: commodity avg `0.3557` n `12`; crypto_alt avg `0.4136` n `232`; crypto_major avg `0.6584` n `8`; equity avg `0.5155` n `133`; fx avg `-0.106` n `6`; index avg `0.1285` n `26`; metal avg `0.2628` n `20`; unknown avg `0.3601` n `789`
- 24h: commodity avg `0.4328` n `12`; crypto_alt avg `-0.2155` n `232`; crypto_major avg `-0.6572` n `8`; equity avg `0.0194` n `133`; fx avg `-0.3457` n `6`; index avg `0.0337` n `26`; metal avg `0.131` n `20`; unknown avg `-0.3637` n `751`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0534`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0483`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0443`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0425`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0413`, n `668`, weak_sample_signal
