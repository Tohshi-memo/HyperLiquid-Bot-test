# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T15:37:26.795731+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.72` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `-2.6744` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `-2.6103` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.4423` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.3681` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0422` n `12`; crypto_alt avg `0.1864` n `232`; crypto_major avg `0.1225` n `8`; equity avg `-0.0463` n `133`; fx avg `-0.0027` n `6`; index avg `-0.0176` n `26`; metal avg `-0.0131` n `20`; unknown avg `0.045` n `789`
- 1h: commodity avg `0.1149` n `12`; crypto_alt avg `0.2429` n `232`; crypto_major avg `0.1793` n `8`; equity avg `-0.1028` n `133`; fx avg `0.0354` n `6`; index avg `-0.021` n `26`; metal avg `0.0374` n `20`; unknown avg `0.7417` n `779`
- 4h: commodity avg `0.1556` n `12`; crypto_alt avg `-1.9922` n `232`; crypto_major avg `-2.4547` n `8`; equity avg `0.2197` n `133`; fx avg `-0.0879` n `6`; index avg `-0.0124` n `26`; metal avg `-0.0866` n `20`; unknown avg `1.0379` n `725`
- 24h: commodity avg `0.0624` n `12`; crypto_alt avg `-1.1996` n `232`; crypto_major avg `-1.5694` n `8`; equity avg `1.3213` n `133`; fx avg `-0.0672` n `6`; index avg `0.1518` n `26`; metal avg `-0.3347` n `20`; unknown avg `28.7155` n `686`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
