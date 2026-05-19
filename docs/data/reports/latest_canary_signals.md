# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T04:21:54.987182+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0414` n `12`; crypto_alt avg `0.0249` n `228`; crypto_major avg `-0.062` n `8`; equity avg `0.0142` n `66`; fx avg `0.005` n `6`; index avg `-0.018` n `23`; metal avg `0.0644` n `18`; unknown avg `0.4836` n `383`
- 1h: commodity avg `-0.0749` n `12`; crypto_alt avg `0.2957` n `228`; crypto_major avg `0.167` n `8`; equity avg `-0.0548` n `66`; fx avg `0.0149` n `6`; index avg `-0.1493` n `23`; metal avg `-0.2149` n `18`; unknown avg `0.3552` n `383`
- 4h: commodity avg `0.123` n `12`; crypto_alt avg `-0.416` n `228`; crypto_major avg `-0.7005` n `8`; equity avg `-0.7411` n `66`; fx avg `0.0974` n `6`; index avg `-0.5637` n `23`; metal avg `-1.4865` n `18`; unknown avg `0.1946` n `383`
- 24h: commodity avg `0.1104` n `12`; crypto_alt avg `1.0622` n `228`; crypto_major avg `0.4265` n `8`; equity avg `-0.9754` n `66`; fx avg `0.2535` n `6`; index avg `-0.5594` n `23`; metal avg `0.2381` n `18`; unknown avg `1.1336` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1948`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1683`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1519`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1517`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
