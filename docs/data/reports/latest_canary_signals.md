# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T16:22:31.373972+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0444` n `12`; crypto_alt avg `0.5209` n `233`; crypto_major avg `0.6651` n `8`; equity avg `0.3074` n `136`; fx avg `-0.0023` n `6`; index avg `0.0519` n `27`; metal avg `0.0637` n `20`; unknown avg `2.5565` n `894`
- 1h: commodity avg `-0.1183` n `12`; crypto_alt avg `0.5972` n `233`; crypto_major avg `0.7503` n `8`; equity avg `0.5519` n `136`; fx avg `-0.0107` n `6`; index avg `0.152` n `27`; metal avg `0.1451` n `20`; unknown avg `1.8452` n `892`
- 4h: commodity avg `-0.0883` n `12`; crypto_alt avg `0.161` n `233`; crypto_major avg `0.6228` n `8`; equity avg `1.0398` n `136`; fx avg `-0.0039` n `6`; index avg `0.0954` n `27`; metal avg `0.0814` n `20`; unknown avg `1.0653` n `872`
- 24h: commodity avg `0.4324` n `12`; crypto_alt avg `0.113` n `233`; crypto_major avg `1.8462` n `8`; equity avg `-0.3079` n `136`; fx avg `0.0379` n `6`; index avg `-0.1709` n `27`; metal avg `-0.3443` n `20`; unknown avg `1.0451` n `636`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
