# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T17:52:29.240907+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.04` n `12`; crypto_alt avg `0.1885` n `232`; crypto_major avg `0.2836` n `8`; equity avg `0.1077` n `133`; fx avg `-0.0037` n `6`; index avg `0.0293` n `26`; metal avg `0.0652` n `20`; unknown avg `16.66` n `792`
- 1h: commodity avg `-0.0606` n `12`; crypto_alt avg `0.0027` n `232`; crypto_major avg `0.1432` n `8`; equity avg `0.248` n `133`; fx avg `-0.0093` n `6`; index avg `0.0367` n `26`; metal avg `0.0803` n `20`; unknown avg `16.4067` n `790`
- 4h: commodity avg `0.2482` n `12`; crypto_alt avg `-0.2561` n `232`; crypto_major avg `-0.1505` n `8`; equity avg `0.4324` n `133`; fx avg `-0.004` n `6`; index avg `0.1443` n `26`; metal avg `-0.0558` n `20`; unknown avg `-0.2234` n `789`
- 24h: commodity avg `0.2496` n `12`; crypto_alt avg `-0.3772` n `232`; crypto_major avg `-0.6244` n `8`; equity avg `0.1704` n `133`; fx avg `-0.3703` n `6`; index avg `0.0898` n `26`; metal avg `0.271` n `20`; unknown avg `-0.3311` n `751`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0513`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.05`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0479`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0447`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0374`, n `668`, weak_sample_signal
