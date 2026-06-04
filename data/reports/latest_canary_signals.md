# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T05:07:24.635332+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.3682` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0057` n `12`; crypto_alt avg `-0.9904` n `228`; crypto_major avg `-0.8018` n `8`; equity avg `-0.0886` n `73`; fx avg `0.0013` n `6`; index avg `-0.0522` n `23`; metal avg `-0.0906` n `18`; unknown avg `2.2944` n `420`
- 1h: commodity avg `0.0313` n `12`; crypto_alt avg `-1.9884` n `228`; crypto_major avg `-1.3188` n `8`; equity avg `-0.0978` n `73`; fx avg `-0.0008` n `6`; index avg `0.0494` n `23`; metal avg `0.162` n `18`; unknown avg `-0.5697` n `420`
- 4h: commodity avg `-0.149` n `12`; crypto_alt avg `-3.1251` n `228`; crypto_major avg `-0.6656` n `8`; equity avg `0.0345` n `73`; fx avg `0.017` n `6`; index avg `-0.006` n `23`; metal avg `0.2009` n `18`; unknown avg `0.6095` n `420`
- 24h: commodity avg `0.0317` n `12`; crypto_alt avg `-4.2384` n `228`; crypto_major avg `-3.4143` n `8`; equity avg `-3.6009` n `73`; fx avg `0.01` n `6`; index avg `-1.061` n `23`; metal avg `-1.2696` n `18`; unknown avg `1.0218` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1907`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1727`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1544`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1541`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
