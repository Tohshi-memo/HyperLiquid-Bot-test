# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T04:07:13.355621+00:00`
- Correlation status: `ready`
- Asset price records: `612`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.05` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0478` n `12`; crypto_alt avg `-0.0127` n `228`; crypto_major avg `0.0012` n `8`; equity avg `0.0756` n `65`; fx avg `0.0039` n `5`; index avg `0.0008` n `23`; metal avg `0.0236` n `18`; unknown avg `-0.057` n `365`
- 1h: commodity avg `-0.0138` n `12`; crypto_alt avg `0.7599` n `228`; crypto_major avg `0.3268` n `8`; equity avg `0.094` n `65`; fx avg `0.0255` n `5`; index avg `0.0385` n `23`; metal avg `0.2062` n `18`; unknown avg `-0.0418` n `365`
- 4h: commodity avg `-0.3274` n `12`; crypto_alt avg `0.0054` n `228`; crypto_major avg `-0.4381` n `8`; equity avg `0.334` n `65`; fx avg `0.0869` n `5`; index avg `0.1679` n `23`; metal avg `0.4962` n `18`; unknown avg `-0.27` n `365`
- 24h: commodity avg `0.3967` n `12`; crypto_alt avg `2.7559` n `228`; crypto_major avg `-1.0085` n `8`; equity avg `-0.9266` n `65`; fx avg `0.1601` n `5`; index avg `-0.5973` n `23`; metal avg `0.5427` n `18`; unknown avg `0.121` n `355`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1291`, n `608`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1163`, n `608`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1108`, n `604`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1098`, n `608`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1092`, n `604`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1082`, n `608`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0898`, n `604`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0891`, n `604`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0791`, n `604`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0757`, n `608`, weak_sample_signal
