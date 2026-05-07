# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T17:12:15.453029+00:00`
- Correlation status: `ready`
- Asset price records: `568`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.307` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.0019` n `12`; crypto_alt avg `0.0894` n `228`; crypto_major avg `0.0397` n `8`; equity avg `-0.3434` n `65`; fx avg `-0.0012` n `5`; index avg `-0.1114` n `23`; metal avg `0.0771` n `18`; unknown avg `-0.0384` n `365`
- 1h: commodity avg `0.5936` n `12`; crypto_alt avg `0.7387` n `228`; crypto_major avg `0.2351` n `8`; equity avg `-0.3869` n `65`; fx avg `0.0168` n `5`; index avg `-0.2619` n `23`; metal avg `-0.0352` n `18`; unknown avg `1.2494` n `365`
- 4h: commodity avg `1.9191` n `12`; crypto_alt avg `-0.9687` n `228`; crypto_major avg `-1.3879` n `8`; equity avg `-1.7331` n `65`; fx avg `0.0605` n `5`; index avg `-0.84` n `23`; metal avg `-1.1237` n `18`; unknown avg `-0.5208` n `365`
- 24h: commodity avg `0.4873` n `12`; crypto_alt avg `0.1763` n `228`; crypto_major avg `-2.1324` n `8`; equity avg `-0.8094` n `65`; fx avg `0.1992` n `5`; index avg `-0.4406` n `23`; metal avg `0.8625` n `18`; unknown avg `0.7008` n `353`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1347`, n `564`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1154`, n `564`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1152`, n `564`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1062`, n `564`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1007`, n `560`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0952`, n `560`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0925`, n `560`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0909`, n `560`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0839`, n `560`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0739`, n `564`, weak_sample_signal
