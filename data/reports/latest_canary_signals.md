# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T04:37:32.885867+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.6842` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `2.5921` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `2.1482` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0015` n `13`; crypto_alt avg `-0.0466` n `239`; crypto_major avg `-0.0239` n `8`; equity avg `-0.0354` n `162`; fx avg `-0.0008` n `6`; index avg `0.0` n `27`; metal avg `-0.0897` n `20`; unknown avg `0.7413` n `1259`
- 1h: commodity avg `0.0383` n `13`; crypto_alt avg `-0.2831` n `239`; crypto_major avg `-0.3169` n `8`; equity avg `-0.0733` n `162`; fx avg `0.0099` n `6`; index avg `-0.0042` n `27`; metal avg `-0.0905` n `20`; unknown avg `0.348` n `1245`
- 4h: commodity avg `0.0686` n `13`; crypto_alt avg `1.9951` n `239`; crypto_major avg `2.6607` n `8`; equity avg `0.5125` n `162`; fx avg `0.0132` n `6`; index avg `0.0145` n `27`; metal avg `-0.0235` n `20`; unknown avg `2.2695` n `1242`
- 24h: commodity avg `0.0839` n `13`; crypto_alt avg `-5.2846` n `239`; crypto_major avg `-3.6622` n `8`; equity avg `-0.7084` n `162`; fx avg `0.0416` n `6`; index avg `-0.0634` n `27`; metal avg `-0.4643` n `20`; unknown avg `47.2284` n `1062`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1372`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
