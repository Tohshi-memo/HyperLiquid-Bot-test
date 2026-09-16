# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T02:52:25.828719+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0074` n `12`; crypto_alt avg `-0.0765` n `234`; crypto_major avg `-0.1276` n `8`; equity avg `0.0509` n `137`; fx avg `0.005` n `6`; index avg `0.0039` n `27`; metal avg `0.0099` n `20`; unknown avg `0.0229` n `915`
- 1h: commodity avg `-0.1062` n `12`; crypto_alt avg `0.6431` n `234`; crypto_major avg `0.6702` n `8`; equity avg `0.4179` n `137`; fx avg `-0.053` n `6`; index avg `0.0562` n `27`; metal avg `0.2209` n `20`; unknown avg `6.4887` n `913`
- 4h: commodity avg `-0.1166` n `12`; crypto_alt avg `-0.2631` n `234`; crypto_major avg `0.2095` n `8`; equity avg `0.2568` n `137`; fx avg `0.0753` n `6`; index avg `0.0309` n `27`; metal avg `0.1618` n `20`; unknown avg `4.4006` n `907`
- 24h: commodity avg `0.2237` n `12`; crypto_alt avg `-3.8621` n `234`; crypto_major avg `-3.6701` n `8`; equity avg `-1.3265` n `137`; fx avg `0.1977` n `6`; index avg `-0.1286` n `27`; metal avg `0.2371` n `20`; unknown avg `0.7559` n `798`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
