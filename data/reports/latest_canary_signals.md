# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T02:37:27.547676+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0462` n `12`; crypto_alt avg `-0.0375` n `232`; crypto_major avg `-0.045` n `8`; equity avg `-0.182` n `130`; fx avg `0.0184` n `6`; index avg `-0.0356` n `26`; metal avg `-0.1345` n `20`; unknown avg `-0.115` n `792`
- 1h: commodity avg `-0.0012` n `12`; crypto_alt avg `-0.268` n `232`; crypto_major avg `-0.1618` n `8`; equity avg `-0.2209` n `130`; fx avg `-0.0133` n `6`; index avg `-0.0446` n `26`; metal avg `-0.1514` n `20`; unknown avg `0.161` n `790`
- 4h: commodity avg `0.0901` n `12`; crypto_alt avg `0.2446` n `232`; crypto_major avg `-0.3754` n `8`; equity avg `-0.1633` n `130`; fx avg `0.0113` n `6`; index avg `0.0205` n `26`; metal avg `-0.0866` n `20`; unknown avg `0.0272` n `790`
- 24h: commodity avg `0.3485` n `12`; crypto_alt avg `1.6326` n `231`; crypto_major avg `1.3778` n `8`; equity avg `1.2642` n `130`; fx avg `-0.0167` n `6`; index avg `0.161` n `26`; metal avg `0.0051` n `20`; unknown avg `0.2138` n `751`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0567`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0522`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0501`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0492`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0459`, n `668`, weak_sample_signal
