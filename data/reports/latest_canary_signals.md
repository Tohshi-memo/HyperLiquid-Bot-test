# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T03:22:15.634565+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0967` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0182` n `12`; crypto_alt avg `0.0456` n `228`; crypto_major avg `0.0897` n `8`; equity avg `0.0574` n `67`; fx avg `-0.0119` n `6`; index avg `0.0035` n `23`; metal avg `0.2083` n `18`; unknown avg `0.1186` n `407`
- 1h: commodity avg `-0.0981` n `12`; crypto_alt avg `-0.2334` n `228`; crypto_major avg `-0.2244` n `8`; equity avg `0.0477` n `67`; fx avg `-0.0283` n `6`; index avg `-0.0013` n `23`; metal avg `0.1644` n `18`; unknown avg `-0.3608` n `407`
- 4h: commodity avg `0.2897` n `12`; crypto_alt avg `-1.5566` n `228`; crypto_major avg `-1.2818` n `8`; equity avg `-0.6466` n `67`; fx avg `-0.1289` n `6`; index avg `-0.1851` n `23`; metal avg `-0.8092` n `18`; unknown avg `-0.1812` n `405`
- 24h: commodity avg `0.2431` n `12`; crypto_alt avg `-0.2748` n `228`; crypto_major avg `-0.9173` n `8`; equity avg `-0.359` n `67`; fx avg `-0.0133` n `6`; index avg `0.0245` n `23`; metal avg `-0.0933` n `18`; unknown avg `0.1864` n `387`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.169`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1632`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1587`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1462`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1449`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1385`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1383`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1312`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
