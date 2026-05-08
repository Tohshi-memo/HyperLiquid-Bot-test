# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T01:37:14.863665+00:00`
- Correlation status: `ready`
- Asset price records: `602`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.15` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0683` n `12`; crypto_alt avg `0.0046` n `228`; crypto_major avg `-0.0364` n `8`; equity avg `-0.0363` n `65`; fx avg `0.0196` n `5`; index avg `0.0218` n `23`; metal avg `-0.1119` n `18`; unknown avg `-0.0882` n `365`
- 1h: commodity avg `-0.351` n `12`; crypto_alt avg `-0.2543` n `228`; crypto_major avg `-0.3461` n `8`; equity avg `0.159` n `65`; fx avg `0.0268` n `5`; index avg `0.1634` n `23`; metal avg `0.4749` n `18`; unknown avg `0.0444` n `365`
- 4h: commodity avg `-0.7195` n `12`; crypto_alt avg `0.088` n `228`; crypto_major avg `-0.337` n `8`; equity avg `0.7679` n `65`; fx avg `0.1007` n `5`; index avg `0.5271` n `23`; metal avg `0.8302` n `18`; unknown avg `0.1052` n `365`
- 24h: commodity avg `0.5437` n `12`; crypto_alt avg `1.8697` n `228`; crypto_major avg `-1.5574` n `8`; equity avg `-0.5948` n `65`; fx avg `0.2057` n `5`; index avg `-0.4895` n `23`; metal avg `0.1207` n `18`; unknown avg `-0.4106` n `355`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1337`, n `598`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1165`, n `598`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1117`, n `598`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.108`, n `594`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1076`, n `598`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1064`, n `594`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0912`, n `594`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0901`, n `594`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.079`, n `594`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0725`, n `598`, weak_sample_signal
