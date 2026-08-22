# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T11:07:26.749240+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-2.6095` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `-2.5632` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.5619` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-2.2887` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0011` n `12`; crypto_alt avg `0.1563` n `230`; crypto_major avg `0.1177` n `8`; equity avg `-0.0385` n `121`; fx avg `0.0016` n `6`; index avg `0.0066` n `25`; metal avg `-0.007` n `20`; unknown avg `0.1119` n `794`
- 1h: commodity avg `-0.0143` n `12`; crypto_alt avg `0.1637` n `230`; crypto_major avg `0.1595` n `8`; equity avg `-0.068` n `121`; fx avg `0.0157` n `6`; index avg `-0.0069` n `25`; metal avg `-0.0209` n `20`; unknown avg `0.0391` n `794`
- 4h: commodity avg `-0.0352` n `12`; crypto_alt avg `-2.355` n `230`; crypto_major avg `-2.5984` n `8`; equity avg `-0.3097` n `121`; fx avg `0.0301` n `6`; index avg `-0.0365` n `25`; metal avg `0.0111` n `20`; unknown avg `0.092` n `794`
- 24h: commodity avg `-0.0911` n `12`; crypto_alt avg `1.4527` n `230`; crypto_major avg `2.383` n `8`; equity avg `-0.9338` n `121`; fx avg `0.0512` n `6`; index avg `-0.1065` n `25`; metal avg `-0.1626` n `20`; unknown avg `1.4467` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1636`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1358`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
