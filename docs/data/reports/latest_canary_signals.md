# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T19:52:28.417143+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0118` n `13`; crypto_alt avg `-0.2113` n `237`; crypto_major avg `-0.093` n `8`; equity avg `-0.0416` n `151`; fx avg `-0.0211` n `6`; index avg `-0.0167` n `26`; metal avg `-0.0063` n `20`; unknown avg `0.9722` n `1194`
- 1h: commodity avg `0.0167` n `13`; crypto_alt avg `-1.5053` n `237`; crypto_major avg `-0.9155` n `8`; equity avg `-0.2321` n `151`; fx avg `-0.0235` n `6`; index avg `-0.0229` n `26`; metal avg `-0.0314` n `20`; unknown avg `6.2849` n `1184`
- 4h: commodity avg `0.018` n `13`; crypto_alt avg `-1.8071` n `237`; crypto_major avg `-0.8787` n `8`; equity avg `-0.3059` n `151`; fx avg `-0.0168` n `6`; index avg `-0.041` n `26`; metal avg `-0.0162` n `20`; unknown avg `0.2365` n `1144`
- 24h: commodity avg `0.038` n `13`; crypto_alt avg `-5.285` n `236`; crypto_major avg `-2.4393` n `8`; equity avg `-1.3094` n `151`; fx avg `-0.0206` n `6`; index avg `-0.1729` n `26`; metal avg `-0.0806` n `20`; unknown avg `1.0796` n `1007`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2102`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1399`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1376`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1147`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0808`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
