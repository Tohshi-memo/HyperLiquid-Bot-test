# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T23:07:34.122121+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0196` n `12`; crypto_alt avg `0.3396` n `234`; crypto_major avg `0.3132` n `8`; equity avg `0.0154` n `140`; fx avg `-0.0035` n `6`; index avg `0.0` n `26`; metal avg `0.0158` n `20`; unknown avg `0.4448` n `943`
- 1h: commodity avg `-0.0066` n `12`; crypto_alt avg `1.2182` n `234`; crypto_major avg `0.727` n `8`; equity avg `0.0657` n `140`; fx avg `0.0111` n `6`; index avg `0.0071` n `26`; metal avg `0.0202` n `20`; unknown avg `0.3651` n `943`
- 4h: commodity avg `-0.0367` n `12`; crypto_alt avg `1.4532` n `234`; crypto_major avg `0.2822` n `8`; equity avg `0.191` n `140`; fx avg `-0.0253` n `6`; index avg `0.019` n `26`; metal avg `0.0433` n `20`; unknown avg `0.2466` n `906`
- 24h: commodity avg `0.1739` n `12`; crypto_alt avg `2.6718` n `234`; crypto_major avg `0.1265` n `8`; equity avg `0.7307` n `140`; fx avg `-0.2836` n `6`; index avg `0.0933` n `26`; metal avg `0.2043` n `20`; unknown avg `1.5012` n `836`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1242`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
