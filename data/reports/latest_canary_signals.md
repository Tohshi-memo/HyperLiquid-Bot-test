# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T14:52:30.268931+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0456` n `12`; crypto_alt avg `-0.0676` n `228`; crypto_major avg `-0.1042` n `8`; equity avg `0.005` n `88`; fx avg `0.0166` n `6`; index avg `-0.0011` n `23`; metal avg `-0.0212` n `20`; unknown avg `0.023` n `764`
- 1h: commodity avg `0.0545` n `12`; crypto_alt avg `0.6032` n `228`; crypto_major avg `0.0448` n `8`; equity avg `0.0057` n `88`; fx avg `0.0074` n `6`; index avg `0.0079` n `23`; metal avg `-0.0244` n `20`; unknown avg `2.7092` n `764`
- 4h: commodity avg `0.1342` n `12`; crypto_alt avg `0.7095` n `228`; crypto_major avg `0.2601` n `8`; equity avg `0.0997` n `88`; fx avg `0.008` n `6`; index avg `0.0288` n `23`; metal avg `-0.0346` n `20`; unknown avg `1.8559` n `764`
- 24h: commodity avg `0.228` n `12`; crypto_alt avg `-0.1128` n `228`; crypto_major avg `-1.2595` n `8`; equity avg `0.0426` n `88`; fx avg `0.0057` n `6`; index avg `-0.0415` n `23`; metal avg `-0.0724` n `20`; unknown avg `16.3907` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1974`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1853`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
