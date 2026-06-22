# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T07:37:31.061362+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0677` n `12`; crypto_alt avg `-0.0193` n `228`; crypto_major avg `0.0881` n `8`; equity avg `-0.0628` n `79`; fx avg `-0.0071` n `6`; index avg `-0.0049` n `23`; metal avg `-0.1252` n `18`; unknown avg `0.0032` n `701`
- 1h: commodity avg `0.1388` n `12`; crypto_alt avg `0.2928` n `228`; crypto_major avg `0.6051` n `8`; equity avg `0.1947` n `79`; fx avg `-0.0034` n `6`; index avg `0.0218` n `23`; metal avg `-0.0918` n `18`; unknown avg `0.0418` n `701`
- 4h: commodity avg `0.0314` n `12`; crypto_alt avg `0.179` n `228`; crypto_major avg `0.3998` n `8`; equity avg `0.2647` n `79`; fx avg `0.0009` n `6`; index avg `0.0203` n `23`; metal avg `0.322` n `18`; unknown avg `0.4495` n `669`
- 24h: commodity avg `-0.1709` n `12`; crypto_alt avg `0.0143` n `228`; crypto_major avg `-0.0334` n `8`; equity avg `-0.2602` n `79`; fx avg `0.1256` n `6`; index avg `0.0134` n `23`; metal avg `0.3636` n `18`; unknown avg `-0.3516` n `643`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0637`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
