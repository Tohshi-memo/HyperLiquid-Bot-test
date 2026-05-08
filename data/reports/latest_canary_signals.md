# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T16:22:13.855475+00:00`
- Correlation status: `ready`
- Asset price records: `661`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.3682` n `12`; crypto_alt avg `0.1706` n `228`; crypto_major avg `0.0232` n `8`; equity avg `0.0566` n `65`; fx avg `0.0141` n `5`; index avg `0.0066` n `23`; metal avg `0.0828` n `18`; unknown avg `-0.0368` n `375`
- 1h: commodity avg `0.3375` n `12`; crypto_alt avg `0.6696` n `228`; crypto_major avg `0.4419` n `8`; equity avg `0.05` n `65`; fx avg `0.0026` n `5`; index avg `0.0826` n `23`; metal avg `0.1096` n `18`; unknown avg `0.0053` n `375`
- 4h: commodity avg `0.9225` n `12`; crypto_alt avg `1.0651` n `228`; crypto_major avg `0.3505` n `8`; equity avg `1.1382` n `65`; fx avg `-0.0397` n `5`; index avg `0.4875` n `23`; metal avg `-0.1365` n `18`; unknown avg `-0.0192` n `375`
- 24h: commodity avg `0.9811` n `12`; crypto_alt avg `2.9403` n `228`; crypto_major avg `0.4436` n `8`; equity avg `2.443` n `65`; fx avg `0.1571` n `5`; index avg `0.9675` n `23`; metal avg `0.1725` n `18`; unknown avg `0.5738` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1206`, n `653`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1174`, n `657`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1164`, n `653`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1029`, n `653`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1005`, n `657`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0966`, n `653`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0836`, n `657`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0835`, n `657`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0725`, n `657`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0718`, n `657`, weak_sample_signal
