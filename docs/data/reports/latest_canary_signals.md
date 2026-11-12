# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T15:07:36.492390+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.5304` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.1647` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.644` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0771` n `13`; crypto_alt avg `-0.4392` n `239`; crypto_major avg `-0.1954` n `8`; equity avg `-0.8771` n `162`; fx avg `0.0028` n `6`; index avg `-0.0662` n `27`; metal avg `-0.1759` n `20`; unknown avg `0.3549` n `1257`
- 1h: commodity avg `0.0425` n `13`; crypto_alt avg `-0.4418` n `239`; crypto_major avg `-0.4473` n `8`; equity avg `0.2486` n `162`; fx avg `-0.0089` n `6`; index avg `0.0475` n `27`; metal avg `-0.2162` n `20`; unknown avg `1.3581` n `1255`
- 4h: commodity avg `0.3233` n `13`; crypto_alt avg `-1.8069` n `239`; crypto_major avg `-2.2071` n `8`; equity avg `-1.6034` n `162`; fx avg `-0.017` n `6`; index avg `-0.0424` n `27`; metal avg `-0.5631` n `20`; unknown avg `19.9871` n `1241`
- 24h: commodity avg `-0.0346` n `13`; crypto_alt avg `-3.6986` n `239`; crypto_major avg `-3.0892` n `8`; equity avg `-2.974` n `162`; fx avg `-0.0653` n `6`; index avg `-0.117` n `27`; metal avg `-1.1378` n `20`; unknown avg `0.8299` n `1146`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.139`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1356`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
