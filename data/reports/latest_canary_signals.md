# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T10:52:26.922135+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.028` n `12`; crypto_alt avg `0.0852` n `228`; crypto_major avg `0.1527` n `8`; equity avg `0.011` n `88`; fx avg `0.0` n `6`; index avg `0.0011` n `23`; metal avg `-0.0013` n `20`; unknown avg `-0.1574` n `764`
- 1h: commodity avg `-0.011` n `12`; crypto_alt avg `-0.1362` n `228`; crypto_major avg `-0.2048` n `8`; equity avg `-0.0601` n `88`; fx avg `0.0028` n `6`; index avg `-0.0083` n `23`; metal avg `-0.0036` n `20`; unknown avg `-0.2563` n `764`
- 4h: commodity avg `-0.043` n `12`; crypto_alt avg `0.3148` n `228`; crypto_major avg `0.3678` n `8`; equity avg `0.2032` n `88`; fx avg `0.0278` n `6`; index avg `0.0591` n `23`; metal avg `-0.0122` n `20`; unknown avg `-0.082` n `742`
- 24h: commodity avg `0.1662` n `12`; crypto_alt avg `-0.3` n `228`; crypto_major avg `-0.8987` n `8`; equity avg `0.0104` n `88`; fx avg `-0.0149` n `6`; index avg `-0.0705` n `23`; metal avg `-0.0138` n `20`; unknown avg `16.0458` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2148`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.189`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
