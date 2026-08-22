# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T00:07:23.021648+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.3467` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `2.2642` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `2.2442` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_index_leads_crypto: score `1.3968` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0101` n `12`; crypto_alt avg `-0.2379` n `230`; crypto_major avg `-0.8423` n `8`; equity avg `-0.0368` n `121`; fx avg `0.0` n `6`; index avg `0.0039` n `25`; metal avg `-0.0009` n `20`; unknown avg `0.639` n `793`
- 1h: commodity avg `-0.0368` n `12`; crypto_alt avg `-0.437` n `230`; crypto_major avg `-1.3913` n `8`; equity avg `-0.0345` n `121`; fx avg `-0.0001` n `6`; index avg `0.0055` n `25`; metal avg `-0.0008` n `20`; unknown avg `0.8439` n `793`
- 4h: commodity avg `0.0328` n `12`; crypto_alt avg `2.0806` n `230`; crypto_major avg `2.297` n `8`; equity avg `0.0528` n `121`; fx avg `-0.0054` n `6`; index avg `0.0258` n `25`; metal avg `-0.0497` n `20`; unknown avg `0.0918` n `793`
- 24h: commodity avg `0.1349` n `12`; crypto_alt avg `7.8341` n `230`; crypto_major avg `6.3012` n `8`; equity avg `0.8924` n `121`; fx avg `-0.0494` n `6`; index avg `0.1142` n `25`; metal avg `0.4847` n `20`; unknown avg `1.3157` n `777`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.22`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1798`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1768`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1709`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
