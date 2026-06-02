# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T09:37:26.426681+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.67` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.3001` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1968` n `12`; crypto_alt avg `0.0906` n `228`; crypto_major avg `0.0265` n `8`; equity avg `0.0532` n `69`; fx avg `0.0009` n `6`; index avg `-0.0226` n `23`; metal avg `-0.088` n `18`; unknown avg `0.6582` n `422`
- 1h: commodity avg `0.0349` n `12`; crypto_alt avg `-0.5344` n `228`; crypto_major avg `-0.5432` n `8`; equity avg `-0.1043` n `69`; fx avg `-0.0212` n `6`; index avg `-0.0967` n `23`; metal avg `-0.2703` n `18`; unknown avg `0.2589` n `422`
- 4h: commodity avg `0.0511` n `12`; crypto_alt avg `-0.8346` n `228`; crypto_major avg `-1.05` n `8`; equity avg `0.1338` n `69`; fx avg `0.0444` n `6`; index avg `0.2501` n `23`; metal avg `-0.1283` n `18`; unknown avg `-0.8499` n `412`
- 24h: commodity avg `-1.1222` n `12`; crypto_alt avg `-0.3801` n `228`; crypto_major avg `-2.2329` n `8`; equity avg `0.5516` n `69`; fx avg `0.1245` n `6`; index avg `0.029` n `23`; metal avg `0.8747` n `18`; unknown avg `1.4055` n `406`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1844`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1452`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
