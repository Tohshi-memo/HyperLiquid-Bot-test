# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T09:37:32.360191+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0871` n `13`; crypto_alt avg `0.1607` n `239`; crypto_major avg `0.2523` n `8`; equity avg `0.4322` n `162`; fx avg `-0.002` n `6`; index avg `0.038` n `27`; metal avg `0.0127` n `20`; unknown avg `1.093` n `1261`
- 1h: commodity avg `-0.1712` n `13`; crypto_alt avg `0.0194` n `239`; crypto_major avg `0.1026` n `8`; equity avg `0.5879` n `162`; fx avg `-0.018` n `6`; index avg `0.0651` n `27`; metal avg `-0.1558` n `20`; unknown avg `1.1242` n `1255`
- 4h: commodity avg `0.2255` n `13`; crypto_alt avg `-0.2634` n `239`; crypto_major avg `-0.0554` n `8`; equity avg `0.7732` n `162`; fx avg `0.0752` n `6`; index avg `0.0459` n `27`; metal avg `-0.2318` n `20`; unknown avg `61.2625` n `1207`
- 24h: commodity avg `0.1226` n `13`; crypto_alt avg `-1.1878` n `239`; crypto_major avg `-0.4333` n `8`; equity avg `-0.2192` n `162`; fx avg `-0.0257` n `6`; index avg `-0.0111` n `27`; metal avg `-0.8329` n `20`; unknown avg `17.5931` n `1140`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1379`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1334`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1306`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
