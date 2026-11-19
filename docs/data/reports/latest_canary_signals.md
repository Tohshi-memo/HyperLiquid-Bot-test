# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T09:22:29.218418+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0245` n `13`; crypto_alt avg `-0.0212` n `239`; crypto_major avg `-0.0888` n `8`; equity avg `-0.084` n `164`; fx avg `0.0025` n `6`; index avg `-0.0139` n `27`; metal avg `-0.0689` n `20`; unknown avg `0.3062` n `1264`
- 1h: commodity avg `0.0317` n `13`; crypto_alt avg `0.2498` n `239`; crypto_major avg `0.1202` n `8`; equity avg `0.0755` n `164`; fx avg `0.0301` n `6`; index avg `0.0076` n `27`; metal avg `-0.0122` n `20`; unknown avg `261.8651` n `1260`
- 4h: commodity avg `-0.0263` n `13`; crypto_alt avg `0.6831` n `239`; crypto_major avg `0.6449` n `8`; equity avg `1.2545` n `164`; fx avg `0.0933` n `6`; index avg `0.1905` n `27`; metal avg `0.0082` n `20`; unknown avg `359.6316` n `1202`
- 24h: commodity avg `0.2638` n `13`; crypto_alt avg `0.2148` n `239`; crypto_major avg `-0.4806` n `8`; equity avg `0.1074` n `164`; fx avg `0.0858` n `6`; index avg `0.1421` n `27`; metal avg `-0.1338` n `20`; unknown avg `3.4701` n `1161`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1623`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.161`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0582`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.057`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0536`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0524`, n `668`, weak_sample_signal
