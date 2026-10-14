# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T22:37:30.390768+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0137` n `13`; crypto_alt avg `-0.0044` n `236`; crypto_major avg `-0.0226` n `8`; equity avg `-0.1631` n `151`; fx avg `0.0266` n `6`; index avg `-0.0022` n `26`; metal avg `-0.0043` n `20`; unknown avg `0.1789` n `1136`
- 1h: commodity avg `-0.0109` n `13`; crypto_alt avg `-0.2107` n `236`; crypto_major avg `-0.3447` n `8`; equity avg `-0.7458` n `151`; fx avg `0.0099` n `6`; index avg `-0.0874` n `26`; metal avg `0.0227` n `20`; unknown avg `-0.2247` n `1054`
- 4h: commodity avg `0.0564` n `13`; crypto_alt avg `0.4793` n `236`; crypto_major avg `0.1636` n `8`; equity avg `-1.1774` n `151`; fx avg `0.0264` n `6`; index avg `-0.1275` n `26`; metal avg `0.0133` n `20`; unknown avg `0.9766` n `998`
- 24h: commodity avg `-0.1109` n `13`; crypto_alt avg `-2.2469` n `236`; crypto_major avg `-2.1632` n `8`; equity avg `-5.3325` n `151`; fx avg `-0.1329` n `6`; index avg `-0.677` n `26`; metal avg `-0.8154` n `20`; unknown avg `1393.0724` n `890`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0875`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0856`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0816`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0797`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0598`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0576`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0531`, n `666`, weak_sample_signal
