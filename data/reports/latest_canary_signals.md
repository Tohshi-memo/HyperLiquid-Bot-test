# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T20:37:20.413576+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1302` n `12`; crypto_alt avg `0.1044` n `228`; crypto_major avg `0.0785` n `8`; equity avg `0.0058` n `66`; fx avg `-0.0002` n `6`; index avg `-0.0459` n `23`; metal avg `0.0091` n `18`; unknown avg `-0.0438` n `383`
- 1h: commodity avg `-0.1791` n `12`; crypto_alt avg `0.1026` n `228`; crypto_major avg `0.0028` n `8`; equity avg `-0.0935` n `66`; fx avg `0.0285` n `6`; index avg `-0.0665` n `23`; metal avg `-0.1141` n `18`; unknown avg `-0.1952` n `383`
- 4h: commodity avg `0.1189` n `12`; crypto_alt avg `0.1674` n `228`; crypto_major avg `0.0071` n `8`; equity avg `0.0669` n `66`; fx avg `0.0886` n `6`; index avg `-0.0246` n `23`; metal avg `-0.4353` n `18`; unknown avg `1.2231` n `383`
- 24h: commodity avg `1.2208` n `12`; crypto_alt avg `-0.1724` n `228`; crypto_major avg `0.0218` n `8`; equity avg `0.1073` n `66`; fx avg `0.0687` n `6`; index avg `-0.5386` n `23`; metal avg `-2.5925` n `18`; unknown avg `0.8638` n `363`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0691`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0544`, n `668`, weak_sample_signal
