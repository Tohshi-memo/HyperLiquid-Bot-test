# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T15:37:48.845405+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.17` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.0452` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0365` n `12`; crypto_alt avg `0.1397` n `228`; crypto_major avg `0.1319` n `8`; equity avg `0.0752` n `88`; fx avg `-0.0027` n `6`; index avg `0.0178` n `23`; metal avg `0.0471` n `20`; unknown avg `-0.0285` n `765`
- 1h: commodity avg `-0.0951` n `12`; crypto_alt avg `-0.3182` n `228`; crypto_major avg `-0.4302` n `8`; equity avg `-0.2774` n `88`; fx avg `0.0537` n `6`; index avg `0.0049` n `23`; metal avg `-0.2987` n `20`; unknown avg `-0.4462` n `765`
- 4h: commodity avg `0.0541` n `12`; crypto_alt avg `-0.2194` n `228`; crypto_major avg `-0.8715` n `8`; equity avg `0.1917` n `88`; fx avg `0.0978` n `6`; index avg `0.1737` n `23`; metal avg `-0.1146` n `20`; unknown avg `-0.3666` n `765`
- 24h: commodity avg `0.2734` n `12`; crypto_alt avg `-1.6555` n `228`; crypto_major avg `-1.3007` n `8`; equity avg `1.9424` n `88`; fx avg `0.1458` n `6`; index avg `0.4141` n `23`; metal avg `0.3148` n `20`; unknown avg `8.4191` n `735`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0637`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
