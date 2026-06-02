# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T07:52:23.151813+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.68` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `-2.6257` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-2.151` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `2.0482` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1559` n `12`; crypto_alt avg `-0.0153` n `228`; crypto_major avg `-0.1351` n `8`; equity avg `0.0543` n `69`; fx avg `-0.0024` n `6`; index avg `0.017` n `23`; metal avg `0.0424` n `18`; unknown avg `0.0425` n `422`
- 1h: commodity avg `-0.1366` n `12`; crypto_alt avg `0.2714` n `228`; crypto_major avg `0.1577` n `8`; equity avg `0.0616` n `69`; fx avg `-0.0141` n `6`; index avg `0.1412` n `23`; metal avg `0.1213` n `18`; unknown avg `-0.2978` n `422`
- 4h: commodity avg `-0.091` n `12`; crypto_alt avg `-1.1731` n `228`; crypto_major avg `-1.446` n `8`; equity avg `0.705` n `69`; fx avg `0.0645` n `6`; index avg `0.6022` n `23`; metal avg `1.1797` n `18`; unknown avg `0.368` n `412`
- 24h: commodity avg `-1.2097` n `12`; crypto_alt avg `0.2304` n `228`; crypto_major avg `-1.0516` n `8`; equity avg `0.3921` n `69`; fx avg `0.1373` n `6`; index avg `-0.6104` n `23`; metal avg `1.4165` n `18`; unknown avg `2.266` n `406`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1933`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
