# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T02:52:16.170325+00:00`
- Correlation status: `ready`
- Asset price records: `607`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.1` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.3179` n `12`; crypto_alt avg `0.1924` n `228`; crypto_major avg `0.0806` n `8`; equity avg `-0.0084` n `65`; fx avg `-0.0259` n `5`; index avg `0.0501` n `23`; metal avg `0.1644` n `18`; unknown avg `-0.1199` n `365`
- 1h: commodity avg `-0.1595` n `12`; crypto_alt avg `0.1244` n `228`; crypto_major avg `-0.0179` n `8`; equity avg `-0.1974` n `65`; fx avg `0.0036` n `5`; index avg `-0.0331` n `23`; metal avg `-0.1366` n `18`; unknown avg `-0.2932` n `365`
- 4h: commodity avg `-0.5449` n `12`; crypto_alt avg `0.2737` n `228`; crypto_major avg `-0.1113` n `8`; equity avg `0.7411` n `65`; fx avg `0.1072` n `5`; index avg `0.4732` n `23`; metal avg `0.9346` n `18`; unknown avg `-0.2229` n `365`
- 24h: commodity avg `0.4411` n `12`; crypto_alt avg `2.0913` n `228`; crypto_major avg `-1.2729` n `8`; equity avg `-0.9387` n `65`; fx avg `0.1832` n `5`; index avg `-0.6067` n `23`; metal avg `0.2177` n `18`; unknown avg `0.0891` n `355`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1316`, n `603`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1237`, n `603`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1142`, n `603`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1118`, n `603`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1111`, n `599`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1097`, n `599`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0906`, n `599`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0902`, n `599`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0788`, n `599`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0762`, n `603`, weak_sample_signal
