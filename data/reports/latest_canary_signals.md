# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T18:22:30.107020+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0624` n `12`; crypto_alt avg `0.0148` n `229`; crypto_major avg `0.0425` n `8`; equity avg `-0.0698` n `92`; fx avg `-0.0038` n `6`; index avg `-0.0161` n `25`; metal avg `0.007` n `20`; unknown avg `0.0028` n `765`
- 1h: commodity avg `0.0068` n `12`; crypto_alt avg `-0.0457` n `229`; crypto_major avg `0.0485` n `8`; equity avg `0.0286` n `92`; fx avg `-0.0166` n `6`; index avg `0.0258` n `25`; metal avg `-0.045` n `20`; unknown avg `-0.0334` n `765`
- 4h: commodity avg `0.0478` n `12`; crypto_alt avg `0.2502` n `229`; crypto_major avg `0.2217` n `8`; equity avg `0.3953` n `92`; fx avg `-0.0404` n `6`; index avg `0.1004` n `25`; metal avg `-0.0567` n `20`; unknown avg `-0.1242` n `765`
- 24h: commodity avg `-0.385` n `12`; crypto_alt avg `0.5325` n `229`; crypto_major avg `0.7319` n `8`; equity avg `-0.8303` n `92`; fx avg `-0.1717` n `6`; index avg `0.0033` n `25`; metal avg `-0.1254` n `20`; unknown avg `-0.1523` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
