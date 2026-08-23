# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T05:58:54.986716+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `2.1759` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_commodity_crypto_divergence: score `-2.1653` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.1644` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.9634` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0219` n `12`; crypto_alt avg `-0.2237` n `230`; crypto_major avg `-0.3093` n `8`; equity avg `-0.0477` n `121`; fx avg `-0.0117` n `6`; index avg `-0.0031` n `25`; metal avg `0.0007` n `20`; unknown avg `-0.0131` n `794`
- 1h: commodity avg `0.01` n `12`; crypto_alt avg `0.022` n `230`; crypto_major avg `-0.2425` n `8`; equity avg `-0.1028` n `121`; fx avg `-0.0216` n `6`; index avg `-0.0105` n `25`; metal avg `0.0089` n `20`; unknown avg `-0.1806` n `794`
- 4h: commodity avg `-0.0161` n `12`; crypto_alt avg `-2.4334` n `230`; crypto_major avg `-2.1814` n `8`; equity avg `-0.218` n `121`; fx avg `-0.0063` n `6`; index avg `-0.0055` n `25`; metal avg `-0.017` n `20`; unknown avg `0.4339` n `794`
- 24h: commodity avg `-0.0469` n `12`; crypto_alt avg `-4.5326` n `230`; crypto_major avg `-2.3745` n `8`; equity avg `-0.0901` n `121`; fx avg `0.063` n `6`; index avg `-0.0092` n `25`; metal avg `0.0302` n `20`; unknown avg `2.1089` n `778`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.159`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1307`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
