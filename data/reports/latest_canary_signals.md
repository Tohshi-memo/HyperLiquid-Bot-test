# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T00:37:25.805620+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0269` n `12`; crypto_alt avg `-0.1029` n `234`; crypto_major avg `-0.1005` n `8`; equity avg `-0.0293` n `141`; fx avg `-0.011` n `6`; index avg `-0.0148` n `26`; metal avg `-0.0245` n `20`; unknown avg `-0.051` n `946`
- 1h: commodity avg `-0.0902` n `12`; crypto_alt avg `0.0854` n `234`; crypto_major avg `0.0681` n `8`; equity avg `0.0834` n `141`; fx avg `-0.0318` n `6`; index avg `-0.0098` n `26`; metal avg `-0.0696` n `20`; unknown avg `0.0598` n `938`
- 4h: commodity avg `-0.412` n `12`; crypto_alt avg `0.4408` n `234`; crypto_major avg `0.0748` n `8`; equity avg `0.2143` n `141`; fx avg `-0.017` n `6`; index avg `0.02` n `26`; metal avg `-0.0266` n `20`; unknown avg `4.381` n `896`
- 24h: commodity avg `0.5856` n `12`; crypto_alt avg `3.8813` n `234`; crypto_major avg `0.945` n `8`; equity avg `-0.1621` n `141`; fx avg `0.0214` n `6`; index avg `-0.0918` n `26`; metal avg `-0.1297` n `20`; unknown avg `23.293` n `815`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1527`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1477`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1454`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.127`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
