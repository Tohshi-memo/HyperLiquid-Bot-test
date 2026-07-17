# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T17:22:29.353829+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.7277` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0427` n `12`; crypto_alt avg `-0.0014` n `230`; crypto_major avg `0.0061` n `8`; equity avg `-0.0553` n `96`; fx avg `-0.0227` n `6`; index avg `-0.0422` n `25`; metal avg `-0.0074` n `20`; unknown avg `0.1172` n `769`
- 1h: commodity avg `0.1111` n `12`; crypto_alt avg `0.3948` n `230`; crypto_major avg `0.605` n `8`; equity avg `0.7853` n `96`; fx avg `0.0052` n `6`; index avg `0.0966` n `25`; metal avg `0.0076` n `20`; unknown avg `0.3811` n `769`
- 4h: commodity avg `0.159` n `12`; crypto_alt avg `1.4191` n `230`; crypto_major avg `1.3441` n `8`; equity avg `3.0718` n `96`; fx avg `0.0799` n `6`; index avg `0.4104` n `25`; metal avg `0.4387` n `20`; unknown avg `0.7347` n `769`
- 24h: commodity avg `0.8054` n `12`; crypto_alt avg `-0.9115` n `230`; crypto_major avg `-1.2041` n `8`; equity avg `-0.4564` n `94`; fx avg `0.0857` n `6`; index avg `-0.1372` n `25`; metal avg `-0.0916` n `20`; unknown avg `-0.0707` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
