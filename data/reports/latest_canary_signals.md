# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T20:52:26.414217+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0171` n `13`; crypto_alt avg `0.1113` n `238`; crypto_major avg `-0.0042` n `8`; equity avg `0.0245` n `156`; fx avg `0.0019` n `6`; index avg `-0.0013` n `27`; metal avg `0.001` n `20`; unknown avg `3.6159` n `1262`
- 1h: commodity avg `0.0327` n `10`; crypto_alt avg `-0.0955` n `231`; crypto_major avg `-0.0975` n `8`; equity avg `-0.0026` n `118`; fx avg `0.0082` n `5`; index avg `-0.0233` n `8`; metal avg `-0.0046` n `16`; unknown avg `0.742` n `1171`
- 4h: commodity avg `0.0049` n `13`; crypto_alt avg `-0.8091` n `238`; crypto_major avg `-0.0883` n `8`; equity avg `0.0394` n `156`; fx avg `0.0023` n `6`; index avg `-0.0027` n `27`; metal avg `-0.0144` n `20`; unknown avg `0.536` n `1164`
- 24h: commodity avg `-0.0669` n `13`; crypto_alt avg `0.4969` n `238`; crypto_major avg `0.1048` n `8`; equity avg `0.2344` n `156`; fx avg `-0.0175` n `6`; index avg `-0.0259` n `27`; metal avg `0.1` n `20`; unknown avg `1.5409` n `1073`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1491`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1461`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1419`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1333`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
