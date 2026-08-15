# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T11:33:02.230011+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0179` n `12`; crypto_alt avg `0.0328` n `230`; crypto_major avg `-0.0117` n `8`; equity avg `-0.0115` n `114`; fx avg `-0.0024` n `6`; index avg `0.0006` n `25`; metal avg `-0.0011` n `20`; unknown avg `0.0619` n `791`
- 1h: commodity avg `0.0708` n `12`; crypto_alt avg `-0.0523` n `230`; crypto_major avg `0.0068` n `8`; equity avg `0.0073` n `114`; fx avg `-0.0018` n `6`; index avg `0.0011` n `25`; metal avg `0.0118` n `20`; unknown avg `0.0651` n `791`
- 4h: commodity avg `0.0787` n `12`; crypto_alt avg `0.0817` n `230`; crypto_major avg `-0.123` n `8`; equity avg `-0.0065` n `114`; fx avg `-0.0075` n `6`; index avg `-0.0135` n `25`; metal avg `0.016` n `20`; unknown avg `-0.0045` n `791`
- 24h: commodity avg `0.0549` n `12`; crypto_alt avg `1.0307` n `230`; crypto_major avg `0.075` n `8`; equity avg `-0.6797` n `114`; fx avg `0.1142` n `6`; index avg `-0.1568` n `25`; metal avg `0.1305` n `20`; unknown avg `-0.037` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2144`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1895`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1825`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.177`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.153`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1483`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.146`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1411`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1411`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1383`, n `668`, weak_sample_signal
