# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T18:52:27.366675+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0033` n `12`; crypto_alt avg `-0.1094` n `230`; crypto_major avg `-0.0771` n `8`; equity avg `-0.0055` n `92`; fx avg `0.0` n `6`; index avg `-0.0105` n `25`; metal avg `0.0068` n `20`; unknown avg `0.0523` n `765`
- 1h: commodity avg `0.0033` n `12`; crypto_alt avg `0.093` n `230`; crypto_major avg `0.0512` n `8`; equity avg `0.0351` n `92`; fx avg `-0.0023` n `6`; index avg `-0.0112` n `25`; metal avg `0.0057` n `20`; unknown avg `-0.0168` n `765`
- 4h: commodity avg `0.0439` n `12`; crypto_alt avg `0.0953` n `230`; crypto_major avg `0.0403` n `8`; equity avg `0.1666` n `92`; fx avg `-0.001` n `6`; index avg `0.0009` n `25`; metal avg `-0.027` n `20`; unknown avg `0.2337` n `765`
- 24h: commodity avg `0.0216` n `12`; crypto_alt avg `1.3547` n `229`; crypto_major avg `1.0846` n `8`; equity avg `0.2789` n `92`; fx avg `0.0035` n `6`; index avg `0.0226` n `25`; metal avg `0.104` n `20`; unknown avg `2.4211` n `727`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
