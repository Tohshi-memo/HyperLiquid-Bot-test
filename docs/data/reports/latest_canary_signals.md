# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T20:52:30.843559+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.11` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0049` n `12`; crypto_alt avg `-0.0414` n `228`; crypto_major avg `-0.0019` n `8`; equity avg `0.0268` n `88`; fx avg `-0.0035` n `6`; index avg `-0.0047` n `23`; metal avg `-0.0333` n `20`; unknown avg `-0.005` n `765`
- 1h: commodity avg `-0.0229` n `12`; crypto_alt avg `-0.3111` n `228`; crypto_major avg `-0.227` n `8`; equity avg `0.052` n `88`; fx avg `0.0037` n `6`; index avg `-0.0418` n `23`; metal avg `-0.1637` n `20`; unknown avg `0.3616` n `765`
- 4h: commodity avg `-0.1619` n `12`; crypto_alt avg `-0.2458` n `228`; crypto_major avg `0.3391` n `8`; equity avg `0.3251` n `88`; fx avg `-0.0063` n `6`; index avg `-0.0572` n `23`; metal avg `-0.2772` n `20`; unknown avg `1.2632` n `763`
- 24h: commodity avg `0.1223` n `12`; crypto_alt avg `-2.3252` n `228`; crypto_major avg `-2.2073` n `8`; equity avg `1.1997` n `88`; fx avg `0.1339` n `6`; index avg `0.2184` n `23`; metal avg `-0.0305` n `20`; unknown avg `8.0841` n `733`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0539`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.053`, n `668`, weak_sample_signal
