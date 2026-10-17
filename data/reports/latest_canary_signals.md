# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T14:22:28.332715+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1537` n `13`; crypto_alt avg `0.3493` n `236`; crypto_major avg `0.1468` n `8`; equity avg `0.0381` n `151`; fx avg `-0.0036` n `6`; index avg `0.0057` n `26`; metal avg `-0.0113` n `20`; unknown avg `0.0376` n `1193`
- 1h: commodity avg `0.0393` n `13`; crypto_alt avg `0.5619` n `236`; crypto_major avg `0.2391` n `8`; equity avg `0.0954` n `151`; fx avg `-0.0137` n `6`; index avg `0.0074` n `26`; metal avg `-0.0043` n `20`; unknown avg `0.0578` n `1191`
- 4h: commodity avg `0.0231` n `13`; crypto_alt avg `-0.7164` n `236`; crypto_major avg `-0.3668` n `8`; equity avg `-0.1044` n `151`; fx avg `-0.0134` n `6`; index avg `-0.0346` n `26`; metal avg `-0.0125` n `20`; unknown avg `2.7698` n `1185`
- 24h: commodity avg `0.7654` n `13`; crypto_alt avg `-2.8045` n `236`; crypto_major avg `-1.7846` n `8`; equity avg `-2.2948` n `151`; fx avg `-0.0374` n `6`; index avg `-0.4263` n `26`; metal avg `-0.2771` n `20`; unknown avg `4.2294` n `964`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1739`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1441`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1173`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1127`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0695`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
