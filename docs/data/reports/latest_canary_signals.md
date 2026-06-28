# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T14:37:25.374552+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.006` n `12`; crypto_alt avg `0.1307` n `228`; crypto_major avg `-0.0622` n `8`; equity avg `0.0079` n `88`; fx avg `-0.0008` n `6`; index avg `0.0145` n `23`; metal avg `-0.0063` n `20`; unknown avg `2.4972` n `764`
- 1h: commodity avg `0.0022` n `12`; crypto_alt avg `0.6184` n `228`; crypto_major avg `0.0961` n `8`; equity avg `0.039` n `88`; fx avg `-0.0107` n `6`; index avg `0.0104` n `23`; metal avg `0.0029` n `20`; unknown avg `2.6601` n `764`
- 4h: commodity avg `0.1165` n `12`; crypto_alt avg `0.8481` n `228`; crypto_major avg `0.5184` n `8`; equity avg `0.1055` n `88`; fx avg `-0.0086` n `6`; index avg `0.031` n `23`; metal avg `-0.0148` n `20`; unknown avg `1.6076` n `764`
- 24h: commodity avg `0.1558` n `12`; crypto_alt avg `0.0506` n `228`; crypto_major avg `-1.0858` n `8`; equity avg `0.0266` n `88`; fx avg `-0.0122` n `6`; index avg `-0.0403` n `23`; metal avg `-0.0522` n `20`; unknown avg `16.3933` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1986`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1853`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
