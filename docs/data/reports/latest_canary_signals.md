# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T01:22:19.389670+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3281` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.029` n `12`; crypto_alt avg `-0.5148` n `228`; crypto_major avg `-0.1519` n `8`; equity avg `-0.0448` n `67`; fx avg `0.0063` n `6`; index avg `-0.0465` n `23`; metal avg `-0.3821` n `18`; unknown avg `0.7967` n `419`
- 1h: commodity avg `-0.093` n `12`; crypto_alt avg `-0.6152` n `228`; crypto_major avg `-0.1806` n `8`; equity avg `0.2248` n `67`; fx avg `-0.0093` n `6`; index avg `0.0796` n `23`; metal avg `-0.6176` n `18`; unknown avg `1.0526` n `419`
- 4h: commodity avg `0.2702` n `12`; crypto_alt avg `-2.3679` n `228`; crypto_major avg `-1.523` n `8`; equity avg `-0.3267` n `67`; fx avg `0.0132` n `6`; index avg `-0.1949` n `23`; metal avg `-0.6084` n `18`; unknown avg `1.9801` n `419`
- 24h: commodity avg `-0.8163` n `12`; crypto_alt avg `-2.7734` n `228`; crypto_major avg `-1.8043` n `8`; equity avg `-0.6998` n `67`; fx avg `-0.0697` n `6`; index avg `-0.776` n `23`; metal avg `-2.0467` n `18`; unknown avg `-0.1325` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1822`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1775`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1741`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1649`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1581`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1451`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1446`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1401`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1376`, n `668`, weak_sample_signal
