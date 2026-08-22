# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T08:07:27.239223+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.1547` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.0509` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.9913` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.6738` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0091` n `12`; crypto_alt avg `-0.0887` n `230`; crypto_major avg `-0.359` n `8`; equity avg `-0.0617` n `121`; fx avg `-0.0009` n `6`; index avg `-0.0062` n `25`; metal avg `-0.0027` n `20`; unknown avg `0.2419` n `794`
- 1h: commodity avg `-0.0081` n `12`; crypto_alt avg `-0.7244` n `230`; crypto_major avg `-1.0085` n `8`; equity avg `-0.1247` n `121`; fx avg `-0.0022` n `6`; index avg `-0.024` n `25`; metal avg `0.0133` n `20`; unknown avg `0.2395` n `794`
- 4h: commodity avg `0.063` n `12`; crypto_alt avg `-3.7284` n `230`; crypto_major avg `-2.0917` n `8`; equity avg `-0.4179` n `121`; fx avg `-0.0038` n `6`; index avg `-0.0408` n `25`; metal avg `-0.1004` n `20`; unknown avg `0.1216` n `778`
- 24h: commodity avg `0.0304` n `12`; crypto_alt avg `4.8291` n `230`; crypto_major avg `5.6062` n `8`; equity avg `-0.5947` n `121`; fx avg `0.0516` n `6`; index avg `-0.113` n `25`; metal avg `-0.0549` n `20`; unknown avg `1.9899` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.154`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1475`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.14`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1393`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
