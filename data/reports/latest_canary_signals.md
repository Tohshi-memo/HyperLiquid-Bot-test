# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T17:37:30.991150+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0181` n `12`; crypto_alt avg `-0.0953` n `234`; crypto_major avg `-0.0827` n `8`; equity avg `-0.0818` n `141`; fx avg `0.0111` n `6`; index avg `-0.0207` n `26`; metal avg `-0.0091` n `20`; unknown avg `0.3771` n `943`
- 1h: commodity avg `0.4122` n `12`; crypto_alt avg `-0.361` n `234`; crypto_major avg `-0.3614` n `8`; equity avg `-0.0646` n `141`; fx avg `0.016` n `6`; index avg `-0.0453` n `26`; metal avg `-0.1162` n `20`; unknown avg `5.139` n `941`
- 4h: commodity avg `0.718` n `12`; crypto_alt avg `1.913` n `234`; crypto_major avg `0.9132` n `8`; equity avg `0.5281` n `141`; fx avg `0.0222` n `6`; index avg `0.0451` n `26`; metal avg `0.0114` n `20`; unknown avg `8.8043` n `883`
- 24h: commodity avg `1.1299` n `12`; crypto_alt avg `3.0459` n `234`; crypto_major avg `1.3915` n `8`; equity avg `-0.3332` n `141`; fx avg `0.0128` n `6`; index avg `-0.0691` n `26`; metal avg `-0.0515` n `20`; unknown avg `264.0223` n `833`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1632`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1569`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1477`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1399`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
