# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T07:52:27.357060+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.1475` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.9981` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.9668` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.6736` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.012` n `12`; crypto_alt avg `-0.1766` n `230`; crypto_major avg `-0.355` n `8`; equity avg `-0.0162` n `121`; fx avg `-0.0014` n `6`; index avg `-0.0056` n `25`; metal avg `-0.0034` n `20`; unknown avg `-0.0273` n `794`
- 1h: commodity avg `-0.0006` n `12`; crypto_alt avg `-0.1252` n `230`; crypto_major avg `0.0566` n `8`; equity avg `-0.062` n `121`; fx avg `-0.0187` n `6`; index avg `-0.0101` n `25`; metal avg `0.0222` n `20`; unknown avg `0.5961` n `794`
- 4h: commodity avg `0.0879` n `12`; crypto_alt avg `-3.7966` n `230`; crypto_major avg `-2.0596` n `8`; equity avg `-0.386` n `121`; fx avg `-0.0139` n `6`; index avg `-0.0615` n `25`; metal avg `-0.0928` n `20`; unknown avg `0.4663` n `778`
- 24h: commodity avg `0.1217` n `12`; crypto_alt avg `5.1276` n `230`; crypto_major avg `6.5053` n `8`; equity avg `-0.5833` n `121`; fx avg `0.0405` n `6`; index avg `-0.1184` n `25`; metal avg `-0.0756` n `20`; unknown avg `1.7172` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1536`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1452`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1401`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1399`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1374`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
