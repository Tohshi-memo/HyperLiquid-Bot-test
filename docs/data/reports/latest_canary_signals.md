# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T04:07:31.141975+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0242` n `12`; crypto_alt avg `0.0064` n `229`; crypto_major avg `0.0403` n `8`; equity avg `0.1278` n `91`; fx avg `-0.0099` n `6`; index avg `0.0306` n `25`; metal avg `0.0073` n `20`; unknown avg `-0.1201` n `765`
- 1h: commodity avg `0.049` n `12`; crypto_alt avg `0.0467` n `229`; crypto_major avg `0.2441` n `8`; equity avg `-0.0759` n `91`; fx avg `0.0079` n `6`; index avg `0.0061` n `25`; metal avg `-0.0493` n `20`; unknown avg `0.937` n `765`
- 4h: commodity avg `0.0821` n `12`; crypto_alt avg `0.967` n `229`; crypto_major avg `1.4057` n `8`; equity avg `0.4025` n `91`; fx avg `-0.012` n `6`; index avg `0.1061` n `25`; metal avg `0.2356` n `20`; unknown avg `1.3691` n `763`
- 24h: commodity avg `-0.9858` n `12`; crypto_alt avg `1.7136` n `229`; crypto_major avg `1.8912` n `8`; equity avg `1.869` n `91`; fx avg `0.0254` n `6`; index avg `0.4576` n `25`; metal avg `0.9667` n `20`; unknown avg `0.1902` n `746`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
