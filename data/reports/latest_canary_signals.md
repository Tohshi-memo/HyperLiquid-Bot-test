# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T07:52:27.646408+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0308` n `12`; crypto_alt avg `0.143` n `231`; crypto_major avg `0.1799` n `8`; equity avg `0.0575` n `127`; fx avg `-0.0039` n `6`; index avg `0.0091` n `26`; metal avg `0.003` n `20`; unknown avg `0.0108` n `791`
- 1h: commodity avg `-0.0628` n `12`; crypto_alt avg `0.1327` n `231`; crypto_major avg `0.2195` n `8`; equity avg `0.1943` n `127`; fx avg `-0.0167` n `6`; index avg `0.0195` n `26`; metal avg `-0.1138` n `20`; unknown avg `0.0407` n `791`
- 4h: commodity avg `-0.1957` n `12`; crypto_alt avg `0.2594` n `231`; crypto_major avg `0.4619` n `8`; equity avg `0.1479` n `127`; fx avg `-0.002` n `6`; index avg `-0.0291` n `26`; metal avg `-0.2678` n `20`; unknown avg `0.164` n `775`
- 24h: commodity avg `0.3363` n `12`; crypto_alt avg `0.4621` n `231`; crypto_major avg `0.6227` n `8`; equity avg `1.6833` n `127`; fx avg `-0.0951` n `6`; index avg `0.2709` n `26`; metal avg `-0.3967` n `20`; unknown avg `0.4306` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1249`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
