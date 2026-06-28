# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T07:22:32.432061+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0012` n `12`; crypto_alt avg `-0.031` n `228`; crypto_major avg `0.0339` n `8`; equity avg `0.0271` n `88`; fx avg `0.0015` n `6`; index avg `0.004` n `23`; metal avg `-0.0052` n `20`; unknown avg `-1.021` n `764`
- 1h: commodity avg `0.1381` n `12`; crypto_alt avg `0.3902` n `228`; crypto_major avg `0.3862` n `8`; equity avg `0.0683` n `88`; fx avg `0.003` n `6`; index avg `0.0148` n `23`; metal avg `-0.0117` n `20`; unknown avg `-1.166` n `764`
- 4h: commodity avg `0.1418` n `12`; crypto_alt avg `-0.032` n `228`; crypto_major avg `-0.2127` n `8`; equity avg `0.0174` n `88`; fx avg `0.0068` n `6`; index avg `-0.0037` n `23`; metal avg `-0.0268` n `20`; unknown avg `-1.3387` n `732`
- 24h: commodity avg `0.3484` n `12`; crypto_alt avg `-0.6526` n `228`; crypto_major avg `-1.3375` n `8`; equity avg `-0.0607` n `88`; fx avg `-0.0278` n `6`; index avg `-0.1298` n `23`; metal avg `-0.0547` n `20`; unknown avg `14.9136` n `682`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2187`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.189`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
