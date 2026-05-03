# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T17:00:25.926612+00:00`
- Correlation status: `ready`
- Asset price records: `187`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1204` n `7`; crypto_alt avg `-0.0734` n `223`; crypto_major avg `-0.121` n `7`; equity avg `-0.0168` n `42`; fx avg `-0.0051` n `4`; index avg `-0.0146` n `9`; metal avg `-0.0035` n `7`; unknown avg `0.0037` n `313`
- 1h: commodity avg `0.0182` n `7`; crypto_alt avg `-0.099` n `223`; crypto_major avg `-0.0469` n `7`; equity avg `0.1033` n `42`; fx avg `0.0008` n `4`; index avg `0.0317` n `9`; metal avg `0.0357` n `7`; unknown avg `0.2166` n `313`
- 4h: commodity avg `-0.305` n `7`; crypto_alt avg `-0.191` n `223`; crypto_major avg `-0.1335` n `7`; equity avg `0.1` n `42`; fx avg `0.0128` n `4`; index avg `0.0287` n `9`; metal avg `0.141` n `7`; unknown avg `0.1483` n `313`
- 24h: commodity avg `-0.536` n `7`; crypto_alt avg `-0.5098` n `223`; crypto_major avg `-0.2086` n `7`; equity avg `0.4729` n `42`; fx avg `0.0798` n `4`; index avg `0.0852` n `9`; metal avg `0.3237` n `7`; unknown avg `0.0376` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4013`, n `183`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3863`, n `179`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3835`, n `183`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.3806`, n `183`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3801`, n `179`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.367`, n `183`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3259`, n `183`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.3215`, n `179`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3084`, n `179`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.3078`, n `183`, moderate_sample_signal
