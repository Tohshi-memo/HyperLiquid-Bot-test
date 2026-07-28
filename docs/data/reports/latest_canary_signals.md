# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T00:07:31.361157+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.7857` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.7714` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0685` n `12`; crypto_alt avg `0.0946` n `230`; crypto_major avg `0.0046` n `8`; equity avg `-0.075` n `102`; fx avg `0.062` n `6`; index avg `-0.0447` n `25`; metal avg `-0.0697` n `20`; unknown avg `-0.145` n `774`
- 1h: commodity avg `-0.0561` n `12`; crypto_alt avg `-0.0811` n `230`; crypto_major avg `-0.0928` n `8`; equity avg `-0.0839` n `102`; fx avg `0.0636` n `6`; index avg `-0.0836` n `25`; metal avg `-0.074` n `20`; unknown avg `-0.1238` n `774`
- 4h: commodity avg `-0.0058` n `12`; crypto_alt avg `-1.964` n `230`; crypto_major avg `-1.9137` n `8`; equity avg `-0.6352` n `102`; fx avg `0.0589` n `6`; index avg `-0.128` n `25`; metal avg `-0.1423` n `20`; unknown avg `1.127` n `774`
- 24h: commodity avg `-0.7278` n `12`; crypto_alt avg `-3.6456` n `230`; crypto_major avg `-3.0312` n `8`; equity avg `-1.8933` n `102`; fx avg `0.0163` n `6`; index avg `-0.5003` n `25`; metal avg `-0.1722` n `20`; unknown avg `1161.7654` n `757`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.3543`, n `668`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.3035`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1944`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1363`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
