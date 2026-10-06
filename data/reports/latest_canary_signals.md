# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T09:22:30.328743+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0323` n `13`; crypto_alt avg `-0.047` n `235`; crypto_major avg `0.0677` n `8`; equity avg `-0.0211` n `149`; fx avg `-0.007` n `6`; index avg `-0.0115` n `26`; metal avg `0.0033` n `20`; unknown avg `-0.1178` n `1074`
- 1h: commodity avg `-0.2143` n `13`; crypto_alt avg `-0.0303` n `235`; crypto_major avg `0.225` n `8`; equity avg `0.0317` n `149`; fx avg `0.0107` n `6`; index avg `-0.0007` n `26`; metal avg `0.0191` n `20`; unknown avg `0.5444` n `1072`
- 4h: commodity avg `-0.4515` n `13`; crypto_alt avg `0.2981` n `235`; crypto_major avg `0.2531` n `8`; equity avg `0.1893` n `149`; fx avg `0.02` n `6`; index avg `0.0513` n `26`; metal avg `0.1315` n `20`; unknown avg `-0.1246` n `976`
- 24h: commodity avg `-0.6289` n `13`; crypto_alt avg `-0.8026` n `235`; crypto_major avg `-0.2593` n `8`; equity avg `0.3818` n `149`; fx avg `0.0126` n `6`; index avg `0.1897` n `26`; metal avg `-0.1978` n `20`; unknown avg `0.1136` n `876`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1837`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1671`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1588`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.15`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
