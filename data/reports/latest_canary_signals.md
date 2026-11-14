# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T23:37:26.291982+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.7927` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `3.6733` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-3.4327` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-3.0853` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.004` n `13`; crypto_alt avg `-0.0394` n `239`; crypto_major avg `-0.4335` n `8`; equity avg `-0.0699` n `162`; fx avg `-0.0085` n `6`; index avg `-0.0102` n `27`; metal avg `-0.0514` n `20`; unknown avg `-0.0989` n `1262`
- 1h: commodity avg `0.0186` n `13`; crypto_alt avg `0.3692` n `239`; crypto_major avg `0.0987` n `8`; equity avg `-0.1073` n `162`; fx avg `0.0008` n `6`; index avg `-0.0079` n `27`; metal avg `0.0181` n `20`; unknown avg `-0.0505` n `1228`
- 4h: commodity avg `0.1075` n `13`; crypto_alt avg `-3.0524` n `239`; crypto_major avg `-3.6852` n `8`; equity avg `-0.5999` n `162`; fx avg `0.004` n `6`; index avg `-0.0119` n `27`; metal avg `-0.2525` n `20`; unknown avg `4.0751` n `1176`
- 24h: commodity avg `0.0354` n `13`; crypto_alt avg `-9.0791` n `239`; crypto_major avg `-8.9247` n `8`; equity avg `-1.6396` n `162`; fx avg `0.0036` n `6`; index avg `-0.1351` n `27`; metal avg `-0.4863` n `20`; unknown avg `46.2749` n `1070`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1393`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
