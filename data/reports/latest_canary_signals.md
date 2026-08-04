# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T01:52:29.978109+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0327` n `12`; crypto_alt avg `0.1914` n `230`; crypto_major avg `0.2651` n `8`; equity avg `0.4852` n `107`; fx avg `0.0055` n `6`; index avg `0.1088` n `25`; metal avg `0.0615` n `20`; unknown avg `0.0515` n `780`
- 1h: commodity avg `-0.0454` n `12`; crypto_alt avg `0.5863` n `230`; crypto_major avg `0.7269` n `8`; equity avg `0.776` n `107`; fx avg `0.0216` n `6`; index avg `0.1598` n `25`; metal avg `0.1737` n `20`; unknown avg `-0.0514` n `780`
- 4h: commodity avg `0.1556` n `12`; crypto_alt avg `-0.1253` n `230`; crypto_major avg `0.1322` n `8`; equity avg `0.1383` n `107`; fx avg `-0.018` n `6`; index avg `0.0463` n `25`; metal avg `0.1354` n `20`; unknown avg `-0.2963` n `780`
- 24h: commodity avg `0.2366` n `12`; crypto_alt avg `0.9696` n `230`; crypto_major avg `0.9389` n `8`; equity avg `1.8757` n `107`; fx avg `-0.035` n `6`; index avg `0.2051` n `25`; metal avg `-0.0343` n `20`; unknown avg `0.1926` n `763`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1429`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
