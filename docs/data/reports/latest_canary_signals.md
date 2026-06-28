# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T18:37:29.273879+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0015` n `12`; crypto_alt avg `-0.1746` n `228`; crypto_major avg `-0.1456` n `8`; equity avg `-0.0157` n `88`; fx avg `-0.0113` n `6`; index avg `-0.0077` n `23`; metal avg `0.009` n `20`; unknown avg `0.5149` n `764`
- 1h: commodity avg `-0.0337` n `12`; crypto_alt avg `-0.0851` n `228`; crypto_major avg `-0.0902` n `8`; equity avg `0.0194` n `88`; fx avg `-0.0144` n `6`; index avg `0.0083` n `23`; metal avg `0.0258` n `20`; unknown avg `0.4409` n `764`
- 4h: commodity avg `-0.0105` n `12`; crypto_alt avg `-1.131` n `228`; crypto_major avg `-0.909` n `8`; equity avg `-0.1014` n `88`; fx avg `-0.0196` n `6`; index avg `-0.025` n `23`; metal avg `-0.0116` n `20`; unknown avg `-0.5275` n `764`
- 24h: commodity avg `0.317` n `12`; crypto_alt avg `-0.9348` n `228`; crypto_major avg `-1.5509` n `8`; equity avg `0.0519` n `88`; fx avg `-0.0368` n `6`; index avg `-0.0217` n `23`; metal avg `-0.0181` n `20`; unknown avg `14.8934` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.19`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1868`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
