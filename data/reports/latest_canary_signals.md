# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T02:37:16.374110+00:00`
- Correlation status: `ready`
- Asset price records: `606`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.11` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.1551` n `12`; crypto_alt avg `0.2937` n `228`; crypto_major avg `0.2132` n `8`; equity avg `-0.0792` n `65`; fx avg `0.0166` n `5`; index avg `-0.0218` n `23`; metal avg `-0.2103` n `18`; unknown avg `-0.1734` n `365`
- 1h: commodity avg `0.0933` n `12`; crypto_alt avg `-0.1172` n `228`; crypto_major avg `-0.1041` n `8`; equity avg `-0.1818` n `65`; fx avg `0.0206` n `5`; index avg `-0.0783` n `23`; metal avg `-0.1239` n `18`; unknown avg `-0.1578` n `365`
- 4h: commodity avg `-0.2679` n `12`; crypto_alt avg `0.2292` n `228`; crypto_major avg `-0.1298` n `8`; equity avg `0.8408` n `65`; fx avg `0.1219` n `5`; index avg `0.3976` n `23`; metal avg `0.6473` n `18`; unknown avg `-0.1617` n `365`
- 24h: commodity avg `0.7425` n `12`; crypto_alt avg `2.0298` n `228`; crypto_major avg `-1.3001` n `8`; equity avg `-0.9629` n `65`; fx avg `0.2267` n `5`; index avg `-0.6083` n `23`; metal avg `0.1154` n `18`; unknown avg `0.0282` n `355`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1314`, n `602`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1238`, n `602`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1142`, n `602`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.112`, n `602`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.111`, n `598`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1097`, n `598`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0904`, n `598`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0903`, n `598`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0785`, n `598`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0763`, n `602`, weak_sample_signal
