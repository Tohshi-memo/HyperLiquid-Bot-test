# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T02:52:35.361697+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.2432` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.9802` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.8775` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.5581` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_metal_divergence: score `-1.5182` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0002` n `13`; crypto_alt avg `-0.2203` n `235`; crypto_major avg `-0.0055` n `8`; equity avg `0.0266` n `150`; fx avg `-0.0077` n `6`; index avg `0.0032` n `26`; metal avg `-0.0129` n `20`; unknown avg `2.6692` n `1076`
- 1h: commodity avg `-0.0168` n `13`; crypto_alt avg `-2.0584` n `235`; crypto_major avg `-1.5829` n `8`; equity avg `-0.277` n `150`; fx avg `-0.0125` n `6`; index avg `-0.0248` n `26`; metal avg `-0.0647` n `20`; unknown avg `1.5579` n `1074`
- 4h: commodity avg `0.2177` n `13`; crypto_alt avg `-2.7523` n `235`; crypto_major avg `-2.0255` n `8`; equity avg `-0.531` n `150`; fx avg `-0.0143` n `6`; index avg `-0.0453` n `26`; metal avg `-0.148` n `20`; unknown avg `1.9584` n `1068`
- 24h: commodity avg `0.4464` n `13`; crypto_alt avg `-2.9032` n `235`; crypto_major avg `-2.4574` n `8`; equity avg `0.0078` n `149`; fx avg `0.0675` n `6`; index avg `0.0061` n `26`; metal avg `-0.0788` n `20`; unknown avg `871.1373` n `914`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1712`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1558`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.152`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
