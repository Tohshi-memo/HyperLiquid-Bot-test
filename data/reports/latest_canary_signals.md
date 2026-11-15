# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T00:37:27.563100+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.7927` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.6268` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.6074` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0039` n `13`; crypto_alt avg `-0.5293` n `239`; crypto_major avg `-0.4972` n `8`; equity avg `-0.1115` n `162`; fx avg `0.0` n `6`; index avg `-0.0096` n `27`; metal avg `-0.0557` n `20`; unknown avg `-0.0828` n `1262`
- 1h: commodity avg `0.0124` n `13`; crypto_alt avg `0.9883` n `239`; crypto_major avg `1.14` n `8`; equity avg `0.2423` n `162`; fx avg `0.0012` n `6`; index avg `0.0165` n `27`; metal avg `-0.0043` n `20`; unknown avg `0.9233` n `1252`
- 4h: commodity avg `0.083` n `13`; crypto_alt avg `-0.7692` n `239`; crypto_major avg `-1.7867` n `8`; equity avg `-0.1793` n `162`; fx avg `0.0094` n `6`; index avg `0.006` n `27`; metal avg `-0.1599` n `20`; unknown avg `41.6573` n `1196`
- 24h: commodity avg `0.0014` n `13`; crypto_alt avg `-8.2166` n `239`; crypto_major avg `-8.1099` n `8`; equity avg `-1.4587` n `162`; fx avg `0.0178` n `6`; index avg `-0.1294` n `27`; metal avg `-0.4866` n `20`; unknown avg `46.4662` n `1070`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1423`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
