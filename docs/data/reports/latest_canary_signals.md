# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T04:07:26.301477+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.036` n `12`; crypto_alt avg `0.105` n `230`; crypto_major avg `0.0152` n `8`; equity avg `0.0092` n `114`; fx avg `0.004` n `6`; index avg `0.0053` n `25`; metal avg `0.0176` n `20`; unknown avg `0.0189` n `792`
- 1h: commodity avg `-0.0399` n `12`; crypto_alt avg `0.1021` n `230`; crypto_major avg `0.0776` n `8`; equity avg `0.0961` n `114`; fx avg `0.0231` n `6`; index avg `0.0221` n `25`; metal avg `-0.0208` n `20`; unknown avg `0.1831` n `792`
- 4h: commodity avg `-0.0115` n `12`; crypto_alt avg `0.8381` n `230`; crypto_major avg `1.1624` n `8`; equity avg `0.5802` n `114`; fx avg `-0.0104` n `6`; index avg `0.0355` n `25`; metal avg `0.1731` n `20`; unknown avg `1.1747` n `792`
- 24h: commodity avg `-0.2062` n `12`; crypto_alt avg `0.4407` n `230`; crypto_major avg `0.7209` n `8`; equity avg `0.7403` n `114`; fx avg `-0.0159` n `6`; index avg `0.0852` n `25`; metal avg `0.2141` n `20`; unknown avg `0.0793` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1775`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1734`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1469`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1466`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.129`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
