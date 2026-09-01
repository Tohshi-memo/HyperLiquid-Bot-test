# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T03:37:26.237204+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0141` n `12`; crypto_alt avg `0.3451` n `232`; crypto_major avg `0.4648` n `8`; equity avg `0.1152` n `130`; fx avg `-0.0024` n `6`; index avg `0.0113` n `26`; metal avg `0.0315` n `20`; unknown avg `-0.1364` n `792`
- 1h: commodity avg `-0.0459` n `12`; crypto_alt avg `0.6639` n `232`; crypto_major avg `0.6417` n `8`; equity avg `0.2063` n `130`; fx avg `-0.0055` n `6`; index avg `0.0317` n `26`; metal avg `0.081` n `20`; unknown avg `-0.0909` n `790`
- 4h: commodity avg `0.0138` n `12`; crypto_alt avg `0.9626` n `232`; crypto_major avg `0.4551` n `8`; equity avg `0.0695` n `130`; fx avg `0.0201` n `6`; index avg `0.0421` n `26`; metal avg `0.0148` n `20`; unknown avg `0.4135` n `790`
- 24h: commodity avg `0.3657` n `12`; crypto_alt avg `1.8505` n `231`; crypto_major avg `1.9481` n `8`; equity avg `1.2819` n `130`; fx avg `-0.0168` n `6`; index avg `0.1323` n `26`; metal avg `0.0168` n `20`; unknown avg `0.2812` n `751`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0561`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0531`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0506`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0479`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0433`, n `668`, weak_sample_signal
