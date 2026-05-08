# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T14:52:13.265539+00:00`
- Correlation status: `ready`
- Asset price records: `655`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.046` n `12`; crypto_alt avg `0.1552` n `228`; crypto_major avg `0.1059` n `8`; equity avg `0.3034` n `65`; fx avg `-0.0077` n `5`; index avg `0.138` n `23`; metal avg `0.0845` n `18`; unknown avg `0.036` n `375`
- 1h: commodity avg `0.4195` n `12`; crypto_alt avg `0.9138` n `228`; crypto_major avg `0.5913` n `8`; equity avg `0.3874` n `65`; fx avg `0.0074` n `5`; index avg `-0.0574` n `23`; metal avg `-0.3127` n `18`; unknown avg `-0.0307` n `375`
- 4h: commodity avg `0.3465` n `12`; crypto_alt avg `0.5841` n `228`; crypto_major avg `0.1686` n `8`; equity avg `0.9879` n `65`; fx avg `-0.0314` n `5`; index avg `0.6047` n `23`; metal avg `-0.0843` n `18`; unknown avg `0.0403` n `375`
- 24h: commodity avg `1.969` n `12`; crypto_alt avg `2.3362` n `228`; crypto_major avg `-0.028` n `8`; equity avg `0.6851` n `65`; fx avg `0.2253` n `5`; index avg `0.3099` n `23`; metal avg `-0.9239` n `18`; unknown avg `0.0179` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1247`, n `647`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1214`, n `647`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1094`, n `651`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0972`, n `647`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0961`, n `647`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.094`, n `651`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0882`, n `651`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0872`, n `651`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.072`, n `651`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0717`, n `651`, weak_sample_signal
