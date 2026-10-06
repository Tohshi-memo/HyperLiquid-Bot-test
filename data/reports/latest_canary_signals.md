# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T23:52:29.831423+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0024` n `13`; crypto_alt avg `0.0433` n `235`; crypto_major avg `0.1469` n `8`; equity avg `-0.0061` n `150`; fx avg `0.0026` n `6`; index avg `-0.0039` n `26`; metal avg `-0.0084` n `20`; unknown avg `0.6285` n `1076`
- 1h: commodity avg `0.07` n `13`; crypto_alt avg `0.1273` n `235`; crypto_major avg `0.1045` n `8`; equity avg `0.0168` n `150`; fx avg `0.0166` n `6`; index avg `-0.0051` n `26`; metal avg `0.0333` n `20`; unknown avg `0.5343` n `1074`
- 4h: commodity avg `0.1071` n `13`; crypto_alt avg `0.0819` n `235`; crypto_major avg `0.0749` n `8`; equity avg `0.1668` n `150`; fx avg `0.0151` n `6`; index avg `0.026` n `26`; metal avg `0.0027` n `20`; unknown avg `0.1726` n `990`
- 24h: commodity avg `0.4025` n `13`; crypto_alt avg `-1.2705` n `235`; crypto_major avg `-0.747` n `8`; equity avg `0.3275` n `149`; fx avg `0.0895` n `6`; index avg `-0.0143` n `26`; metal avg `0.0945` n `20`; unknown avg `870.7619` n `914`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1638`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1507`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1488`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
