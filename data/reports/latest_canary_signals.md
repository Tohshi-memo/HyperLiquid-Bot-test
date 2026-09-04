# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T15:22:30.349772+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-2.8721` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- polymarket_volume_spike: score `2.71` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `-2.6766` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.5755` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.4954` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0239` n `12`; crypto_alt avg `0.1358` n `232`; crypto_major avg `0.2246` n `8`; equity avg `0.0511` n `133`; fx avg `0.0127` n `6`; index avg `0.0143` n `26`; metal avg `0.0259` n `20`; unknown avg `0.1589` n `785`
- 1h: commodity avg `0.1968` n `12`; crypto_alt avg `-0.1715` n `232`; crypto_major avg `-0.1008` n `8`; equity avg `0.0057` n `133`; fx avg `0.0283` n `6`; index avg `-0.0049` n `26`; metal avg `0.0767` n `20`; unknown avg `0.3311` n `783`
- 4h: commodity avg `0.1089` n `12`; crypto_alt avg `-2.0859` n `232`; crypto_major avg `-2.5677` n `8`; equity avg `0.3044` n `133`; fx avg `-0.0928` n `6`; index avg `0.0078` n `26`; metal avg `-0.0723` n `20`; unknown avg `1.2908` n `729`
- 24h: commodity avg `-0.0923` n `12`; crypto_alt avg `-1.0426` n `232`; crypto_major avg `-1.6056` n `8`; equity avg `1.5625` n `133`; fx avg `-0.0997` n `6`; index avg `0.1957` n `26`; metal avg `-0.3109` n `20`; unknown avg `28.8264` n `690`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
