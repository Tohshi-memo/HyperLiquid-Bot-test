# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T02:07:31.899846+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0417` n `13`; crypto_alt avg `0.105` n `239`; crypto_major avg `0.0656` n `8`; equity avg `0.0678` n `164`; fx avg `-0.0052` n `6`; index avg `0.0166` n `27`; metal avg `-0.0861` n `20`; unknown avg `9.0928` n `1259`
- 1h: commodity avg `0.1278` n `13`; crypto_alt avg `-0.3824` n `239`; crypto_major avg `-0.6047` n `8`; equity avg `-0.7724` n `164`; fx avg `-0.0066` n `6`; index avg `-0.0925` n `27`; metal avg `-0.1638` n `20`; unknown avg `2.131` n `1263`
- 4h: commodity avg `0.1713` n `13`; crypto_alt avg `0.5908` n `239`; crypto_major avg `0.4242` n `8`; equity avg `0.7636` n `164`; fx avg `-0.0207` n `6`; index avg `0.0862` n `27`; metal avg `0.1385` n `20`; unknown avg `6.0128` n `1257`
- 24h: commodity avg `0.1338` n `13`; crypto_alt avg `-0.2847` n `239`; crypto_major avg `-1.375` n `8`; equity avg `-0.393` n `164`; fx avg `-0.1081` n `6`; index avg `0.0757` n `27`; metal avg `-0.5544` n `20`; unknown avg `121.2518` n `1129`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0643`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0557`, n `668`, weak_sample_signal
