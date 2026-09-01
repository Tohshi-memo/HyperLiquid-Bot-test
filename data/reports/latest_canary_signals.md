# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T05:52:25.734356+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0714` n `12`; crypto_alt avg `0.2374` n `232`; crypto_major avg `0.1739` n `8`; equity avg `0.1128` n `130`; fx avg `0.0064` n `6`; index avg `0.0208` n `26`; metal avg `0.044` n `20`; unknown avg `1.1454` n `792`
- 1h: commodity avg `-0.1348` n `12`; crypto_alt avg `0.5973` n `232`; crypto_major avg `0.4988` n `8`; equity avg `0.1602` n `130`; fx avg `-0.0387` n `6`; index avg `0.0561` n `26`; metal avg `0.1186` n `20`; unknown avg `-0.2291` n `790`
- 4h: commodity avg `-0.0266` n `12`; crypto_alt avg `0.7307` n `232`; crypto_major avg `0.7257` n `8`; equity avg `0.2622` n `130`; fx avg `-0.0195` n `6`; index avg `0.0522` n `26`; metal avg `0.053` n `20`; unknown avg `-0.3463` n `790`
- 24h: commodity avg `0.2232` n `12`; crypto_alt avg `1.9771` n `232`; crypto_major avg `1.6526` n `8`; equity avg `0.9759` n `130`; fx avg `-0.0111` n `6`; index avg `0.0902` n `26`; metal avg `-0.0459` n `20`; unknown avg `0.4457` n `751`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0539`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0527`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0514`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0489`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0488`, n `668`, weak_sample_signal
