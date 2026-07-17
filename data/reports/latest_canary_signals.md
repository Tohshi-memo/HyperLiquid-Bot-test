# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T19:52:33.727402+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0261` n `12`; crypto_alt avg `0.0421` n `230`; crypto_major avg `0.1154` n `8`; equity avg `-0.0555` n `96`; fx avg `-0.0043` n `6`; index avg `0.0029` n `25`; metal avg `0.0254` n `20`; unknown avg `-0.0485` n `769`
- 1h: commodity avg `-0.026` n `12`; crypto_alt avg `-0.3696` n `230`; crypto_major avg `-0.107` n `8`; equity avg `-0.1925` n `96`; fx avg `0.014` n `6`; index avg `-0.0179` n `25`; metal avg `0.0277` n `20`; unknown avg `-0.0542` n `769`
- 4h: commodity avg `0.2037` n `12`; crypto_alt avg `0.3158` n `230`; crypto_major avg `0.7463` n `8`; equity avg `0.3349` n `96`; fx avg `0.0288` n `6`; index avg `-0.0101` n `25`; metal avg `-0.022` n `20`; unknown avg `0.8901` n `769`
- 24h: commodity avg `0.6366` n `12`; crypto_alt avg `-1.1135` n `230`; crypto_major avg `-1.0814` n `8`; equity avg `-1.1339` n `94`; fx avg `0.0922` n `6`; index avg `-0.1672` n `25`; metal avg `-0.0226` n `20`; unknown avg `-0.0251` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
